"""
build_windninja_library.py — precompute a WindNinja diagnostic-wind library over the
Kandy basin (2026-06-05), to replace the hand-rolled channelling/drainage in
terrain_transport.py with physically-derived mass-consistent terrain winds.

WindNinja (Forthofer et al.; mass-conservation solver + Forthofer diurnal slope-flow
scheme) is run over the Kandy UTM DEM for a grid of conditions:
  direction : 16 bins (every 22.5°)
  speed     : 2 anchors {1, 4} m/s — the mass-consistent synoptic part scales ~linearly
              with input speed while the diurnal slope-flow part is ~fixed, so two
              anchors let us linearly reconstruct any speed (interp/extrapolate).
  regime    : night (03 LT, clear → katabatic drainage) and day (13 LT, clear → anabatic
              + daytime mixing/ventilation).
Each WindNinja velocity+angle grid (90 m, UTM) is converted to (u, v) (eastward,
northward) and resampled to the solver's 64×64 PINN lat/lon grid.

Out: data/processed/pinn_inputs/windninja_library.npz
     u,v : (16 dir, 2 speed, 2 regime, 64, 64)  + dirs, speeds, regimes, lats, lons
"""
from __future__ import annotations
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from config import KANDY_PINN_BBOX as BB

# NOTE: this is a DEV-ONLY rebuild utility. The wind library it produces
# (windninja_library.npz) is already shipped under data/processed/pinn_inputs/,
# so the model and figures run without it. Re-running this needs a local
# WindNinja 3.x install (not bundled): point WINDNINJA_CLI at the executable
# (and optionally WINDNINJA_WORKDIR at a scratch dir) before invoking.
CLI = Path(os.environ.get("WINDNINJA_CLI", "WindNinja_cli"))
DEM = REPO / "data" / "processed" / "pinn_inputs" / "kandy_dem_utm44n_90m.tif"
WORK = Path(os.environ.get("WINDNINJA_WORKDIR", Path(tempfile.gettempdir()) / "wn_lib"))
OUT = REPO / "data" / "processed" / "pinn_inputs" / "windninja_library.npz"

N = 64
DIRS = np.arange(0, 360, 22.5)          # 16 directions (FROM, met convention)
SPEEDS = [1.0, 4.0]                     # m/s anchors
REGIMES = [("night", 3, 22.0), ("day", 13, 28.0)]   # (name, hour LT, air_temp C)
MESH = 90


def read_asc(p: Path):
    h = {}
    with open(p) as f:
        for _ in range(6):
            k, v = f.readline().split(); h[k.lower()] = float(v)
        A = np.loadtxt(f)
    return A, h


def run_one(direction, speed, hour, temp, tag):
    WORK.mkdir(parents=True, exist_ok=True)
    cmd = [str(CLI), "--elevation_file", str(DEM),
           "--initialization_method", "domainAverageInitialization",
           "--input_speed", str(speed), "--input_speed_units", "mps",
           "--input_direction", str(int(direction)),
           "--input_wind_height", "10", "--units_input_wind_height", "m",
           "--output_wind_height", "10", "--units_output_wind_height", "m",
           "--vegetation", "grass", "--mesh_resolution", str(MESH), "--units_mesh_resolution", "m",
           "--diurnal_winds", "true", "--uni_air_temp", str(temp), "--air_temp_units", "C",
           "--uni_cloud_cover", "0", "--cloud_cover_units", "percent",
           "--year", "2023", "--month", "1", "--day", "15", "--hour", str(hour), "--minute", "0",
           "--time_zone", "Asia/Colombo", "--write_ascii_output", "true",
           "--output_path", str(WORK), "--num_threads", "4"]
    import glob as _glob
    sp_i = int(round(speed))
    pat = str(WORK / f"kandy_dem_utm44n_90m_{int(direction)}_{sp_i}_*_{hour:02d}00_{MESH}m_vel.asc")
    for attempt in range(2):
        subprocess.run(cmd, capture_output=True, text=True)   # phone-home stderr non-fatal
        hits = sorted(_glob.glob(pat), key=lambda f: Path(f).stat().st_mtime)
        if hits:
            vf = Path(hits[-1])
            vel, hv = read_asc(vf)
            ang, _ = read_asc(Path(str(vf).replace("_vel.asc", "_ang.asc")))
            return vel, ang, hv
        print(f"    retry dir={int(direction)} s={sp_i} h={hour} (attempt {attempt+1})")
    raise FileNotFoundError(pat)


def main():
    import pyproj
    from scipy.interpolate import RegularGridInterpolator
    assert CLI.exists(), f"WindNinja CLI not found at {CLI}"
    assert DEM.exists(), f"DEM not found at {DEM}"

    lats = np.linspace(BB["lat_min"], BB["lat_max"], N)
    lons = np.linspace(BB["lon_min"], BB["lon_max"], N)
    LA, LO = np.meshgrid(lats, lons, indexing="ij")
    tf = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32644", always_xy=True)
    X, Y = tf.transform(LO.ravel(), LA.ravel())          # product grid in UTM

    U = np.zeros((len(DIRS), len(SPEEDS), len(REGIMES), N, N))
    V = np.zeros_like(U)
    total = U.shape[0] * U.shape[1] * U.shape[2]; k = 0
    for di, d in enumerate(DIRS):
        for si, s in enumerate(SPEEDS):
            for ri, (rname, hour, temp) in enumerate(REGIMES):
                vel, ang, h = run_one(d, s, hour, temp, rname)
                nc, nr, x0, y0, cs = (int(h["ncols"]), int(h["nrows"]),
                                      h["xllcorner"], h["yllcorner"], h["cellsize"])
                ax = x0 + (np.arange(nc) + 0.5) * cs           # asc col centres (E)
                ay = y0 + (np.arange(nr) + 0.5) * cs           # asc row centres (N), row0=top→reverse
                gv = RegularGridInterpolator((ay[::-1], ax), vel, bounds_error=False, fill_value=None)
                ga = RegularGridInterpolator((ay[::-1], ax), ang, bounds_error=False, fill_value=None)
                pts = np.stack([Y, X], axis=1)
                spd = gv(pts).reshape(N, N)
                a_from = np.deg2rad(ga(pts).reshape(N, N))     # FROM direction (met)
                # vector blowing TO = FROM+180: u east, v north
                U[di, si, ri] = -spd * np.sin(a_from)
                V[di, si, ri] = -spd * np.cos(a_from)
                k += 1
                if k % 8 == 0 or k == total:
                    print(f"  {k}/{total}  dir={int(d)} s={s} {rname}  "
                          f"core|domain spd {spd[N//2,N//2]:.2f}|{spd.mean():.2f}")

    np.savez_compressed(OUT, u=U, v=V, dirs=DIRS, speeds=np.array(SPEEDS),
                        regimes=np.array([r[0] for r in REGIMES]), lats=lats, lons=lons,
                        regime_hours=np.array([r[1] for r in REGIMES]))
    print(f"\nlibrary {U.shape} -> {OUT}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
