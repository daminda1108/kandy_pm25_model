"""
export_kandy_dem_utm.py — export the Kandy SRTM elevation grid to a projected
GeoTIFF (UTM 44N, EPSG:32644) for WindNinja (2026-06-05).

WindNinja requires a DEM in a projected coordinate system (metres). We take the
100 m lat/lon elevation grid (kandy_elev_grid_100m.npz, the 15 km PINN domain),
write it as an EPSG:4326 GeoTIFF, then warp it to UTM 44N at 90 m. The output
DEM is the terrain input for the diagnostic-wind library.

Out: data/processed/pinn_inputs/kandy_dem_utm44n_90m.tif
"""
from __future__ import annotations
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
NPZ = REPO / "data" / "processed" / "pinn_inputs" / "kandy_elev_grid_100m.npz"
OUT = REPO / "data" / "processed" / "pinn_inputs" / "kandy_dem_utm44n_90m.tif"


def main():
    import rasterio
    from rasterio.transform import from_bounds
    from rasterio.warp import calculate_default_transform, reproject, Resampling

    z = np.load(NPZ)
    elev = z["elev"].astype("float32")
    la = z["lat_grid"][:, 0].astype(float); lo = z["lon_grid"][0, :].astype(float)
    # orient north-up (row 0 = north) for the GeoTIFF
    if la[0] < la[-1]:
        elev = elev[::-1, :]; la = la[::-1]
    if lo[0] > lo[-1]:
        elev = elev[:, ::-1]; lo = lo[::-1]
    ny, nx = elev.shape
    dlat = abs(la[0] - la[1]); dlon = abs(lo[1] - lo[0])
    west, east = lo.min() - dlon / 2, lo.max() + dlon / 2
    south, north = la.min() - dlat / 2, la.max() + dlat / 2
    src_tf = from_bounds(west, south, east, north, nx, ny)
    src_crs = "EPSG:4326"

    tmp = OUT.with_suffix(".ll.tif")
    with rasterio.open(tmp, "w", driver="GTiff", height=ny, width=nx, count=1,
                       dtype="float32", crs=src_crs, transform=src_tf,
                       nodata=-9999.0) as dst:
        dst.write(elev, 1)

    dst_crs = "EPSG:32644"   # UTM 44N (Sri Lanka)
    with rasterio.open(tmp) as src:
        tf, w, h = calculate_default_transform(src.crs, dst_crs, src.width, src.height,
                                               *src.bounds, resolution=90.0)
        with rasterio.open(OUT, "w", driver="GTiff", height=h, width=w, count=1,
                           dtype="float32", crs=dst_crs, transform=tf, nodata=-9999.0) as dst:
            reproject(source=rasterio.band(src, 1), destination=rasterio.band(dst, 1),
                      src_transform=src.transform, src_crs=src.crs,
                      dst_transform=tf, dst_crs=dst_crs, resampling=Resampling.bilinear)
    tmp.unlink(missing_ok=True)
    with rasterio.open(OUT) as d:
        a = d.read(1); a = a[a > -9000]
        print(f"wrote {OUT}")
        print(f"  size {d.width}x{d.height}  CRS {d.crs}  res {d.res[0]:.0f} m")
        print(f"  elev range {a.min():.0f}..{a.max():.0f} m  bounds {d.bounds}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
