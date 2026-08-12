# Kandy PM2.5 — a physically-structured decomposition model

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Status](https://img.shields.io/badge/status-research-orange.svg)
![Reproducible](https://img.shields.io/badge/reproducible-inputs%20included-brightgreen.svg)

Hourly PM2.5 at 1 km over the Kandy basin, Sri Lanka, with calibrated uncertainty and a
population-exposure and health-burden layer.

**Kandy has no public air-quality monitor.** That is the problem this model exists to
solve, and it shapes everything below: with nothing local to fit or to check against, the
model is built from physically separable terms that depend only on globally available
inputs, and is then validated by running it unchanged at ten cities that *do* have dense
monitoring networks.

**[Explore the output →](https://daminda1108.github.io/kandy-pm25-explorer/)**

---

## At a glance

| | |
|---|---|
| **Domain** | Kandy basin, Sri Lanka · 15 × 15 km · 1 km grid · hourly |
| **Period** | 2019–2026, in three tiers of decreasing confidence |
| **Validated** | 10 analogue cities, 5 countries, scored against withheld monitors |
| **Seasonal cycle** | *r* = 0.94–1.00 across all ten cities |
| **Diurnal cycle** | *r* = 0.60–0.98 in nine of ten |
| **Level transfer** | −4% to +30% (median +7.6%) |
| **Spatial rank** | significant against each city's own null in 6 of 9 estimable |
| **Kandy 2023** | basin mean 21.0 µg/m³ · 427 attributable deaths/yr [235–625] |

---

## Quickstart

Tested on Python 3.11.

```bash
git clone https://github.com/daminda1108/kandy_pm25_model.git
cd kandy_pm25_model
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

A single hour, rendered in seconds:

```bash
python scripts/nowcast.py --ts "2022-12-07 08:00" --label "Dec 2022 haze episode"
```

The whole field, rebuilt from the inputs in `data/`:

```bash
python scripts/regenerate_all.py
```

The publication figure suite:

```bash
python kandymodel/viz/paper_figures.py --figs all
```

The first figure render fetches OpenStreetMap basemap layers and caches them, so it needs
network access once. Everything else runs offline.

---

## The model

Concentration is a regional background plus a locally-structured increment:

```
inc = T(t) − B(t)

PM(x, y, t) = B(t) + max( max(inc, 0), ε ) · P_local(x, y, t)
                   + min(inc, 0) − max( 0, ε − max(inc, 0) )
```

- **`T(t)`** — the basin temporal anchor. A lag-free gradient-boosted series on exogenous
  drivers, conformal-wrapped, re-anchored each year to a satellite area mean.
- **`B(t)`** — the regional and transboundary background, horizontally uniform per hour.
- **`P_local`** — the spatial pattern, normalised to **unit spatial mean**: the product of a
  road-network emission surface, terrain confinement, and transport along mass-consistent
  diagnostic winds over the real topography.

**The unit-mean normalisation is the load-bearing constraint.** It means the basin average
returns `T(t)` exactly, so the level and the pattern are separately identifiable and can be
validated independently. Everything the model claims rests on that separation.

The two correction terms beyond the plain `B + inc·P_local` form each fix a defect that
ground truth exposed. The **increment split** stops the model rendering the city core
*cleaner* than the rural edge when the hourly total dips below the daily-resolution
background. The **ventilated-hour floor `ε`** stops those hours rendering perfectly flat,
which withheld stations at Medellín show they are not. Both are mean-zero or
accumulation-side by construction, so the basin mean is preserved exactly and structured
hours are unchanged.

### The regional/local split

About **48% of the annual mean is locally generated**, and that figure follows from a
physical constraint rather than an assumption. Local sources emit continuously, so the
local increment at an emitting location is strictly positive at every hour — rain changes
removal, not emission — and the background therefore can never reach the total. Imposing
that constraint yields *f* ≈ 0.48, and the result is insensitive to the one free parameter
(a fourfold sweep moves it from 0.477 to 0.502). It agrees with three independent lines: a
coherence floor of ≥0.41 derived from the anchor alone, a hierarchical fit with Kandy held
out at 0.392, and a national-network instrument at 0.446.

Because the field is anchor-locked, the level, exposure and burden are arithmetically
unchanged by this. What changes is the attribution.

---

## Confidence tiers

The three periods are **not** equally trustworthy, and the model labels them everywhere:

| tier | period | basis |
|---|---|---|
| **Anchored** | 2019–2023 | Level pinned to the satellite product. The years the ten-city panel scored. |
| **Extension** | 2024–2026 | The satellite anchor ends in 2023; level modelled from meteorology. Episode *frequency* is corrected and validated by holding out anchored years; episode *timing* is not. |
| **Forecast** | rolling 5 days | A demonstration. No local verification is possible; intervals are deliberately widened. |

---

## Validation

Kandy cannot check this model, so the model is checked elsewhere. Every term uses inputs
available for any city, so the identical pipeline runs at ten cities with dense networks —
**restricted to Kandy's two-sensor information budget** — and is scored against monitors it
never saw.

The most complete single test is Kathmandu: 39 held-out stations, seasonal and diurnal
cycles both reproduced at *r* = 0.97, level within 1%.

Full per-city results: [`evidence/results/validation_scorecard.csv`](evidence/results/validation_scorecard.csv).

**What transfers:** temporal structure and the anchored level, across regimes.
**What does not transfer uniformly:** fine within-city spatial rank, which is significant
in six of nine estimable cities and absent in the rest.

---

## Evidence and pre-registration

[`evidence/`](evidence/) holds the reasoning, not just the results:

- **six pre-registrations** with gates, falsifiers and the expected outcome recorded
  *before* each test ran;
- a **43-entry epistemic ledger** tagging every quantity as **observed**, **learned** or
  **imposed**, with the test that would falsify it;
- the machine-readable artifacts behind each number.

Not every pre-registered test passed, which is why they are all published. One produced a
result that improved the headline number and was **not** adopted, because its validity gate
could not be evaluated. Another plan was abandoned at a gate set in advance rather than
moving the threshold.

---

## Data

`data/` ships the ~8 MB of **derived inputs** the pipeline needs, so a fresh clone
reproduces the field. Third-party raw observations are deliberately not redistributed.
[`data/README.md`](data/README.md) states what is included, what is not, why, and how to
obtain the rest. Upstream attributions are listed there and must travel with any reuse.

---

## Limitations

Stated plainly, because they bound what the output can be used for.

- **The fine within-city spatial pattern is imposed from physics, not measured.** No public
  monitoring network anywhere samples the valley-floor-to-ridge gradient, and five
  independent tests indicate the pattern cannot be learned from public covariates either.
  The direction is defensible; the annual core-to-edge contrast (~1.2×) is the figure to
  quote, not any single hour.
- **The hourly regional/local split is not identifiable.** References built from real, dense
  networks show the same pathology in 13–25% of hours. The split is reported annually.
- **The shipped interval is correctly scaled but not centred for point comparison.** The
  field is a 1 km area mean and any monitor is a point; expect an offset of +5 to +6 µg/m³
  before drawing conclusions from a future measurement.
- **The health estimate** propagates field uncertainty only, not structural uncertainty in
  the concentration-response functions.

The decisive missing input is a single monitor inside or upwind of the basin.

---

## Repository layout

```
kandymodel/            the model package
├── level.py           satellite area-mean level anchor
├── background.py      B(t) regional/transboundary background
├── anchor/            T(t) temporal anchor: predict, train
├── emission/          emission surface, traffic centrality, diurnal timing
├── confinement/       M(x,y,t) terrain confinement
├── transport/         terrain advection–dispersion, WindNinja winds
├── assemble/          decomposition map, additive field (headline)
├── exposure.py        population weighting
├── health.py          GEMM attributable burden
├── validate/          cross-checks against independent products
└── viz/               figure suite (F1–F13), styling, basemap
scripts/               regenerate_all, nowcast, and build steps
data/                  derived inputs (tracked) · outputs (regenerated)
evidence/              pre-registrations, epistemic ledger, result artifacts
config.py              constants and paths
```

---

## Citation

```bibtex
@software{alahakoon2026kandy,
  author  = {Alahakoon, Daminda},
  title   = {Kandy PM2.5: a physically-structured decomposition model},
  year    = {2026},
  version = {1.0.0},
  url     = {https://github.com/daminda1108/kandy_pm25_model}
}
```

See [`CITATION.cff`](CITATION.cff), or GitHub's "Cite this repository" button. Please cite
the upstream data sources listed in [`data/README.md`](data/README.md) as well.

## Licence

Code released under the [MIT License](LICENSE). MIT covers this project's own code and
derived products; it does not re-license the upstream data, which carries the terms of each
source.

---

*Undergraduate thesis, Department of Environmental Sciences, University of Peradeniya.
Supervisors: Dr. U. Ranathunge, Dr. M. Dehideniya.*
