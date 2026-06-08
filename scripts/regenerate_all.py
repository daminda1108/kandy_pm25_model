"""regenerate_all.py — rebuild the Kandy PM2.5 decomposition end to end.

Runs the locked chain in order, from the provided intermediate artifacts:

    T(t) anchor -> sharpen -> decomp map -> transport overlay -> spatial UQ
      -> additive field -> exposure -> health -> figures

The static source grids (S_emit, M-confinement, S_traffic, the WindNinja wind
library) are shipped prebuilt under data/processed/; they are NOT rebuilt here
because that needs the raw Van Donkelaar / OSM inputs which are not part of this
release. Pass --from-anchor to also re-derive T(t) from the inference grids.

Usage:
    python scripts/regenerate_all.py                 # from provided T(t)
    python scripts/regenerate_all.py --from-anchor   # also rebuild T(t)
    python scripts/regenerate_all.py --figs-only      # just re-render figures
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PY = sys.executable
YEARS = [2019, 2020, 2021, 2022, 2023]


def run(desc: str, *args: str) -> None:
    print(f"\n=== {desc} ===", flush=True)
    r = subprocess.run([PY, *args], cwd=ROOT)
    if r.returncode != 0:
        sys.exit(f"FAILED at: {desc} (exit {r.returncode})")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-anchor", action="store_true",
                    help="also re-derive T(t) from the inference grids")
    ap.add_argument("--figs-only", action="store_true",
                    help="skip the build chain, just re-render the figure suite")
    a = ap.parse_args()

    if not a.figs_only:
        if a.from_anchor:
            for y in YEARS:
                run(f"T(t) anchor {y}", "kandymodel/anchor/predict_anchor.py", "--year", str(y))
            run("sharpen T(t) diurnal/seasonal", "scripts/sharpen_T_diurnal.py")
        for y in YEARS:
            run(f"decomp map {y}", "kandymodel/assemble/decomp_map.py", "--year", str(y))
        run("transport overlay (4-factor)", "scripts/build_overlay_predictions.py")
        run("spatial UQ", "scripts/build_spatial_uq.py")
        run("additive field (headline)", "kandymodel/assemble/additive_field.py")
        run("exposure weighting", "kandymodel/exposure.py")
        run("health burden (GEMM)", "kandymodel/health.py")
        run("seasonal + episodic fields", "scripts/build_seasonal_episodic_fields.py")

    run("publication figure suite F1-F13", "kandymodel/viz/paper_figures.py", "--figs", "all")
    print("\nALL DONE — outputs under data/processed/decomp/ and results/figures/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
