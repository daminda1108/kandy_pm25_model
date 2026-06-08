"""nowcast_figure.py — single-timestamp PM2.5 "nowcast card" for Kandy (2026-06-06).

Demonstrates that the model can reconstruct the full 1 km spatial PM2.5 field for ANY
hour in 2019-2023. Default: 2022-01-01 07:00 LT (DJF NE-monsoon morning rush). The
requested time is linearly interpolated from the two bracketing native hours (the hourly
grid sits at UTC whole-hours = local :30).

Panels:  (a) the PM2.5 field + WindNinja flow + emission-intensity contours + landmarks
         (b) plausible upper bound this hour (90% PI q95)
         (c) the day's diurnal curve with the requested hour marked
         (d) conditions + additive decomposition (regional B vs local increment) readout

Run:  python scripts/nowcast_figure.py  [--ts "2022-01-01 07:00"]
Out:  results/figures/paper_figures/NOWCAST_<ts>.png
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
from kandymodel.viz import helpers as pf
from kandymodel.transport import terrain as tt
from kandymodel.viz.basemap import _draw, _elev, _scale_bar, _north_arrow

DEC = pf.DEC; STG = pf.STG; CEN = pf.CEN


def _grid(sl, col, lats, lons):
    return sl.groupby(["lat", "lon"])[col].mean().unstack("lon").reindex(index=lats, columns=lons).values


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--ts", default="2022-01-01 07:00")
    ap.add_argument("--label", default=""); a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    tgt = pd.Timestamp(a.ts, tz="Asia/Colombo"); year = tgt.year; tgtU = tgt.tz_convert("UTC")
    d = pd.read_parquet(DEC / f"kandy_decomp_predictions_{year}_additive.parquet")
    d["tutc"] = pd.to_datetime(d.time, utc=True); d["loct"] = d.tutc.dt.tz_convert("Asia/Colombo")
    hrs = pd.to_datetime(np.sort(d.tutc.unique()), utc=True)
    i1 = int(hrs.searchsorted(tgtU)); i0 = max(i1 - 1, 0); i1 = min(i1, len(hrs) - 1)
    t0, t1 = hrs[i0], hrs[i1]
    w = 0.0 if t1 == t0 else float((tgtU - t0) / (t1 - t0))               # interp weight to t1
    lats = np.sort(d.lat.unique()); lons = np.sort(d.lon.unique())
    def interp(col):
        Z0 = _grid(d[d.tutc == t0], col, lats, lons); Z1 = _grid(d[d.tutc == t1], col, lats, lons)
        return (1 - w) * Z0 + w * Z1
    Z = interp("pm25_q50"); Zhi = interp("pm25_q95"); Zlo = interp("pm25_q05")

    # background B this hour (uniform) → local increment
    B = pd.read_parquet(DEC / f"B_background_hourly_{year}.parquet")
    B["tutc"] = pd.to_datetime(B["time"] if "time" in B else B.iloc[:, 0], utc=True)
    bcol = [c for c in B.columns if c.lower().startswith("b") and B[c].dtype.kind == "f"][0]
    Bv = float((1 - w) * B.loc[B.tutc == t0, bcol].mean() + w * B.loc[B.tutc == t1, bcol].mean())

    # met + WindNinja wind for the interpolated hour
    m = pd.read_parquet(STG / f"inference_grid_{year}_s12451.parquet",
                        columns=["datetime_utc", "u10", "v10", "blh_m", "wind_speed_10m"])
    m["tutc"] = pd.to_datetime(m.datetime_utc, utc=True)
    def mval(c):
        return float((1 - w) * m.loc[m.tutc == t0, c].mean() + w * m.loc[m.tutc == t1, c].mean())
    u, v, blh, spd = mval("u10"), mval("v10"), mval("blh_m"), mval("wind_speed_10m")
    frm = (np.degrees(np.arctan2(u, v)) + 180) % 360
    wn = tt.windninja_wind(u, v, blh)
    L = np.load(pf.PIN / "windninja_library.npz", allow_pickle=True)
    U, V, wla, wlo = (wn[0], wn[1], L["lats"], L["lons"]) if wn is not None else (None, None, None, None)

    core = Z[np.argmin(np.abs(lats - 7.2906)), np.argmin(np.abs(lons - 80.6337))]
    basin = float(np.nanmean(Z)); incr_core = core - Bv
    season = ["DJF", "DJF", "MAM", "MAM", "MAM", "JJA", "JJA", "JJA", "SON", "SON", "SON", "DJF"][tgt.month - 1]
    hr = tgt.hour
    daypart = ("deep night" if hr < 6 else "morning rush" if hr < 10 else "midday" if hr < 16
               else "evening rush" if hr < 20 else "night")

    # ── figure ──────────────────────────────────────────────────────────────
    fig = plt.figure(figsize=(7.2, 5.6))
    gs = fig.add_gridspec(2, 3, width_ratios=[1.5, 1, 1], height_ratios=[1.35, 1], hspace=0.28, wspace=0.32)
    # per-hour adaptive range so the spatial structure shows at any pollution level
    # (snapshot view; absolute basin/core are stated in the title). 5 even ticks.
    def _rng(A, padlo=3, padhi=99.5):
        lo_ = np.floor(np.nanpercentile(A, padlo) / 5) * 5
        hi_ = np.ceil(np.nanpercentile(A, padhi) / 5) * 5
        return float(lo_), float(max(hi_, lo_ + 10))
    import matplotlib.colors as mcolors
    lo, hi = _rng(Z); lob, hib = _rng(Zhi)
    # CANONICAL nowcast scaling (user 2026-06-06): auto-switch panel (a) by pollution level.
    # decider = field hotspot (98th pct); WHO IT-1 = 35 µg/m³ marks the "unhealthy" line.
    #   episode (≥35)  → TURBO + fixed universal 8–90  → severity comparable across episodes
    #   ordinary (<35) → YlOrRd + per-hour adaptive     → max spatial structure on a normal hour
    # panel (b) upper bound is ALWAYS YlOrRd (per-hour adaptive).
    EPISODE_PM = 35.0
    episode = float(np.nanpercentile(Z, 98)) >= EPISODE_PM
    if episode:
        cmapA = "turbo"; normA = mcolors.PowerNorm(0.85, vmin=8, vmax=90)
        tkA = [15, 25, 35, 50, 70, 90]; sctag = "universal"
    else:
        cmapA = pf.PM_CMAP; normA = pf.pm_norm(vmin=lo, vmax=hi, gamma=1.05)
        tkA = list(np.linspace(lo, hi, 5).round().astype(int)); sctag = "adaptive"
    # (a) main field
    axm = fig.add_subplot(gs[0, 0:2])
    im = _draw(axm, Z, lats, lons, cmapA, norm=normA, show_marks=False)
    if U is not None:
        pf.quiver(axm, U, V, wla, wlo, step=7, color="white", lw=0.6)
    pf.emission_contours(axm, lw=0.6)
    _scale_bar(axm, lats, lons); _north_arrow(axm, lats, lons)
    axm.set_title(f"(a) PM$_{{2.5}}$ field — {tgt:%Y-%m-%d %H:%M} LT  (basin {basin:.0f}, core {core:.0f} µg m$^{{-3}}$)", fontsize=8.8)
    axm.set_xticks([]); axm.set_yticks([])
    fig.colorbar(im, ax=axm, extend="max", ticks=tkA, shrink=0.85, label=f"PM$_{{2.5}}$ (µg m$^{{-3}}$, {sctag})")
    # (b) 90% upper bound — always YlOrRd, per-hour adaptive
    axu = fig.add_subplot(gs[0, 2])
    imu = _draw(axu, Zhi, lats, lons, pf.PM_CMAP, norm=pf.pm_norm(vmin=lob, vmax=hib, gamma=1.05), show_marks=False)
    axu.set_title(f"(b) 90% upper bound\n(q95, core {Zhi[np.argmin(np.abs(lats-7.2906)),np.argmin(np.abs(lons-80.6337))]:.0f})", fontsize=8.2)
    axu.set_xticks([]); axu.set_yticks([]); fig.colorbar(imu, ax=axu, shrink=0.8, label="µg m$^{-3}$")
    # (c) diurnal context for that day + FECT ground-sensor overlay (validation)
    day = d[(d.loct.dt.date == tgt.date())].groupby(d.loct.dt.hour).pm25_q50.mean()
    axd = fig.add_subplot(gs[1, 0])
    axd.plot(day.index, day.values, "o-", color="#B35806", lw=1.8, ms=3, label="model basin")
    try:
        fe = pd.read_parquet(STG / "dataset_v3_hourly.parquet", columns=["datetime_utc", "sensor_id", "pm25_observed"])
        fe["loct"] = pd.to_datetime(fe.datetime_utc, utc=True).dt.tz_convert("Asia/Colombo")
        fe = fe[(fe.sensor_id == 12451) & (fe.loct.dt.date == tgt.date())].dropna(subset=["pm25_observed"])
        if len(fe) >= 3:
            axd.plot(fe.loct.dt.hour, fe.pm25_observed, "s", color="#1A9850", ms=3.5, label="FECT obs")
            mh = day.reindex(fe.loct.dt.hour.values)
            rr = np.corrcoef(mh.values, fe.pm25_observed.values)[0, 1] if mh.notna().sum() > 2 else np.nan
            axd.legend(fontsize=5.6, loc="upper left", title=f"r={rr:+.2f}" if np.isfinite(rr) else None, title_fontsize=5.6)
    except Exception as ex:
        print(f"  (FECT overlay skipped: {ex})")
    axd.axvline(tgt.hour, color="crimson", ls="--", lw=1.2)
    axd.set_title("(c) diurnal cycle + FECT obs", fontsize=8.2); axd.set_xlabel("local hour"); axd.set_ylabel("PM$_{2.5}$ (µg m$^{-3}$)"); axd.set_xticks(range(0, 24, 6)); axd.grid(alpha=.25)
    # (d) decomposition + conditions readout
    axb = fig.add_subplot(gs[1, 1])
    axb.bar(["basin", "core"], [Bv, Bv], color="#9ECAE1", label="regional B")
    axb.bar(["basin", "core"], [basin - Bv, incr_core], bottom=[Bv, Bv], color="#E6550D", label="local increment")
    axb.set_title("(d) additive split (this hour)", fontsize=8.2); axb.set_ylabel("µg m$^{-3}$")
    axb.legend(fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2); axb.grid(axis="y", alpha=.25)
    axt = fig.add_subplot(gs[1, 2]); axt.axis("off")
    txt = (f"$\\bf{{{tgt:%Y-%m-%d}}}$\n$\\bf{{{tgt:%H:%M}\\ LT}}$  ({season}, {daypart})\n\n"
           f"wind  {spd:.1f} m/s from {frm:.0f}°\nBLH   {blh:.0f} m (shallow → trapping)\n\n"
           f"basin   {basin:.1f}  µg m⁻³\ncore    {core:.1f}  µg m⁻³\n90% PI  {np.nanmean(Zlo):.0f}–{np.nanmean(Zhi):.0f}\n\n"
           f"regional {Bv:.0f} ({Bv/basin*100:.0f}%)\nlocal    {basin-Bv:.0f} ({(1-Bv/basin)*100:.0f}%)")
    axt.text(0.0, 0.98, txt, va="top", ha="left", fontsize=7.6, family="monospace")
    sub = a.label if a.label else f"{season} {daypart}"
    fig.suptitle(f"Kandy PM$_{{2.5}}$ nowcast — {tgt:%Y-%m-%d %H:%M} local — {sub}", fontsize=9.5)
    pf.square_heatmaps(fig)                                 # canonical: square map panels
    out = pf.PAPER_OUT / f"NOWCAST_{tgt:%Y%m%d_%H%M}.png"
    fig.savefig(out, dpi=400, bbox_inches="tight"); plt.close(fig)
    print(f"  basin {basin:.1f}  core {core:.1f}  B {Bv:.1f}  wind {spd:.1f}@{frm:.0f}  BLH {blh:.0f}")
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
