# Evidence

The claims in this project rest on tests that were specified before they were run, and on
results that were recorded whether or not they were welcome. This directory holds both, so a
reader can check the reasoning rather than take it on trust.

Start with `F_epistemic_ledger.md`. It is the spine of the whole project: 43 dated entries,
each recording what was tried, what the gate was, what happened, and what it changed. Several
entries record errors and retractions, including claims of mine that were withdrawn after
their own falsifier fired.

---

## `prereg/` — pre-registrations

Six tests, each with its gates, its falsifiers and the author's expected outcome **written
down before the test was run**. They are included precisely because not all of them passed.

| file | question | outcome |
|---|---|---|
| `prereg_spatial_resolution_2026-08-06.md` | is spatial skill being measured at the wrong resolution? | Test A **falsified**; Test B partially survived |
| `prereg_common_hours_spatial_2026-08-07.md` | can a rank statistic avoid laundering temporal skill? | validity gate **unevaluable** — a *favourable* result was **not adopted** |
| `prereg_spatial_significance_2026-08-07.md` | is the corrected estimator sound, per city? | **passed**; 6 of 9 cities significant |
| `prereg_activity_shocks_2026-08-07.md` | do the 2020 lockdown and 2021–22 fuel crisis constrain the local share? | 2 of 4 — the fuel crisis has the **opposite sign** to the assumption it was used to justify |
| `prereg_partition_identification_2026-08-07.md` | can the local/background split be estimated and validated? | **stopped at step 1** as registered |
| `prereg_partition_daily_2026-08-07.md` | does a coarser reference rescue it? | **failed again**; route abandoned |

The second and the last two are the ones worth reading. In one, a result that improved the
headline number was rejected because its validity gate could not be evaluated. In the others,
a plan was abandoned at a gate the author had set himself, and the abandonment is reported
rather than the threshold moved.

## `results/` — machine-readable artifacts behind the numbers

Validation, in the sense the project uses the word:

- `validation_scorecard.csv` — the ten analogue cities, scored against their withheld
  monitoring networks under Kandy's two-sensor information budget.
- `spatial_significance_test.{csv,json}` — per-city spatial rank with each city's **own**
  permutation null and a p-value, plus a second estimator agreeing to 0.002 (sign 9/9).
- `spatial_rho_bootstrap.csv` — station-resampled intervals on every rank.

The local/background split, which took eight attempts:

- `kandy_f_hierarchical.json` — hierarchical fit with Kandy held out of the fitting set.
- `kandy_activity_shocks.json` — natural experiments on the lockdown and the fuel crisis.
- `panel_reference_partition{,_daily}.csv` — the two reference designs that failed.
- `eps_floor_hierarchical.json` — a transferred constant shown **not** to transfer.

Uncertainty and known defects:

- `kandy_interval_coverage.json` — measured coverage of the shipped interval, decomposed
  into centring and width.
- `extension_tier_audit.json` — the audit that found the post-2023 tier could not produce
  episodes; every aggregate statistic had looked healthy.
- `extension_tail_correction.json` — the fix, validated by holding out each anchored year.
- `visibility_partial_correlation.json` — an independent check, retested after conditioning
  on the model's own drivers.
- `kandy_emission_clock_fit.json` — a literature prior refuted by a local natural experiment.

---

## How to read a claim

Every quantity in this model carries a status: **observed**, **learned**, or **imposed**. The
ledger tags each one and states the test that would falsify it. Where something is imposed
from physics rather than measured, it says so, and where a test could not be run the ledger
records *not estimable* rather than a null. The distinction between "we measured zero" and
"we could not measure" is maintained throughout.
