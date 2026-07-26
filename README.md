# Kandy PM2.5 — Additive Decomposition Model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Status](https://img.shields.io/badge/status-research-orange.svg)

A physically-structured spatiotemporal PM2.5 model for the Kandy basin, Sri Lanka,
at 1 km hourly resolution for 2019–2023, with calibrated uncertainty and a
population-exposure / health-burden layer.

This repository is the isolated, runnable production model. It contains only the
additive-decomposition pipeline and its canonical figure suite — none of the
exploratory PINN / cross-city ConvCNP / analogue-finder work that preceded it.

## The model

```
inc  = T(t) − B(t)
PM(x, y, t) = B(t) + max( max(inc, 0), ε ) · P_local(x, y, t)
                   + min(inc, 0)  −  max( 0, ε − max(inc, 0) )
```

The two correction terms beyond the plain `B + inc·P_local` form are deliberate and
each fixes a defect that ground truth exposed:

- the **increment split** (`max(inc,0)` / `min(inc,0)`) — when the hourly total dips
  below the daily-resolution background (deep midday mixing, ~38 % of hours), the plain
  form multiplies a core-high pattern by a *negative* increment and renders the city
  core **cleaner** than the rural edge. The split lets the pattern structure only the
  accumulation above background; ventilation below it is spatially uniform.
- the **ventilated-hour floor ε** — the split alone renders those hours perfectly flat,
  but Medellín's withheld network keeps real spatial spread on exactly those hours.
  ε is mean-zero by construction, so the basin mean (the T-lock) is preserved
  *exactly*, and ε ≥ 0 with an accumulation-side pattern means the core can never fall
  below the edge. Validated at Medellín on stations never used to fit it
  (flat-hour RMSE 8.53 → 8.00). Default `EPS_FLOOR = 2.573` (the shipped Kandy value,
  a disclosed method transfer); set `KANDY_EPS_FLOOR=0` to reproduce the paper tier.

Both collapse to the plain form wherever the increment is healthy, so structured hours
are unchanged.

- **B(t)** — regional and transboundary background (horizontally uniform per hour):
  a rural Van Donkelaar floor scaled by the GEOS-CF daily seasonal shape. The local
  fraction is ≈ 25 % (basin exposure ≈ 75 % regional / 25 % local), bracketed from
  source-apportionment literature.
- **T(t)** — the basin temporal anchor: a lag-free gradient-boosted series on
  exogenous drivers, conformal-wrapped, re-anchored per year to the Van Donkelaar
  area mean, then amplitude-sharpened. Be precise about what depends on local data
  here: the annual **level** uses **no local measurement** (satellite only), whereas
  the diurnal/seasonal **amplitude** is calibrated against two local research
  low-cost sensors — the model trains on their record and its climatological swing is
  matched to theirs, because a lag-free learner otherwise damps the daily cycle by
  ~15 %. Those sensors are not a public, retrievable series, but they are local. The
  evidence that the *method* recovers the shape without them is the transfer result
  across the analogue-city panel, not this field.
- **P_local** — a unit-mean spatial pattern (so the basin mean is preserved exactly):
  the normalised product of emission structure (Van Donkelaar surface + a
  congestion-weighted traffic source), boundary-layer-scaled terrain confinement, and
  a transport overlay on WindNinja mass-consistent diagnostic winds.

The transport overlay is a physically-motivated scenario; the fine-scale spatial
*magnitude* is imposed from physics and not yet independently measured (no public
monitoring network samples the valley-floor-to-ridge gradient). Temporal behaviour
and basin level are corroborated by two independent satellite products.

## Layout

```
kandymodel/                 the model package
├── level.py                Van Donkelaar area-mean level anchor + S_emit grid
├── background.py           B(t) regional/transboundary background
├── anchor/                 T(t): predict_anchor, train_lgbm, (sharpen in scripts/)
├── emission/               s_emit, traffic (congestion-weighted), timing e(t)
├── confinement/            M(x,y,t) terrain confinement: build, calibrate
├── transport/              terrain advection–dispersion + WindNinja winds
├── assemble/               decomp_map, additive_field (headline)
├── exposure.py · health.py population-weighting + GEMM burden
├── validate/               validate, GHAP/NO2 cross-checks, Senarathna reference
└── viz/                    style, basemap, helpers, paper_figures (F1–F13)
scripts/                    regenerate_all, nowcast, sharpen_T_diurnal,
                            build_overlay_predictions/spatial_uq/windninja_library/…
data/  results/             intermediate artifacts + outputs (gitignored)
config.py                   constants and paths
```

## Install

Tested on Python 3.11. From the repository root:

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The figure suite pulls OSM layers (roads / river / places) for the study-area
basemap on first run and caches them under `data/processed/decomp/osm_kandy/`, so
the first render needs network access; later runs work offline. Rendering the full
F1–F13 suite takes a few minutes on a laptop CPU; a single nowcast is seconds.

## Running it

All commands are run from the repository root.

```bash
# render the publication figure suite (F1–F13) → results/figures/paper_figures/
python kandymodel/viz/paper_figures.py --figs all

# single-hour nowcast for any hour in the record
python scripts/nowcast.py --ts "2022-12-07 08:00" --label "Dec 2022 episode"

# rebuild the whole chain from the provided artifacts
python scripts/regenerate_all.py              # from the provided T(t)
python scripts/regenerate_all.py --from-anchor  # also re-derive T(t)
```

The shipped `data/` contains the intermediate artifacts the chain reads (the static
S_emit / M / S_traffic / WindNinja grids, the T(t) parquets and inference grids, the
lag-free boosters, the per-year field parquets, and the raw GEOS-CF daily CSVs). A
full rebuild from raw satellite / reanalysis inputs is out of scope for this release.

## Provenance

Extracted from the research project `kandy_pm25` (D. Alahakoon, University of
Peradeniya). The full development history, validation record, and the exploratory
work that motivated this model live in the parent repository.

## Citation

If you use this model or its outputs, please cite it (see `CITATION.cff`, or use
GitHub's "Cite this repository" button):

> Alahakoon, D. (2026). *Kandy PM2.5 — Additive Decomposition Model* (Version 1.0.0)
> [Software]. https://github.com/daminda1108/kandy_pm25_model

## License

Released under the [MIT License](LICENSE).
