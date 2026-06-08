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
PM(x, y, t) = B(t) + [ T(t) − B(t) ] · P_local(x, y, t)
```

- **B(t)** — regional and transboundary background (horizontally uniform per hour):
  a rural Van Donkelaar floor scaled by the GEOS-CF daily seasonal shape. The local
  fraction is ≈ 25 % (basin exposure ≈ 75 % regional / 25 % local), bracketed from
  source-apportionment literature.
- **T(t)** — the basin temporal anchor: a lag-free gradient-boosted series on
  exogenous drivers, conformal-wrapped, re-anchored per year to the Van Donkelaar
  area mean and amplitude-sharpened to the observed local diurnal/seasonal swing.
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

## Running it

```bash
# render the publication figure suite (F1–F13)
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
