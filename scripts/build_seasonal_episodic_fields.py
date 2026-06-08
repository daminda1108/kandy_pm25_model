"""build_seasonal_episodic_fields.py — per-season wind-resolved dispersion patterns +
an episodic worst-case accumulation field, for the publication figures (2026-06-06).

Motivation (user): the seasonal figures looked flat — the NE↔SW monsoon wind reversal
and the calm-season terrain entrapment of the Hantana-enclosed core were not visible,
and time-averaging washes out the high-emission stagnation SPIKES. This precomputes,
straight from ERA5→WindNinja→solver (the same machinery as build_overlay_predictions):

  • seas_A[season]      16×16 mean transport pattern A (headline cap 0.5, basin-mean 1)
  • seas_Astrong[season]16×16 entrapment-STRONG scenario (cap 1.4) — the labelled physical
                        scenario the user asked to show beside the validated-flat headline
  • seas_uv[season]     64×64 WindNinja regime-mean wind (U,V) for the per-season quiver
                        (DJF blows toward SW, JJA toward NE — the monsoon reversal)
  • episode             16×16 ABSOLUTE worst-case PM field: inter-monsoon stable-night /
                        low-BLH decile × evening-rush emission, confinement uncapped & NOT
                        renormalised → the core spike (honest scenario, wide UQ).

ERA5 sets WHEN/HOW-HARD the wind blows + the mixing depth; WindNinja sets WHAT THE TERRAIN
DOES to it (channelling, Hantana blocking, night drainage); the solver sets WHERE pollution
piles up. Output: data/processed/decomp/seasonal_episodic_fields.npz
"""
from __future__ import annotations
import sys
from pathlib import Path

import numpy as np
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(REPO / "scripts"))
import build_overlay_predictions as bo   # reuse _met_table, _shape16, _SHAPE_CACHE, grids
from kandymodel.emission.timing import e_at
from kandymodel.transport import terrain as tt

DEC = REPO / "data" / "processed" / "decomp"
STG = REPO / "data" / "processed" / "stage1_v3"
YEARS = range(2019, 2024)
SEAS = {"DJF": [12, 1, 2], "MAM": [3, 4, 5], "JJA": [6, 7, 8], "SON": [9, 10, 11]}
AMP_HEAD, AMP_STRONG = 0.5, 1.4          # headline cap vs entrapment-strong scenario cap


def _A(shape, lh, wind, blh, cap, lo, hi):
    amp = np.clip(e_at(lh) * 18.0 / (max(wind, 0.3) * max(blh, 1)), 0, cap)
    A = np.clip(1.0 + amp * (shape - 1.0), lo, hi)
    return A / A.mean()


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    lats16 = np.sort(pd.read_parquet(DEC / "kandy_decomp_predictions_2023.parquet",
                                     columns=["lat"]).lat.unique())
    lons16 = np.sort(pd.read_parquet(DEC / "kandy_decomp_predictions_2023.parquet",
                                     columns=["lon"]).lon.unique())
    # pooled (sector×BLH) mean met for the shape lookup (identical to build_overlay)
    pool = pd.concat([bo._met_table(y).reset_index() for y in YEARS], ignore_index=True)
    bin_means = {(int(s), int(b)): (g.u10.mean(), g.v10.mean(), g.blh_m.mean())
                 for (s, b), g in pool.groupby(["sector", "bbin"])}

    sumA = {s: np.zeros((16, 16)) for s in SEAS}
    sumAs = {s: np.zeros((16, 16)) for s in SEAS}
    cnt = {s: 0 for s in SEAS}
    sumuv = {s: [0.0, 0.0, 0.0] for s in SEAS}          # u,v,blh accumulators
    mon2sea = {m: s for s, ms in SEAS.items() for m in ms}

    for y in YEARS:
        met = bo._met_table(y)
        mon = pd.to_datetime(met.index, utc=True).tz_convert("Asia/Colombo").month
        for (r, mo) in zip(met.itertuples(), mon):
            s = mon2sea[int(mo)]
            bm = bin_means[(int(r.sector), int(r.bbin))]
            shape = bo._shape_for(r.sector, r.bbin, bm[0], bm[1], bm[2], lats16, lons16)
            sumA[s] += _A(shape, r.lh, r.wind_speed_10m, r.blh_m, AMP_HEAD, 0.5, 2.8)
            sumAs[s] += _A(shape, r.lh, r.wind_speed_10m, r.blh_m, AMP_STRONG, 0.4, 4.0)
            cnt[s] += 1
            sumuv[s][0] += r.u10; sumuv[s][1] += r.v10; sumuv[s][2] += r.blh_m
        print(f"  {y} pooled ({len(met)} h)")

    seas_A = {s: sumA[s] / cnt[s] for s in SEAS}
    seas_As = {s: sumAs[s] / cnt[s] for s in SEAS}
    # per-season WindNinja regime-mean wind (ERA5 season mean → WindNinja terrain field)
    seas_uv = {}
    for s in SEAS:
        u, v, blh = (sumuv[s][0] / cnt[s], sumuv[s][1] / cnt[s], sumuv[s][2] / cnt[s])
        w = tt.windninja_wind(u, v, blh)
        seas_uv[s] = (w[0], w[1]) if w is not None else (None, None)
        d = np.hypot(lats16[:, None] - 7.2906, lons16[None, :] - 80.6337)
        core = seas_A[s][d <= np.percentile(d, 20)].mean()
        edge = seas_A[s][d >= np.percentile(d, 80)].mean()
        print(f"  {s}: ERA5 u{u:+.2f} v{v:+.2f} blh{blh:.0f}  core/edge head {core/edge:.2f}× "
              f"strong {seas_As[s][d<=np.percentile(d,20)].mean()/seas_As[s][d>=np.percentile(d,80)].mean():.2f}×")

    # ── episodic worst case: inter-monsoon (MAM) stable-night/low-BLH × evening rush ──
    mam = pool[pd.to_datetime(pool.time, utc=True).dt.tz_convert("Asia/Colombo").dt.month.isin([3, 4, 5])]
    stag = mam[mam.blh_m <= mam.blh_m.quantile(0.10)]               # low-BLH stagnation decile
    u_e, v_e, blh_e = stag.u10.mean(), stag.v10.mean(), stag.blh_m.mean()
    wind_e = np.hypot(u_e, v_e)
    shp = np.clip(bo._shape16(u_e, v_e, blh_e, lats16, lons16), 0.5, 2.5)  # temper extreme tail
    amp_e = min(e_at(18) * 18.0 / (max(wind_e, 0.3) * max(blh_e, 1)), 0.6)  # evening rush, capped
    A_ep = np.clip(1.0 + amp_e * (shp - 1.0), 0.5, 3.0)
    A_ep = A_ep / A_ep.mean()                                       # spatial pattern, mean 1
    # absolute level = validated smooth basin × diurnal+seasonal peak factor; core lifted by A_ep
    sm = pd.concat([pd.read_parquet(DEC / f"kandy_decomp_predictions_{y}.parquet",
                                    columns=["lat", "lon", "pm25_q50"]) for y in YEARS])
    base = sm.groupby(["lat", "lon"]).pm25_q50.mean().unstack("lon").reindex(
        index=lats16, columns=lons16).values
    Tcol = pd.concat([pd.read_parquet(STG / f"T_anchor/T_kandy_hourly_{y}.parquet",
                                      columns=["T_q50"]) for y in YEARS]).T_q50
    peak = float(min(Tcol.quantile(0.97) / Tcol.mean(), 2.4))       # diurnal+seasonal peak hour
    episode = base * peak * A_ep                                    # absolute µg/m³ (basin ≈ base·peak)
    print(f"\n  episode (MAM stable-night low-BLH × 18LT rush): BLH {blh_e:.0f} wind {wind_e:.2f} "
          f"ampE {amp_e:.2f} peak×{peak:.2f} A_ep core/edge "
          f"{A_ep.max()/A_ep.min():.2f}× -> core {np.nanmax(episode):.0f}  basin {np.nanmean(episode):.0f} µg/m³")

    out = DEC / "seasonal_episodic_fields.npz"
    np.savez(out, lats16=lats16, lons16=lons16,
             seas=list(SEAS), seas_A=np.stack([seas_A[s] for s in SEAS]),
             seas_As=np.stack([seas_As[s] for s in SEAS]),
             seas_U=np.stack([seas_uv[s][0] for s in SEAS]),
             seas_V=np.stack([seas_uv[s][1] for s in SEAS]),
             wn_lats=np.load(bo.REPO / "data/processed/pinn_inputs/windninja_library.npz")["lats"],
             wn_lons=np.load(bo.REPO / "data/processed/pinn_inputs/windninja_library.npz")["lons"],
             episode=episode, A_ep=A_ep, episode_meta=np.array([blh_e, wind_e, amp_e, peak]))
    print(f"\nwrote {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
