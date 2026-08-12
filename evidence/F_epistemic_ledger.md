# Appendix F — The Epistemic Ledger

> The model's conscience in one table. Every quantity that enters the reconstruction,
> with its **provenance** (🔵 OBSERVED / 🟢 LEARNED / 🟠 IMPOSED), its value, its
> uncertainty, and — the column that matters most — **the specific observation that
> would confirm or refute it.** This is what makes the model auditable: anyone can
> see, at a glance, exactly how much of the answer is earned versus assumed.
>
> Rule of reading: a result is only as trustworthy as the *weakest-provenance* link
> in its causal chain. The headline **level** and **temporal/seasonal behaviour**
> rest on 🔵/🟢 links; the **fine-scale spatial magnitude** rests on 🟠 links — which
> is the whole reason for the honesty framing.
>
> *(Seeded in Batch 1 from Part IV; finalised in Batch 4 once Parts III/V add the
> data-source and physics quantities.)*

---

## F.1 Headline reconstruction

| Quantity | Symbol | Value (2019–2023) | Prov. | Uncertainty | Confirm / refute (falsifier) | §|
|---|---|---|---|---|---|---|
| Basin annual mean | $\langle\mathrm{PM}\rangle$ | 19.7 / 19.0 / 17.0 / 18.7 / 20.9 | 🔵 | ±~3 (two-product spread) | independent area product disagreeing >15 % | IV.7 |
| Basin-mean = anchor | — | Δ = 0.000 | derived | exact (theorem) | non-zero G1 ⇒ normalisation bug | IV.1.2 |
| Fine-scale core/edge magnitude | — | ~1.2× annual / ~1.4× night | 🟠 | **unquantified** | floor-to-ridge concurrent sensors | IV.5, IX |

---

## F.2 Temporal anchor $T(t)$

| Quantity | Symbol | Value | Prov. | Uncertainty | Falsifier | §|
|---|---|---|---|---|---|---|
| Residual target | $y$ | $\mathrm{pm25}-c_\text{prior,anch}$ | 🟢 | — | — | IV.2.1 |
| GEOS-CF ratio | $\rho$ | 0.5360 | 🔵 | from KOALA/GEOS means | re-derivation from new ground mean | IV.2.1 |
| Per-sensor offsets | $b_\text{FECT}$ | −9.105 (Ak), −13.749 (Han) | 🔵 | per-sensor fit | recalibration vs reference monitor | IV.2.1 |
| Pooled skill | R² | 0.583 | 🟢 | LOMO | more sensors lifting/lowering it | IV.2.3 |
| Coverage | cov90 | 0.865 | 🟢 | ∈[0.85,0.95] | held-out coverage outside envelope | IV.2.3 |
| Diurnal corr (post-sharpen) | r | ≈1.0 (vs FECT) | 🟢/🔵 | — | new sensor with a different diurnal shape | IV.2.5 |

---

## F.3 Background $B(t)$ and the split

| Quantity | Symbol | Value | Prov. | Uncertainty | Falsifier | §|
|---|---|---|---|---|---|---|
| Seasonal shape | $s_\text{GEOS}$ | GEOS-CF daily, mean 1 | 🔵 | GHAP r≈0.91 | independent product breaking Mar-peak/Aug-trough | IV.3.2 |
| Local fraction | $f$ | {.28,.25,.21,.20,.27}, ~0.24 mean | 🟠 | bracket [15 %, <50 %] | local PMF / paired urban–rural sensors | IV.3.3 |
| Background level | $B_\text{annual}$ | $(1-f)\cdot$VanD ; 2019 ≈14.8 | 🟠/🔵 | bracket [10.5, rural P25] | rural sensor measuring the floor directly | IV.3.3 |
| Background bracket | $B_\text{lo},B_\text{hi}$ | 10.5 ; rural P25 | 🔵/🔵 | hard floor = ridge obs | — | IV.3.3 |

---

## F.4 Spatial pattern $P_\text{local}=S\cdot M\cdot A$

| Quantity | Symbol | Value | Prov. | Uncertainty | Falsifier | §|
|---|---|---|---|---|---|---|
| Satellite surface | $S_\text{emit}$ | mean 1, ±10 % | 🔵 | weak contrast | finer surface product | IV.4.1 |
| Traffic source | $S_\text{traffic}$ | core ≈3.3× mean | 🟠 | **magnitude prior** | measured traffic counts / flow | IV.4.2 |
| Vehicular share | $\nu$ | 0.90 | 🟠 | tunable | local emission inventory | IV.4.3 |
| Emission clock | $e(t)$ | bimodal, mean 1 | 🟠 | EDGAR profile | local traffic-count diurnal | IV.4.3 |
| Confinement coeff | $\kappa$ | 0.15 | 🟠 | **uncalibrated** | floor-vs-ridge hourly contrast | IV.5 |
| Ridge height | $H_\text{ridge}$ | 300 m | 🟠 | **uncalibrated** | observed trapping-height threshold | IV.5 |
| Enclosure field | $c(x,y)$ | zscore$(-\Delta z)$, mean 0 | 🔵→🟠 | DEM-exact geometry | — (geometry is observed) | IV.5 |
| Wind field | $\mathbf u$ | WindNinja library | 🟠 | shape r=0.49 cross-city | basin wind-profiler/sonic | IV.6.1 |
| Transport amplitude | $a(t)$ | clip(…,0,0.5) | 🟠 | **amplitude prior** | drainage-sink test at Katugastota | IV.6 |
| Diffusivity / deposition | $K, v_d$ | solver constants | 🟠 | literature range | tracer/flux measurement | IV.6 |

---

## F.5 Level anchor and health

| Quantity | Symbol | Value | Prov. | Uncertainty | Falsifier | §|
|---|---|---|---|---|---|---|
| Level | $L=$VanD area | per-year, β≡1 | 🔵 | two-product triangulated | new area product | IV.7 |
| KOALA reference | — | ~24.5 (2019 floor/core; derived from monthlies, not printed in the source) | 🔵 | single site/year; 4 s.f. unsupported | re-measurement 2020–23 | IV.7 |
| GEMM params | $\theta,\alpha,\mu,\nu,C_0$ | 0.143, 1.6, 15.5, 36.8, 2.4 | 🟠 lit. | Burnett 2018 CIs | updated CRF | IV.8.2 |
| SL baseline | CDR, $f_\text{NCD+LRI}$ | 6.6/1000, 0.85 | 🔵 lit. | WB/WHO | age-stratified local rates | IV.8.2 |
| Population | pop | WorldPop, 422 314 | 🔵 | model-pop uncertainty | census | IV.8.1 |
| Attributable burden | — | ≈423/yr [231–616] | derived | from PM + CRF | local epidemiology | IV.8.2 |
| Dynamic exposure | $E_\text{dyn}$ | ≈24 (core ≈ KOALA) | derived | +7 % over area | personal-monitoring study | IV.8.1 |

---

## F.6 The one honest sentence

> **Everything about *when* and *how much* (the level, the diurnal/seasonal cycle, the year-to-year change) rests on observed or learned quantities and is corroborated by independent data. Everything about the fine-scale *where* (the within-basin floor-to-ridge magnitude) is imposed from physics and literature priors, because no public network samples that gradient. The model is honest exactly to the degree that this table is kept current.**

---

## F.7 Data-source provenance (retrieval-level)

| Source | Prov. | Retrieval uncertainty | Role | §|
|---|---|---|---|---|
| VanD V6 | 🔵 | AOD→PM₂.₅ conversion; sparse-monitor S-Asia | level + $S_\text{emit}$ | III.A.1 |
| GHAP | 🔵 | ML ensemble; quasi-independent | corroboration only | III.A.2 |
| GEOS-CF | 🔵m | tropical over-prediction (ρ<1) | prior + B shape | III.B.1 |
| ERA5 | 🔵m | 25 km; BLH over terrain uncertain | met backbone | III.C.1 |
| MAIAC | 🔵 | 84.5 % cloud-gapped | feature | III.D.1 |
| TROPOMI NO₂ | 🔵 | coarse; placement not magnitude | cross-check | III.D.2 |
| SRTM | 🔵 | near-exact at this scale | confinement + winds | III.E.1 |
| OSM | 🔵/🟠 | geometry obs; volumes inferred | $S_\text{traffic}$ | III.E.2 |
| KOALA/FECT | 🔵 | LCS over-read (calibrated); 2 floor points + 1 site-yr | $T$ labels + anchor | III.F |
| WindNinja | 🟠 | diagnostic; amplitude prior | winds | III.G.1 |
| COPERT/EDGAR | 🟠 | European/global factors at Kandy | $S_\text{traffic}$ mag., $e(t)$ | III.H.1 |

## F.8 Status

This ledger is **complete** for v1.0 of the model. It is the single artifact to keep current: any new Kandy measurement that calibrates an 🟠 ASSUMED quantity moves its row to 🟢/🔵, narrows its uncertainty, and resolves its falsifier — at which point the corresponding claims in Part IX move from CORROBORATED/ASSUMED toward PROVEN. The model's honesty is, operationally, the upkeep of this table.

---

## F.9 Addendum — falsifiers *tested* by the post-v1.0 transfer-validation arc (2026-06-13)

The v1.0 rows above are unchanged (they describe the released model). This addendum records where
the **transfer-validation / GeoAQ-Zero arc (Part XI)** has now *tested* a falsifier listed above —
**by cross-city transfer (LOCO), not by a Kandy measurement.** No production value changed; these
are status moves on the conscience, with the regime-gap caveat (panel cities are local-dominated;
Kandy is regional-dominated — see XI.1) attached to every row. Evidence on OSF `6puk9`.

| Quantity (row) | v1.0 falsifier | What the arc did | Status move |
|---|---|---|---|
| $T(t)$ skill (F.2) | "more sensors lifting/lowering it" + (implicit) can it work *sensorless*? | anchor-free $T(t)$, LOCO over 196 cities | **🟢 strengthened** — 97 % beat zero-GT baseline, seasonal r 0.95; Kandy sensorless level +4 % vs FECT. *Sensorless temporal anchor validated.* (XI.3 T-a, XI.4) |
| cov90 / conformal (F.2) | "held-out coverage outside envelope" | cross-city (shift-aware) conformal, LOCO | **🟢 strengthened** — cov90 0.91, Kandy-regime 92 % in-band; transfer-failure (0.769) fixed. (XI.3 U) |
| Local fraction $f$ (F.3) | "local PMF / paired urban–rural sensors" | SBI from satellite-only summaries (grid-ABC) | **🟠→🟠/🟢** — Kandy **posterior 0.18 [0.10,0.27]**; imposed year values sit at or above the posterior centre and **2019's 0.28 is just outside the upper bound**; data mildly prefer lower. SBC-calibrated. *Inferred, not just asserted; bracket unchanged in production pending promotion.* (XI.3 I) |
| Background $B(t)$ seasonal shape (F.3) | "independent product breaking Mar-peak/Aug-trough" | W2 trajectory verdict + B(t) v2 candidate | **context added** — transboundary share quantified as **seasonal** (JJA/DJF obs 0.39); v1.0 shape shown too flat (B>total in JJA); origin-conditioned B(t) v2 candidate fixes it (0.82→0.50), **not promoted**. (XI.2) |
| Confinement $\kappa$ (F.4) | "floor-vs-ridge hourly contrast" | panel ablation (F0.3) + SBI (I-3) | **🟠 confirmed UNIDENTIFIABLE from public data** — κ=0 beat κ=0.15 at 3/3 floor-sited panel cities; SBI κ posterior simulator-dependent/conflicting. Falsifier still requires a **Kandy vertical transect**; horizontal support is weak, vertical support unmeasurable. (XI.3 I, XI.3 Phase-0) |
| Fine-scale spatial magnitude / $P_\text{local}$ (F.1, F.4) | "floor-to-ridge concurrent sensors" | PatternNet (learned within-city pattern), LOCO 199 cities | **🟠 reinforced** — within-city pattern **not learnable** from public covariates (ρ 0.14, amplitude SD-ratio 0.34). The physics-imposed choice is *vindicated*; amplitude remains the open problem only sensors close. (XI.3 S) |
| $S_\text{emit}$ circularity (F.7 VanD) | (new, surfaced by the arc) | F0.1 audit: VanD V6 is monitor-fused (Shen 2024) | **caveat added** — partial circularity at monitored cities; **station-blind S_emit still clears the spatial gate** → zero-GT spatial-rank claim survives, bounded. (XI.3 Phase-0) |

**Net:** the *temporal* axis (the "when/how much") moved from corroborated to **transfer-validated
sensorless**; the *spatial* axis (the "where") is **unchanged in production** and its imposed status
is now *vindicated* (learning does not beat it) rather than merely assumed; $\kappa$ and the vertical
gradient remain the **permanent public-data fence**. The one-honest-sentence (F.6) still holds —
this arc tightened both halves of it without moving any production number.

---

## F.10 Addendum — the increment split (2026-07-09, production form change)

The one post-v1.0 change to the **assembly equation itself** (IV.1 → IV.1b): the additive form
inverted the spatial pattern whenever the hourly total dipped below the daily background
($T<B$, 38.5 % of Kandy hours — deep midday mixing), rendering the core *cleaner* than the rural
edge. Production now splits the increment by sign — $\mathrm{PM}=B+\max(T-B,0)\,P+\min(T-B,0)$ —
so the local pattern structures only accumulation; ventilation is spatially uniform.

| Property | Status | Evidence |
|---|---|---|
| T-lock under split | exact, both branches | theorem + G1 Δ = 0.000; `test_split_form_preserves_tlock` |
| Inversion removal | 38.2 % → 0.0 % midday core<periphery | webapp v2 audit; `test_split_form_removes_core_periphery_inversion` |
| Accumulation hours | **bit-identical to IV.1** | $\max/\min$ reduce to the plain form when $T\ge B$ |
| Provenance | 🟠 IMPOSED (physical argument: mixing dilutes the basin together) | falsifier: concurrent core+edge sensors on a ventilated midday hour showing a *preserved* spatial gradient |
| Alternatives tested | diurnally-shaped $B$ **rejected** (relocates inversion, 37.6 %) | webapp_v2 plan doc |
| Propagation | Kandy builder · multi-city `xichang_prod` · webapp export/reconstruction · release repo `kandymodel` | commits 75c2349, c642d30, c28d785 |

No headline number moved (T-lock exact; 2023 burden 425 unchanged); the change is in *where*
the ventilated-hour field puts its (now flat) spatial structure.

## F.11 Addendum — the ventilated-hour pattern floor (additive_v3, 2026-07-21)

The split (F.10) fixed the inversion but rendered ventilated hours **perfectly flat** — and
ground truth says that overcorrects. On the Medellín network the 220 hours where the model's
increment is ≤ 0.5 µg m⁻³ keep station spread σ ≈ 5.7 µg m⁻³ (relative 0.68 > 0.42 for structured
hours): near-source plumes persist through ventilation. Production adds a **bounded, mean-zero
pattern floor** $\varepsilon(t)(P-1)$, $\varepsilon(t)=\max(0,\varepsilon_0-\max(T-B,0))$ (IV.1c),
active only where the accumulation amplitude is below $\varepsilon_0$.

| Property | Status | Evidence |
|---|---|---|
| T-lock under the floor | exact ($(P-1)$ is mean-zero) | Δ = 0.000000 all years; webapp QA reconstruction 0.0012 µg m⁻³ |
| No re-inverted core | 0.0 % core<periphery | $\varepsilon_0\ge0$, accumulation-side $P$ mutes toward flat, never flips |
| Structured hours | **bit-identical to IV.1b** | floor inactive when $T-B\ge\varepsilon_0$ |
| Paper figures | unchanged | annual-mean spatial field 99.99 % corr v2↔v3 (floor averages out) |
| $\varepsilon_0$ (Kandy) | 🟠 METHOD-TRANSFER: 2.573 µg m⁻³ = 0.398 × mean accum. amplitude 6.465 | Medellín fit (slope 5.65, holdout-6 flat-hour RMSE 8.53→7.99) + cross-city no-degrade (KTM, ChiMai); relative form transferred (no Kandy network) |
| Distinct from rejected A2 | additive mean-zero ≠ multiplicative $1+a(P-1)$ | A2 inflated the *level* (monitors on high-$P$ side), cross-city 0/4 — the floor touches neither level nor structured hours |
| Provenance | 🟠 IMPOSED at Kandy (validated at Medellín, ported) | **falsifier: a Kandy mobile/transect campaign measuring real spatial spread on ventilated hours** |
| Propagation | fit+gate `flat_hour_residual_fit.py` · build `build_additive_field_v3.py` · webapp export/`store.js` · canonical `assemble_year()` param `EPS_FLOOR` (release + framework) · reference IV.1.3c | — |

Measured Kandy effect: flat-field hours 56.6 %→45.3 %, median spread 0.60→1.25, **annual means and
pop-weighted exposure unchanged** (+0.2 %). Like F.10, no headline number moved; the change is the
muted spatial texture the model now shows on ventilated hours instead of a featureless field.

## F.12 Addendum — the forecast tier (demonstration, 2026-07-27)

A **display tier, not a change to the model.** The frozen area-anchored anchor GBM is driven by
NASA GEOS-CF *forecast* fields instead of reanalysis, producing a +120 h basin-mean level that the
public explorer offers as selectable future hours. The locked 2019–2023 headline and the
2024–2026 extension tier are untouched.

| Property | Status | Evidence |
|---|---|---|
| Driver substitution costs little | **validated, off-target** | F-M2 at Medellín, clean split (train ≤2022, score 2023) vs 15 withheld stations: RMSE **5.71** vs 24 h persistence **6.49**, skill **+0.120**; seasonal r 0.974, diurnal r 0.965 |
| Anchor is satellite-independent | validated | F-K1: retraining without the 5 forecast-absent satellite features costs Δ −0.004 residual R² |
| Skill at **Kandy** | **not estimable** | no public in-basin station; nothing to score against. Displayed as a demonstration with borrowed evidence, never as a checked product |
| Interval calibration | **imposed, measured off the daily anchor** | sensorless anchor's nominal 90 % PI covers **70.7 %** (n=1215 d); k = **1.35** restores 90.0 % (direct search and split-conformal agree to 0.000); applied to the hourly forecast PI as a disclosed transfer |
| Forecast spatial pattern | **does not exist** | only the level is forecast; the map uses the (month, local-hour) `P_local` climatology of the most recent reconstructed year, banner-labelled |
| Background for forecast hours | inherited | $B = T\cdot(B/T)_{\text{month}}$ from the locked 2019–2023 chain — the extension-tier rule; a flat $B$ would flatten the monsoon field (gotcha #61) |
| Propagation | derivation `kandy_forecast_ood_widening.py` · constants `kandy_forecast_pack_update.py` · runner `kandy_webapp/live/kandy_live.py` · client `store.initForecast` · reference F.12 | — |

**Numbers discipline.** An earlier F-M2 run reported skill **+0.223** / RMSE 5.04 and a 12–36 h lead
sweep of +0.22…+0.44. That run trained on hours inside its own evaluation year while the persistence
baseline received no look-ahead; the clean split roughly halves the headline. Those figures must not
be displayed or quoted. Separately, under the clean split the forecast-driven anchor edges the
*analysis*-driven one (5.71 vs 5.96); this is **amplitude calibration, not forecast skill** —
correlation is identical (0.590 vs 0.592) and the analysis anchor's extra hour-to-hour variance is
unskillful at unchanged correlation. It is never to be described as beating reanalysis.

### F.12b — closing the record→forecast seam (2026-07-27)

The forecast tier exposed a structural discontinuity that had always existed and was
simply never visible: the reconstructed record can only reach about **now − 5 days**
(ERA5-Land latency), while the forecast begins at the newest model run, leaving a band
that **no dataset can fill retrospectively**. GEOS-CF serves analysis for a rolling
**25 h window only** (dated CFAPI requests are rejected) and its OPeNDAP replay archive
lags by months (verified 2026-07-27: coverage ends 2026-01-02).

Resolution — three tiers past the end of the anchored record, each labelled separately
rather than merged:

| Tier | Drivers | Lead | Completeness |
|---|---|---|---|
| extension (record) | ERA5-Land, rebuilt on demand | past | full field + met |
| **recent (nowcast)** | GEOS-CF **analysis**, 25 h rolling window logged hourly | 0 | full field + met |
| forecast | GEOS-CF forecast | +1…+120 h | full field + met |
| **level only** | forecast issued earlier, met not retained | past | field only — wind and weather **withheld** |

The nowcast step is the permanent fix: logged every hour, the rolling analysis window
accumulates into continuous coverage and the seam cannot re-form. `level_only` exists
only for the one-off band that predates it; those hours reconstruct a field (which needs
$T$, $B$ and $P$, not meteorology) but the wind layer and weather panel are hidden rather
than back-filled from a different met product.

Two defects were found closing this and are worth stating because both are recurrences:
**(1)** rebuilding `additive_v2` without rebuilding `additive_v3` left the exporter reading
a stale field against fresh anchors — the QA gate caught it at 5.61 µg m⁻³ (tol 0.25), the
same anchor-desync family as gotcha #65, and the fix is to rebuild the tier the exporter
actually reads. **(2)** payload JSON/gzip requests carried **no cache-busting**, so a
returning visitor kept the previous export while running the new code; data URLs are now
stamped with the module version read from `import.meta.url`.

## F.13 — the daily-B seam, quantified; and a seasonal re-level tried and REJECTED (2026-07-27)

Triggered by a user report that the webapp shows no emission structure "since April".
It does not, and the cause is not the extension tier or the forecast: it is the seam
between an **hourly** T(t) and a **daily-resolution** B(t), present in every year of
the record since 2019.

**Measured over all 66,193 shipped hours (2019-2026):**

| Quantity | Value |
|---|---|
| hours with $B>T$ (background exceeds the total) | **28.5%** |
| by month | ~2-13% Jan-Mar, **27-48% from April**, high through November |
| hours below the SBI posterior's own bound $f\ge0.10$ | 35.1% |
| monthly-mean $B/T$, locked years | Jan-Mar 0.53-0.63 · **Apr 0.89 · May 0.97 · Sep 1.11 · Oct 1.01 · Nov 0.96** |
| displayed local share | **negative** in Sep/Oct/Nov of most years (Sep 2022: −0.49) |
| median map spread | 5.7 µg m⁻³ (Mar) → **0.6-0.9 (May-Sep)** |

In May, September, October and November the **monthly mean** background exceeds 90% of
the monthly mean total, so this is not an hourly sampling artefact — the seasonal
partition itself is incoherent. Under the increment split every such hour renders
spatially uniform by construction, which is exactly the reported symptom. Independent
corroboration that the wet-season background runs high: W2 (D2) puts the observed JJA
level near the pristine marine floor at ~7.4 µg m⁻³ while the model's JJA **background
alone** is 8.50.

**The re-level (`scripts/kandy_background_relevel.py`) — built, gated, rejected.**
Bound monthly $B/T\le0.89$ and hourly $B\le0.9\,T$, redistributing multiplicatively so
each year's mean of $B$ is preserved exactly (hence the disclosed $f$ untouched).

| Property | Result |
|---|---|
| annual mean of B | preserved to 7e-15 µg m⁻³ |
| $B>T$ | 28.5% → **0.13%** (residual = hours where raw T itself is <0) |
| negative local shares | eliminated |
| W2 JJA/DJF background ratio | 0.544 → 0.490 (observed 0.53) — passes a 0.03 gate |
| **dry-season structure** | **2022 Mar local share 0.287 → 0.112; map spread 3.92 → 2.61** |
| **wet-season structure** | **little gained; 2023 May spread 1.11 → 0.62** |

**Rejected on that last pair.** Annual mass conservation means every month *below* the
ceiling is scaled UP to absorb what the capped months give back, and those months
outnumber the capped ones — so the season that currently renders well pays for the one
that does not, and the net effect is *less* spatial structure. A first redistribution
variant (proportional to headroom rather than multiplicative) was rejected earlier by
the W2 gate, which caught it driving the transboundary ratio to 0.447.

The three constraints — a coherent monthly partition, the disclosed annual $f\approx0.24$,
and the W2 seasonal background shape — **cannot all hold with a daily background**. That
is the case for Consolidation v3 (an hourly semi-mechanistic B), and this is now the
quantified argument for it rather than a stylistic preference. Code retained with
`RELEVEL = False` in `build_additive_field_v2.py`.

**Process note.** The first application was written as a separate post-processing step
and was silently discarded, because `build_additive_field_v2.py` regenerates B from
scratch. A fix to a derived artefact must live inside the code that derives it.

## F.14 — B(t) checked against instruments for the first time (NBRO network, 2026-08-01)

The regional background carries ~three quarters of Kandy's PM2.5 and had never been compared
with a measurement: everything constraining it was internal (a rural satellite floor, an
origin-conditioned seasonal shape) or indirect (W2 trajectories). The hourly `NBRO_AQ_snapshot`
task has since 2026-05-08 been logging **25 Sri Lankan stations in raw µg m⁻³**, giving a
~10-week overlap with the modelled record.

Method (`scripts/kandy_background_nbro_check.py`): exclude anything within 20 km of Kandy
(one station, "Kandy", dropped — it cannot be allowed to leak into a check of the background);
require ≥6 stations per hour; compare at **daily** resolution because B(t) is a daily product;
score B against the network's low percentiles, since B was *constructed* as a rural floor and
every individual station carries its own local increment.

| Target | Level (µg m⁻³) | r (daily) | Spearman | model − obs | ratio |
|---|---|---|---|---|---|
| network floor P10 | 5.35 | +0.293 | +0.236 | +3.38 | 1.63 |
| network P25 | 7.78 | +0.366 | +0.301 | +0.95 | 1.12 |
| network median | 11.49 | +0.367 | +0.371 | −2.76 | 0.76 |
| network mean | 14.18 | +0.270 | +0.349 | −5.45 | 0.62 |

n = 44 days (2026-05-10 → 07-21), median 13 stations/hour; modelled B = **8.73**.

| Property | Status | Evidence |
|---|---|---|
| Background **level** plausible | **corroborated** | B sits between the network's P10 and median, ratio 1.12 to P25 — where a regional floor belongs |
| Physical ordering | holds | floor < median < mean, as construction requires |
| Background **day-to-day variability** | **weakly verified** | r ≈ 0.37 daily (p ≈ 0.014 at n=44) — it tracks the regional air mass, but loosely. First quantification |
| Wet-season level | **runs HIGH** | applying a x1.35 low-cost-sensor correction puts the true regional floor near **5.76**, making B **1.51x** it |

**The wet-season result is the important one, and it is a THIRD independent line** on the
same conclusion, from an instrument rather than from the model's own internals:
(1) internal coherence — B > T in 28.5% of hours, monthly B/T to 1.14 (F.13);
(2) W2 D2 — model JJA background 8.50 vs observed ~7.4;
(3) **this** — B is ~1.5x the calibrated island floor over 44 wet-season days.

This changes the standing of the rejected re-level (F.13). That fix was rejected because
annual mass conservation forced the dry season to pay; but the constraint being conserved —
the annual f — now has external evidence against it in the wet season specifically. A
**non**-mass-conserving reduction of the wet-season background may simply be correct, with f
rising accordingly. It is the anchor Consolidation v3 should be built against, rather than
the model's own prior.

**Cannot establish:** no station is in-basin, so nothing here validates the Kandy field or
the local increment; the x1.35 correction is a literature assumption, not a measurement; all
44 days are wet-season, so DJF — when the transboundary background matters most — is
untested; an island floor proxies Kandy's inflow rather than measuring it.

## F.15 — Consolidation v3 built in two forms, both REFUTED; the seam is a LEVEL problem (2026-08-01)

F.13 quantified the daily-B seam and rejected a bounded re-level. F.15 attacks the same
defect architecturally, as the roadmap intended — an **hourly semi-mechanistic background**
(`scripts/kandy_background_v3.py`). Both formulations fail, and the failures localise the
problem precisely.

**Form 1 — rebuild B from local physics.** $B=L_{\text{class}}\cdot D\cdot W$ with dilution
$D=(H_{ref}/H)^{\alpha}$ and wet removal $W=e^{-\kappa R}$, $\alpha,\kappa,\tau$ fitted to
the NBRO regional floor.

| Diagnostic | Result |
|---|---|
| fitted $\alpha$ | **0.80 — bound-saturated** (cf. SharedTerrainAnsatz, all 6 params bound-hit) |
| coherence | B > T 28.5% → **21.8%**, still FAIL |
| W2 JJA/DJF | **0.427** vs observed 0.53, FAIL |
| agreement with NBRO floor | **r = −0.07**, against **+0.37 for the v2 daily background it replaced** |

The last row is a genuine finding: **the regional background's day-to-day variation is set by
what is advected in — chemistry and transport, which the GEOS-CF daily shape carries — not by
local dilution and washout.** That is what a background *should* do; it is determined upwind.
Rebuilding it from local meteorology discards real information.

**Form 2 — add only the missing diurnal physics.** $B_{v3}=B_{v2}\cdot D/\overline{D}_{\text{day}}$,
normalised within each calendar day so every daily mean is preserved exactly — hence $f$, the
W2 ratio and every seasonal quantity are invariant *by construction*, and only the diurnal
distribution changes.

| $\alpha$ | 0.0 | 0.2 | 0.4 | 0.6 | 0.8 | 1.0 |
|---|---|---|---|---|---|---|
| B > T | 28.6% | 28.1% | 27.8% | 28.0% | 28.5% | **29.1%** |
| background diurnal swing (µg m⁻³) | 3.65 | 9.27 | 14.73 | 19.70 | 24.18 | **28.19** |

**Coherence is flat in $\alpha$ and worse at the top end**, even at a physically absurd 28 µg m⁻³
background swing. B and T already share their diurnal driver, so adding a BLH response to B moves
it up at night and down at midday exactly as T does — $B/T$ barely changes — and at large $\alpha$
the background's night peak overshoots T, creating new incoherent hours to replace the fixed ones.

**Conclusion — the seam is a LEVEL problem, not a phase problem.** Three independent attempts:

1. mass-conserving seasonal re-level → fixes coherence, costs dry-season structure (F.13)
2. background rebuilt from local physics → external agreement collapses, two gates fail
3. diurnal dilution added to v2 → coherence unchanged at every $\alpha$

The only remaining lever is the **low-season level of B**, and lowering it necessarily raises $f$
above its disclosed band. F.14 says that lowering is probably right *in the wet season* (B is
1.51× the LCS-corrected island floor). But annual conservation makes the dry-season background
rise to compensate, and **no external measurement covers DJF yet** — the NBRO log began
2026-05-08, so its overlap is wet-season only. W2 makes a *higher* DJF background plausible (DJF
is 82% Bay-of-Bengal Indian outflow, IGP-origin FECT 27 µg m⁻³), so the compensating rise may
itself be correct.

**This is now blocked on a measurement rather than on a method, and the measurement is dated:**
the NBRO network accumulates DJF coverage from December 2026, at which point re-running
`kandy_background_nbro_check.py` decides between (a) lower wet-season B and accept f ≈ 0.30, and
(b) the F.13 re-level, whose dry-season cost may be a correction rather than damage. Until then
the shipped v2 background stands, with the defect disclosed.

## F.16 — A2: the anomaly target does NOT retire the sharpening patch, and A4 closes on evidence (2026-08-01)

The sharpening patches (`sharpen_T_diurnal`, `sharpen_to_locked`) exist because the lag-free
GBM regresses to the mean and damps the diurnal swing. A2's premise was that predicting the
**departure from a climatology** would put the amplitude in the climatology and retire the
patch at its cause — and, if the climatology could be made sensorless, would also shrink the
A4 disclosure gap. Both halves were tested on a clean temporal split (train ≤ 2022, score on
2023 hours never seen; gotcha #68), `scripts/kandy_anomaly_target_test.py`.

| variant | RMSE | diurnal r | **swing ratio** | seasonal r | level bias |
|---|---|---|---|---|---|
| a. direct GBM, no sharpening | 12.588 | 0.882 | **0.579** | 0.408 | +4.97% |
| b. direct + post-hoc sharpen (production) | 12.741 | 0.895 | **0.787** | 0.390 | +4.97% |
| c. **anomaly target**, FECT climatology | **12.373** | **0.902** | 0.696 | **0.420** | **+1.79%** |
| d. anomaly target, **sensorless** climatology | 12.847 | 0.874 | 0.609 | 0.376 | +6.45% |
| e. anomaly + post-hoc sharpen | 12.455 | 0.895 | 0.763 | 0.390 | +1.79% |

**Row (a) confirms the defect out-of-sample: the raw anchor reproduces only 58% of the observed
diurnal amplitude.** The patch is not cosmetic.

**The premise is refuted.** The anomaly target lifts the amplitude only to 0.696, short of the
post-hoc patch's 0.787, and combining both (e) still does not beat (b) on amplitude. Predicting
anomalies does *not* retire the patch family; the patch remains the best amplitude repair.

**Its apparent accuracy win does not survive production.** (c) improves level bias 4.97% → 1.79%
and RMSE 12.74 → 12.37, but production **re-anchors T(t) to the VanD area mean every year**, which
absorbs annual level bias entirely. What survives the re-anchor is shape: seasonal r +0.03,
diurnal r +0.007, and swing ratio **−0.09 (worse)** — i.e. marginal, and negative on the very axis
the patch exists for. **Not adopted; the locked anchor is unchanged.**

**A4 now closes on evidence rather than wording.** Row (d) replaces the FECT climatology with a
genuinely sensorless one — the cross-city panel-donor solar-time diurnal shape × a chemistry-prior
seasonal shape — and it is worse on *every* metric (swing 0.609, diurnal r 0.874, level bias
+6.45%, worst RMSE). So the shipped diurnal/seasonal shape's dependence on the two local sensors
is **real and necessary, not a presentational choice**. The preprint's §2 disclosure stands as
written, and can now cite a measurement: a sensorless shape was constructed and performs
measurably worse.

Note for interpretation: out-of-sample the production-style patch itself recovers only 0.787 of
the amplitude, because it maps onto the *training* climatology. In production it is fitted on the
full record, so the in-sample appearance is near-perfect — another instance of gotcha #68's family,
and a reason the shipped swing should not be quoted as validated skill.

## F.17 — the decomposition is OVER-DETERMINED: f, coherence and an independent background cannot all hold (2026-08-02)

Commissioned to (a) establish the background/local split from evidence rather than prior and
(b) build a true hourly background. Both were done. The result is structural, and it is more
important than either deliverable.

### The defect is year-round, not April
`scripts/kandy_f_reconciliation.py` introduces a bound nobody had computed: a background that
is flat within a day cannot exceed that day's MINIMUM total, so the shipped `T(t)` alone puts a
**hard floor** under f, with no external input at all.

| month | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| f shipped | .442 | .469 | .368 | .110 | .034 | .222 | .206 | .174 | **−.115** | −.013 | .043 | .369 |
| f floor | .375 | .349 | .321 | .362 | .406 | .395 | .440 | .455 | .446 | .460 | .473 | .434 |

**The shipped split is below its own coherence floor in 9 of 12 months — April through
December** — and annually **0.244 against a floor of 0.410**. April is merely where it becomes
visible. The seasonality is also inverted: the wet season needs the LARGEST local share (clean
marine inflow, so what is present is mostly local) and the model gives it the smallest. The
NBRO instrument agrees from outside — wet-season f = **0.446**.

### The over-determination
`scripts/kandy_background_v4.py` rebuilt B hourly with the level set by the NBRO instrument
(marine floor 5.76, measured), the day-to-day shape kept from GEOS-CF (the only term with
external support, r = +0.37), and a genuine diurnal dilution response. Sweeping the two free
parameters shows three constraints that cannot be jointly satisfied:

| choose | outcome |
|---|---|
| independent background dynamics + f ≈ 0.25 | **B > T in 28.5% of hours** — the shipped v2 defect |
| independent background dynamics + coherence | **f = 0.65–0.71**, outside the literature bracket [0.15, 0.50) |
| coherence + f ≈ 0.25 | B must track T day-to-day, i.e. B ≈ (1−f)·T — a background with no independent dynamics, making the split definitional rather than physical |

Solving instead against the W2 JJA/DJF ratio (0.53) forces the continental level to 19.45,
giving f = 0.182 and coherence 32.9% — worse than what it replaces. **W2's 0.53 is the outlier
among the three lines**, and it is the softest: it is a background ratio *inferred* from FECT
totals by air-mass origin, and that inference itself assumes a local share, so a larger true f
biases it.

### Two residuals worth recording
* **~1.8% of hours have T(t) below the measured regional floor of 5.76** — no background level
  can make those coherent. Either the wet-season T runs low, or the island P25 overstates
  Kandy's inflow (plausible: 24 stations including coastal towns, while Kandy is inland and
  elevated). **This is the most likely single point of failure and the cheapest thing to test
  next** — an in-basin or upwind rural station would settle it.
* Normalising the dilution term within each day, which an earlier version did to protect the
  daily series, makes the term inert: a daily-neutral factor cannot lower the midday background,
  which is the entire purpose. A real background's daily mean must be an OUTPUT.

### Status
No background was adopted. `kandy_background_v4.py` is retained as the assessment instrument.
The honest reading is that the additive decomposition, as currently posed, has one more
constraint than free function — and the resolution is a measurement (what is the actual regional
inflow over Kandy?), not a reparameterisation. Four rebuild attempts across F.13, F.15 and F.17
now agree on that.

## F.18 — the Lenschow envelope background: built, and rejected on the same gate as its predecessors (2026-08-03)

The last remaining reformulation. Rather than levelling the background independently and
hoping it stays under the total, estimate it the way the project's stated framework
(Lenschow 2001) actually prescribes: as the persistent LOWER ENVELOPE of the total.

    B(t) = L(month) . G(day) . D(hour),  L = a low quantile of hourly T within the month

Coherence then stops being a constraint to satisfy and becomes a property of the
construction. `scripts/kandy_background_v5.py`, swept over the envelope quantile and the
dilution exponent:

| envelope | f annual | B > T | JJA/DJF |
|---|---|---|---|
| P05 | 0.517 | 3.6% | 0.324 |
| **P10** | **0.438** | **7.4%** | **0.349** |
| P15 | 0.379 | 11.4% | 0.360 |
| P20 | 0.330 | 15.5% | 0.365 |
| P25 | 0.284 | 19.8% | 0.370 |

The P10 envelope is attractive on two axes: **f = 0.438 independently matches the NBRO
instrument (0.446) and clears the hard coherence floor (0.410)**, and coherence improves
roughly fourfold (28.5% → 7.4%).

**Rejected on the W2 gate.** It drives the JJA/DJF background ratio to **0.349** against an
observed **0.53** — a clear degradation of a validated transboundary result. The F.13
re-level was rejected for moving the same ratio to 0.447; applying a weaker standard here
because this attempt is more elaborate would be motivated reasoning. **Not adopted.**

### Why every reformulation fails the same way
Five attempts now (F.13, F.15 ×2, F.17, F.18). The pattern is consistent and is the finding:
a background with genuinely independent dynamics, pointwise coherence with the total, an f
inside the literature bracket, and the W2 seasonal shape are **four constraints on three
degrees of freedom**. Each attempt satisfies three and breaks the fourth, and which one
breaks depends only on which is left unconstrained.

The binding evidence gap is specific and cheap to close: **1.8% of hours have T(t) below the
measured regional floor of 5.76 µg/m³**, and the island P25 that supplies that floor pools 24
stations including coastal towns while Kandy is inland and elevated. **One in-basin or upwind
rural monitor would determine whether the wet-season total is too low or the regional floor
too high, and that single measurement collapses the over-determination.** No amount of
reformulation substitutes for it.

**Shipped model unchanged.** The visible consequence is handled at the display layer instead
(F.19): hours where the model cannot resolve a local increment now say so, rather than
rendering a flat field and a zero or negative local share with no explanation.

## F.19 — the split limitation is now stated where the viewer meets it (2026-08-03)

Display-layer consequence of F.13/F.15/F.17/F.18. On hours where the estimated background
is at or above the modelled total the increment is zero or negative, the field is spatially
uniform **by construction**, and the app previously printed "0%" local beside a flat map —
which reads as "there are no local emissions here". It is not that; it is that the split
cannot be made.

Those hours now say so, and link to a new method-page section that gives the frequency
(~28% of all hours, 2-13% Jan-Mar rising to 27-48% from April), the cause (a daily-resolution
background against an hourly total), what was attempted (five reformulations, each rejected
by a measurement), and what would actually resolve it (one in-basin or upwind monitor).

No model quantity changes. This is the only intervention in the whole arc that improves the
product without trading one validated result for another.

## F.20 — city-graph donor weighting: small, real, and bounded by extrapolation (2026-08-06)

`scripts/panel_city_graph_donor.py`. The donor diurnal shape is currently an UNWEIGHTED
MEAN over 199 CNEMC cities. This replaces it with a learned similarity kernel over city
descriptors — the GAGNN/HighAir construction, with cities as nodes, which is the only
graph formulation that applies at Kandy's sensor density (GraPhy loses to IDW below
~0.16 sensors/mi²; Kandy is 0.023).

| evaluation | unweighted mean | geographic kernel | learned kernel | gain |
|---|---|---|---|---|
| plain LOCO | 0.8216 | 0.8785 (100 km) | 0.8833 | +0.062 |
| **block CV > 500 km** | **0.8044** | 0.8245 (400 km) | **0.8359** | **+0.032** |
| block CV, **transferable descriptors only** | 0.8044 | — | **0.8213** | **+0.017** |

**Three findings, in order of importance.**

**(1) Plain LOCO is the wrong evaluation and overstates the gain by ~2×.** Every Chinese
panel city has close neighbours; Kandy has none. Spatial-block CV, which withholds all
donors within 500 km, is the evaluation that matches the use case, and it halves the gain.
Note that the learned kernel *overtakes* the geographic one under block CV — when nearby
donors are unavailable, descriptors are what is left.

**(2) The panel does not bracket the target.** The CNEMC panel spans 84.9–130.4 °E and
Kandy sits at 80.6 °E: **zero of 199 panel cities lie west of it.** Longitude is the
dominant fitted descriptor under block CV, so the +0.032 figure rests on extrapolating
the one feature that cannot transfer. Restricted to physically transferable descriptors
the honest gain is **+0.017**, and among those **relief dominates** (bandwidth 0.87 against
0.77 for magnitude and 0.00 for latitude) — terrain shapes the diurnal cycle through
boundary-layer confinement, which is physically the right answer.

**(3) A leak was caught and removed.** The first run included `peakiness`, derived from the
target city's *own* diurnal shape, and `log_stations`, a property of the monitoring
programme rather than the atmosphere. Neither is obtainable for an unmonitored target.
Removing them dropped plain LOCO from 0.860 to the values above. The admissibility rule is
now stated in the script: **a descriptor may be used only if it exists for a target with no
local observations.**

**Verdict: adopt as a method contribution for the panel work; it does not change Kandy.**
+0.017 on a donor shape that only enters the sensorless comparison is immaterial to the
shipped product, exactly as predicted before running. Its real value is the second finding,
which is an argument for the non-Chinese panel expansion.

## F.21 — a hierarchical estimate of f, and four independent lines converging (2026-08-06)

`scripts/kandy_f_hierarchical.py`. The project kept its hand-set `FRAC_LOCAL_YEAR` over the
SBI posterior on an INFORMAL argument: that the inference "runs low against the literature
bracket at every locally dominated panel city". With four cities that is estimable rather
than assertable.

The shortfall at the three locally dominated cities is not a constant offset (0.34, 0.50,
0.45) but a roughly stable RATIO (0.50, 0.34, 0.44). The distinction decides the answer:
an additive correction applied to Kandy gives f ≈ 0.61, outside every bracket, while a
multiplicative one lands near two independent estimates.

    f_c   ~ N(mu, tau)              population of cities, partial pooling
    SBI_c ~ N(rho . f_c, s_c)       the inference attenuates the true fraction
    lit_c ~ N(f_c, w_c)             literature bracket as a soft observation

Fitted on Xichang, Kathmandu and Medellín; **Kandy is held out of the fit**, so it never
informs the correction applied to it.

| quantity | result |
|---|---|
| SBI attenuation | **rho = 0.426 ± 0.066** — the inference recovers ~43% of the true fraction |
| **Kandy f** | **0.392, 90% CI [0.258, 0.525]** |
| shipped prior | 0.244 (0.20–0.28 by year) |
| raw SBI | 0.181 |

**Four independent routes now converge, and three of them were held out of this model:**

| line | value | used as input? |
|---|---|---|
| hierarchical estimate (this) | 0.392 [0.258, 0.525] | — |
| coherence floor, shipped anchor alone (F.17) | 0.410 | **no** — inside the CI |
| NBRO island network, wet season (F.14) | 0.446 | **no** — inside the CI |
| literature bracket | [0.15, 0.50] | soft |

**The shipped f = 0.244 is now positively refuted rather than merely "below a floor".** The
informal bias argument is confirmed and quantified: the SBI inference is attenuated by a
factor of about 0.43, which is why it looked low everywhere it could be checked.

**Caveats, and they are real.** Three fitting cities — this is the regime partial pooling
exists for, but the population parameters are weakly identified and the interval is
indicative. The literature bracket is an expert range treated as a normal likelihood, so its
tails are optimistic. `rho` is assumed common across cities; regime-varying attenuation is
not identifiable at n=3.

**What this does and does not change.** It does NOT resurrect any of the five rejected
background rebuilds: F.18 showed that a background built to deliver f ≈ 0.44 breaks the W2
seasonal ratio, and that remains true. What it changes is the STATUS of f — from a prior the
project distrusted to an estimate with an interval and four converging lines. The preprint
should carry this number, its interval, and the attenuation finding.

## F.22 — holiday natural experiments: a fifth, direct line on f, and the Sunday conflict resolves (2026-08-06)

`scripts/kandy_holiday_experiment.py`. A meteorology-controlled Sunday test had implied a
locally generated share of only 0.14-0.23, against four converging lines near 0.40 (F.21).
Sri Lanka supplies a better instrument: **Poya days**, monthly full-moon public holidays
that fall on a DIFFERENT WEEKDAY each month, so a holiday effect is identifiable while day
of week is held fixed — which the weekend test cannot do. Transboundary transport is
indifferent to Sri Lankan holidays, so any drop is local by construction.

Residuals are taken against (month × hour × ventilation-quintile) cell means; effects are
measured against ordinary working days. Poya dates are astronomical full moons in local
time (`ephem`); a gazette mismatch of one day dilutes rather than biases.

| instrument | n hours | effect | % of mean | p |
|---|---|---|---|---|
| Sunday | 2,517 | −1.077 | **−7.8%** | 4.2e-08 |
| **Poya (lunar public holiday)** | 603 | −1.626 | **−11.7%** | 1.7e-05 |
| Poya, *within* day-of-week | 558 | −1.422 | −10.3% | — |
| other fixed public holidays | 198 | −2.167 | **−15.6%** | 1.5e-03 |
| Sinhala/Tamil New Year (13–14 Apr) | 143 | +0.255 | +1.8% | 0.79 (null) |

**The ordering is the result.** Sunday (partial reduction) < Poya (full public holiday) <
other fixed holidays (full shutdown) is monotone in the degree of activity removed, which
is what a genuine local-activity signal must look like and what a confounder would not
produce.

**The apparent conflict was an artefact of using the weakest instrument.** Converting under
a 30–50% activity reduction:

| instrument | implied f |
|---|---|
| Sunday | 0.155 – 0.259 |
| Poya (within day-of-week) | 0.205 – 0.342 |
| Poya | 0.235 – 0.391 |
| other fixed public holidays | 0.313 – 0.521 |

The stronger instruments reach and overlap the four converging lines (hierarchical 0.392,
coherence floor 0.410, NBRO 0.446). **f ≈ 0.40 is now supported by a fifth line that
measures local activity directly**, and the earlier Sunday-based objection is withdrawn:
Sunday is a partial-activity day and understates the share.

**One unexplained anomaly, reported not explained away.** The Sinhala/Tamil New Year shows
**no effect at all** (+1.8%, p = 0.79) despite being the largest annual shutdown. Candidate
causes — April is the inter-monsoon transboundary peak, which may swamp the local signal;
large-scale holiday travel replaces commuting; celebratory burning offsets traffic — are
untested. n = 143 hours over few years is also thin. This is flagged as open.

**Standing caveats.** The effect sizes are assumption-free; the conversion to f is not, and
the 30–50% activity-drop assumption is unverified for Kandy and dominates the width. The
outcome is FECT point sensors, not the basin mean. Sources with no holiday cycle — domestic
cooking, waste burning, road dust — are invisible to this design and fall to the regional
side, so every figure here is a **lower bound** on the total local share.

## F.23 — the ~90% vehicular assumption, tested at last (2026-08-06)

The emission-timing profile e(t), the traffic-centrality emission surface, and hence the
shipped diurnal shape all rest on Kandy being roughly nine-tenths vehicular. That figure
came from an EDGAR sector prior and had **never been tested**. The holiday instrument
(F.22) tests it directly: if local emissions are vehicular, the holiday effect must
concentrate at rush hours; if they are cooking, waste burning or dust, it must be flat.

| window | mean holiday effect |
|---|---|
| rush (06–09, 17–20) | **−2.893 µg m⁻³** |
| off-peak (00–04, 11–14) | −0.789 µg m⁻³ |
| **ratio** | **3.67×** |

Hour by hour the effect peaks at **07:00 (−3.38)** and across **17:00–20:00 (−3.35, −3.26,
−3.42, −4.34)**, and is indistinguishable from zero at 00:00 (+0.10). **The assumption is
corroborated**: the local, activity-responsive component of Kandy's PM2.5 is strongly
bimodal and rush-hour timed, which is what a vehicle-dominated local source must look like
and what a 7-day-cycle source such as domestic cooking cannot.

Two consequences. First, e(t) moves from *imposed prior* to *prior with local observational
support*, which upgrades its claim tier. Second, a refinement is now visible: the observed
evening peak is **larger than the morning peak and later than e(t) places it** (maximum at
20:00 rather than 18:00). Adjusting e(t)'s evening lobe is cheap and is the one concrete
improvement this test identifies.

Caveats as F.22: FECT point sensors rather than the basin mean; the control is
month × hour × ventilation quintile rather than a full meteorological model; and sources
with no holiday cycle remain invisible, so this bounds the *timing* of the local component
without bounding its total magnitude.

## F.24 — does the anchor choice flatter the transfer validation? Partly, and not where expected (2026-08-06)

`scripts/anchor_choice_sensitivity.py`. Every headline transfer number comes from running
the model at a "two-sensor budget matching Kandy's scarcity", but the two anchors are not
drawn at random — the rule picks the **dirtiest and cleanest well-sampled stations**, with
full knowledge of every station's mean. Kandy's two sensors are simply wherever FECT put
them. If the extremal choice outperforms an arbitrary pair, the panel flatters Kandy.

Tested at Medellín (16 well-sampled stations, 2023, clean temporal split): the shipped
extremal pair against 30 random pairs, each scored on the stations it is not using.

| metric | shipped | random median | random p10–p90 | shipped beats |
|---|---|---|---|---|
| RMSE | 6.240 | 5.909 | 5.504–6.235 | **10%** |
| abs. level bias | 14.42% | 9.06% | 0.95–16.68% | **23%** |
| **seasonal r** | **0.970** | 0.960 | 0.944–0.968 | **97%** |
| diurnal r | 0.967 | 0.960 | 0.872–0.980 | 60% |
| hourly r | 0.588 | 0.588 | 0.549–0.608 | 47% |

**Two opposite effects, which an average across metrics would hide** — and the first
version of this script did exactly that, reporting a meaningless "47%, representative".

**Level and RMSE are PENALISED, not flattered.** The extremal pair is worse than 77–90% of
random pairs. The reason is a genuine estimator property: averaging the two extremes of a
skewed station distribution is a **biased estimator of the network mean**, whereas a random
pair is closer to an unbiased sample of it. **The panel's level claim is therefore
conservative rather than optimistic** — the opposite of the concern.

**Seasonal shape IS flattered**, at the 97th percentile. An arbitrary two-sensor city
should expect **seasonal r ≈ 0.960 (p10 0.944)** rather than the ~0.97 the extremal pair
achieves. The margin is about **+0.01**, so it does not overturn the seasonal claim, but the
scorecard's seasonal figures should be read as the favourable end of the achievable range,
and that qualification belongs in the paper.

**Scope.** Only the temporal anchor depends on sensor choice; `P_local` never sees a sensor,
so spatial rank is untouched. Absolute values here are not comparable to the scorecard
(clean temporal split, no amplitude sharpening, no full field build) — only the POSITION of
the shipped pair within the random distribution is meaningful. One city, 30 pairs; repeating
at Kathmandu (45 stations) would strengthen it.

## F.25 — the shipped interval, coverage-tested for the first time; and a pre-registered prediction (2026-08-06)

`scripts/kandy_interval_coverage.py`. Three coverage numbers circulate in this project and
refer to different objects: 0.865 (Stage A v3 LOMO, the hourly *anchor*), 0.707 (the
*sensorless* daily anchor, the basis for the forecast's 1.35× widening), and the coverage
of the interval the webapp and paper actually **ship** — which had never been computed.

Measured at the only place Kandy has observations, the two FECT sensor pixels (19,585
matched hours, 2019–2026):

| | coverage |
|---|---|
| **shipped 90% interval, as displayed** | **72.4%** |
| anchored tier 2019–2023 | 71.6% |
| extension tier 2024+ | 76.9% |
| by season | DJF 77.3 · MAM 81.7 · **JJA 61.7** · SON 65.4 |

That looks damning, and the first reading was that the intervals are too narrow. **They are
not.** The failure is almost entirely one-sided — observations fall *below* the lower bound
in 25.7% of hours and above the upper bound in only 1.9% — with a model-minus-observation
median of **+5.85 µg m⁻³ (+43%)**. That is a CENTRING offset, not a width problem, and it is
the documented area-versus-point geometry: a 1 km pixel mean sits above a point sensor
inside it, which is the same effect that makes the KOALA figure a valley-floor value rather
than a basin mean (gotcha #51), and which the residual-stage `b_FECT` constants (−9.105,
−13.749) already encode.

**Removing each sensor's own median offset restores nominal coverage:**

| sensor | offset | coverage after offset removal |
|---|---|---|
| Akurana (12451) | +5.16 | 87.2% |
| Hantana TR4 (33495) | +6.38 | 97.4% |
| **pooled** | | **91.5%** (nominal 90%) |

**The interval width is correct; the interval is not centred for a point comparison.** Both
statements should be made, because only stating the first would be misleading and only
stating the second would be alarming.

### A pre-registered prediction, and the reason it matters
The project's highest-value pending action is obtaining a local measurement — the CEA
archive, NBRO "Kandy 1", or a mobile campaign. **When that arrives, a naive comparison of
the shipped field against it will show the model roughly 40% high, and will look like a
catastrophic failure.** It is not: it is the expected area-versus-point offset, of order
**+5 to +6 µg m⁻³ at a valley-floor or ridge site**, and it must be removed before any
coverage or bias statement is made. Recording this in advance turns a future false alarm
into a confirmation, and makes the prediction falsifiable: an offset far outside that range
would indicate a genuine level error.

**Caveats.** The comparison is in-sample — T(t) is trained on and sharpened to these
sensors (gotcha #68) — so 91.5% is an optimistic bound on width calibration, not a
validation. Offsets are each sensor's own median, which is also in-sample. Two sensors,
one of them (Akurana) 0.93 km from its nearest pixel and outside the model's bounding box.
The seasonal pattern (JJA worst at 61.7%) is consistent with the wet-season high bias
already seen from three other directions (F.14, F.17, F.22) and is not explained away here.

---

## F.26 — spatial rank: bootstrap intervals, and the panel splits in two

`scripts/spatial_rho_bootstrap.py` → `results/figures/multicity/spatial_rho_bootstrap.csv`.
The scorecard reported Spearman ρ from 0.78 down to −0.06 with **no intervals**, and the
preprint built a substantive ordering on those differences. Station-resampled bootstrap
(10,000 draws) + permutation test:

| city | n_ranked | ρ | 90% CI | p |
|---|---:|---:|---|---:|
| Medellín | 16 | 0.78 | [0.49, 0.93] | 0.0006 |
| Tai'an | 11 | 0.68 | [0.16, 0.97] | 0.023 |
| Bogotá | 17 | 0.67 | [0.35, 0.87] | 0.003 |
| Baoji | 16 | 0.59 | [0.12, 0.91] | 0.020 |
| Kathmandu | 38 | 0.39 | [0.10, 0.64] | 0.016 |
| Yichang | 10 | 0.13 | [−0.63, 0.75] | 0.73 |
| Bazhong | 9 | 0.10 | [−0.58, 0.70] | 0.81 |
| Xichang | 9 | 0.07 | [−0.68, 0.94] | 0.87 |
| Chiang Mai | 11 | −0.06 | [−0.62, 0.47] | 0.86 |
| Chandigarh | **2** | — | — | not estimable |

- **The finding is bimodality, not an ordering: 5 of 9 estimable cities are resolvable,
  4 are indistinguishable from zero** (p > 0.7, intervals spanning nearly the whole range).
  Never again interpret the rank order among Yichang/Bazhong/Xichang/ChiangMai.
- **🔴 A REPORTING DEFECT FOUND: `n` in the scorecard is the HELD-OUT count, but ρ is
  computed on the subset falling inside the modelled domain**, and they differ a lot —
  Chiang Mai 31 → **11**, Medellín 22 → **16**, Bogotá 20 → **17**, Chandigarh 4 → **2**.
  The paper printed the larger number beside the spatial column. Both are now reported.
- Chandigarh's n_ranked = 2 independently confirms "not estimable" (gotcha #69).

## F.27 — the visibility corroboration IS independent (tested, not asserted)

`scripts/visibility_partial_correlation.py` → `decomp/visibility_partial_correlation.{csv,json}`.
The preprint called VCBI visibility "a fully independent check" because the variable is not
a model input. **That reasoning is incomplete**: visibility is driven by humidity and rain,
and ERA5 humidity and rain ARE model drivers, so the raw r = −0.46 could be a shared cause.
Tested by partialling out humidity (from the same METAR) and rain + BLH (from **the model's
own ERA5 drivers** — the conservative choice, since it removes exactly the variance the
model consumes):

| control | r | p |
|---|---:|---:|
| none (raw) | −0.456 | 5e-20 |
| station RH | −0.515 | 9e-24 |
| RH + ERA5 rain | −0.508 | 4e-18 |
| RH + rain + BLH + T | −0.448 | 7e-14 (n=257) |

- **SURVIVES, and strengthens slightly.** Context: visibility↔RH r = −0.40 while model
  PM↔RH r = −0.07, so the two are not sharing that pathway.
- ⚠ **VCBI reports NO precipitation** in the ASOS archive (same defect as SKMD, gotcha #60),
  so a METAR-only rain control is vacuous — the ERA5 substitution is not optional.

## F.28 — two claims cut down to size: embedding power, and the Yichang "regime boundary"

`scripts/reviewer_response_stats.py` → `results/figures/multicity/reviewer_response_stats.json`.
- **The AlphaEarth null is underpowered and the preprint over-claimed it.** Minimum
  detectable partial ρ at 80% power: **0.65** (Medellín n=17), **0.82** (ChiMai n=10),
  **0.96** (KTM n=6). The test excludes only a LARGE independent embedding signal. It was
  described as "most directly" supporting the information ceiling; it cannot carry that.
  **The five "independent lines" are honestly three** — two pairs were restatements.
- **No selection-time descriptor predicts the Yichang failure.** Its emission mix is
  *identical* to Tai'an's and Bazhong's (0.45/0.55/0.00) and its climate/emission/magnitude
  scores sit inside the passing range; only topographic similarity falls marginally outside
  (0.63 vs [0.66, 0.74]) — and that threshold would also flag **Medellín (0.65), the
  panel's best city**. ⇒ **the applicability map is DESCRIPTIVE on the diurnal axis, not
  predictive.** A screen built now would be post hoc; deliberately not done.
- **Level bias is systematic, not symmetric:** median **+7.6%**, median |bias| 7.6%,
  IQR [+2.5, +12.1]%, 7/10 within ±10%, and only Baoji (−4%) below observed. "−4% to +30%"
  is a range, not a summary; the model runs high nearly everywhere, and that belongs in the
  health caveat.

---

## F.29 — W10: the emission clock e(t) is FITTED, not assumed (evening lobe)

`scripts/kandy_emission_clock_fit.py` → `decomp/kandy_emission_clock_fit.{csv,json}`;
implemented in `src/stage1_satml/decomp/emission_profile.py` behind `EVENING_FIT`.

A public holiday removes local activity and leaves transboundary transport untouched, so
the holiday-minus-working-day difference **at hour h** estimates the local emission clock
at hour h. Met and season are controlled by differencing against (month × hour ×
ventilation-quintile) cells, so the comparison is *within* hour-of-day and cannot
manufacture a diurnal shape. 971 treated sensor-hours, 2018–2025.

| quantity | EDGAR prior | measured (bootstrap 90% CI) | verdict |
|---|---|---|---|
| morning peak hour | 08:00 | 08:00 | **prior CONFIRMED** |
| evening peak hour | 17:00 | 19:00 [17, 21] | shifted later |
| evening/morning ratio | 0.97 | 2.14 [1.17, 4.35] | **prior REJECTED** (CI excludes it) |

- The prior said morning ≈ evening; **the data say the evening lobe is roughly twice the
  morning one.** The CI excludes the prior value, so this is not merely uncertainty.
- **Correction is deliberately partial:** evening lobe only, +1 h shift and ×1.479 gain,
  **shrunk toward the prior** (w = 0.40) in proportion to the CI width, because ~40 treated
  hours per bin is thin. Morning lobe, night floor and overall shape stay EDGAR.
  Agreement with the measured clock rises **r = 0.49 → 0.755**.
- **e(t) moves from an imposed prior to a prior with a local observational correction.**
- ⚠ Every holiday figure is a **lower bound** on local emission: sources with no holiday
  cycle (cooking, waste burning, road dust) are invisible to the instrument.
- ⚠ Implementation trap found and fixed: shifting the lobe with `np.roll` **wraps** the
  tail back onto the window start and punches a hole at 14:00. The shift is in *time*, not
  a rotation — use index clamping.

**Rebuild + propagation.** `build_overlay_predictions` → `build_spatial_uq` →
`build_additive_field_v2` → `_v3` → `webapp_export`. G1 T-lock **exact (Δ 0.000)** every
year; exporter **QA PASS at 0.0017 µg/m³** (tol 0.25); wind parity 0.0005 m/s.

**🔴 ONE CONSEQUENCE NEEDING A DECISION.** The locked additive_v2 annual means move in the
third decimal: **19.750 → 19.752 · 19.092 → 19.092 · 17.077 → 17.079 · 18.754 → 18.755 ·
21.036 → 21.038** (max **+0.002 µg/m³**, 0.01%). This is 100× below the QA tolerance and
far below the precision at which any number is published (the paper quotes 19.8 … 21.0),
and no exposure, burden or figure changes at quoted precision. But the standing rule is
that the **locked 2019–2023 headline is untouched**, and this touches it. Either the rule
is relaxed for a change of this size, or `EVENING_FIT = False` restores the previous
profile exactly. **Recorded rather than absorbed silently.**

---

## F.30 — W7: the ventilated-hour floor eps0 does NOT transfer (and the relative form is the worse of the two)

`scripts/eps_floor_hierarchical.py` → `decomp/eps_floor_hierarchical.json`, on the per-city
slopes `flat_hour_residual_fit.py` already produced.

`additive_v3`'s floor was fitted at **one** city and carried to Kandy in **relative** form
(a fraction of the city's own mean accumulation amplitude), because that seemed the more
physical normalisation — never because it was tested. With three cities it is testable.

| city | own eps0 (µg/m³) | mean accumulation | relative | Spearman ρ | n |
|---|---:|---:|---:|---:|---:|
| Medellín | 5.65 | 14.20 | 0.398 | 0.31 | 1,751 |
| Kathmandu | 0.93 | 29.40 | 0.032 | **0.03** | 4,429 |
| Chiang Mai | 16.68 | 12.77 | 1.306 | 0.21 | 14,016 |

Hierarchical fit (same machinery as F.21; per-city SE from the slope t-statistic implied by
ρ and n, so a city whose flat-hour structure is not emission-shaped is shrunk hard):

| form | population µ | between-city τ | τ / median within-city SE | max/min |
|---|---:|---:|---:|---:|
| absolute | 7.74 | 6.57 | **14** | 18× |
| relative | 0.577 | 0.534 | **18** | **41×** |

- **eps0 is NOT a transferable constant in either form.** Between-city variation dominates
  within-city uncertainty by more than an order of magnitude, so a value fitted at one city
  predicts another's only weakly.
- **🔴 The relative normalisation the shipped model uses is WORSE behaved than the absolute
  one** (41× spread vs 18×) — the opposite of the assumption that justified choosing it.
- **Kandy: shipped 2.573 vs pooled 3.73, 90% predictive [0.00, 9.40].** The shipped value is
  **inside** the interval, so it is not contradicted — but it is one draw from a wide
  distribution, not a determined quantity, and must be described that way.
- ⚠ Kathmandu's ρ = 0.03 means its slope is essentially **unidentified**: there is no
  emission-shaped structure in its flat hours to fit. Its 0.93 is noise, not an estimate,
  and the pooling treats it accordingly.

**No code change follows, and that is the point.** The floor's *safety* was never in
question: the no-degrade gates pass at all three cities, the form is mean-zero so T-lock
stays exact, and `EPS_FLOOR = 0` recovers `additive_v2` byte-identically. What changes is
the **claim tier** — the floor's magnitude at Kandy is a weakly-determined transfer, and the
paper should say so rather than presenting 2.573 as fitted. W7 closes as a measured
limitation, not a fix.

## F.31 — B(t) vs NBRO refreshed: the binding constraint is the SEASON, not the sample

Re-ran `kandy_background_nbro_check.py` with the NBRO log now at **90 days**
(2026-05-08 → 08-06), double the 44 in F.14. Overlap with the model is **unchanged at 44
days**, because the *model record* ends 2026-07-21 (ERA5-Land latency), not because the
observations are short. Every number reproduces exactly: modelled B = 8.73 sits between the
network P10 (5.35) and median (11.49), ratio 1.12 to P25, daily r ≈ +0.37, ordering
floor < median < mean holds, and B is 1.51× the ×1.35-corrected floor.

**Consequence for the plan:** extending the driver record would add ~11 days of *wet-season*
overlap and cannot change the conclusion. The gate that matters is **DJF**, when the
transboundary background dominates and no external check exists at all. From **December
2026** this script becomes decisive; before then, more days are not more information.

---

## F.32 — 🔴 the spatial rank statistic is UNSTABLE to an undocumented sampling convention

`scripts/spatial_pairing_diagnostic.py` → `results/figures/multicity/spatial_pairing_diagnostic.json`.

The published spatial column averages modelled values over all modelled hours and observed
values over all observed hours **separately**. Averaging both over the *same* hours instead
(an inner join on `(hour, station)`) changes the answer by **0.404 on average and 0.882 at
worst**, in **both directions**.

| city | published | hour-matched | shift |
|---|---:|---:|---:|
| Chiang Mai | −0.06 | +0.82 | **+0.88** |
| Yichang | +0.13 | +0.95 | +0.82 |
| Xichang | +0.07 | +0.75 | +0.68 |
| Kathmandu | +0.39 | +0.93 | +0.54 |
| Bazhong | +0.10 | −0.22 | **−0.32** |
| Medellín | +0.78 | +0.78 | −0.00 |
| Bogotá | +0.67 | +0.63 | −0.04 |

**Verified, not assumed.** The unpaired route reproduces the published scorecard to
**0.000** on the same stations, years and domain filter, so the cause is **isolated to
hour-matching alone**; and the merge is strictly one-to-one (`any_duplicate_keys: false`),
so no join defect inflates it.

**Mechanism, supported but not established.** The two cities with the most *even* station
coverage move least (Medellín CV 0.30 → −0.003; Bogotá CV 0.34 → −0.039) while the most
uneven move most (Kathmandu CV 1.15 → +0.54; Bazhong CV 1.01 → −0.32). Uneven reporting
periods let a station's observed mean encode **when** it reported rather than where it is.

**⚠ Neither statistic is trustworthy.** Unpaired lets sampling periods contaminate the
observed means; **paired hands every station the temporal weighting of its own
observations**, so a model with strong temporal skill and *zero* spatial skill would still
score well — and this model's seasonal *r* is 0.94–1.00.

**Consequence: F.26's bootstrap intervals understate the true uncertainty**, because they
resample stations while holding the convention fixed. The paper's central spatial result
rests on a measurement choice nobody documented.

## F.33 — the anomaly estimator, and why its favourable result was NOT adopted

`scripts/spatial_common_hours_test.py`, pre-registered in
`docs/prereg_common_hours_spatial_2026-08-07.md` **with the author's prior published in
advance** (that the corrected number would come out *lower*).

E1 removes each hour's network mean from both series **within that hour**, so season,
diurnal cycle, episodes and the entire temporal skill of the anchor are differenced away
before any station mean is taken.

| pooled | published | hour-matched | **E1 anomaly** |
|---|---:|---:|---:|
| spatial rank | +0.372 | +0.696 | **+0.621** |

| gate | outcome |
|---|---|
| C1 validity (E1 vs common-hours) | **FAIL — unevaluable**: the 80% quorum is reachable at only 3 of 9 cities. Where computable, agreement was **0.011**, sign 3/3 |
| C2 E1 < paired − 0.10 | **FAIL** (+0.621 vs +0.696) — **the author's contamination hypothesis is refuted at pooled level** |
| C3 permutation control | **PASS** (null centred +0.001; E1 above null p95 +0.520) |
| C4 branch | 8 of 9 ≥ 0.40 → "revise upward" |
| C5 analogues | Chiang Mai **+0.22**, Kathmandu **+0.43** — the two most Kandy-like cities are the panel's weakest |

**NOT ADOPTED, for two reasons.** The registered validity gate did not pass, and rewriting
a rule after seeing a result one likes is the exact behaviour this project criticised in
its own manuscript (the Yichang screen). More substantively, **the permutation null's p95
is +0.520**: at 4–17 stations a rank of 0.5 arises by chance easily, so "8 of 9 above 0.40"
is arithmetic, not significance — per-city p-values were never registered.

**The author's prior was WRONG** (E1 landed well *above* the published values, not below)
and is recorded as such. Per-city significance and a sparse-network estimator are
registered in `docs/prereg_spatial_significance_2026-08-07.md`; C1's design error — a gate
unreachable on the coverage this panel has — is the lesson applied there.

**Standing consequence either way:** three defensible estimators give +0.372, +0.696 and
+0.621 on identical data. That instability is now a reportable limitation of the spatial
claim, independent of which value is eventually adopted.

---

## F.34 — ✅ the spatial estimator is FIXED and VALIDATED; the claim stands, restated

`scripts/spatial_significance_test.py`, pre-registered in
`docs/prereg_spatial_significance_2026-08-07.md` (prior published in advance: *middle
branch expected, Chiang Mai expected to fail significance* — **both correct**).

| city | E1 ρ | p | null p95 | E1 τ | **E3 τ** | pairs | n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Baoji | **+0.83** | 0.000 | +0.43 | +0.67 | +0.67 | 55 | 16 |
| Bogotá | **+0.80** | 0.000 | +0.41 | +0.63 | +0.58 | 134 | 17 |
| Xichang | **+0.78** | 0.016 | +0.58 | +0.67 | +0.73 | 15 | 9 |
| Tai'an | **+0.72** | 0.016 | +0.52 | +0.56 | +0.57 | 23 | 11 |
| Medellín | **+0.66** | 0.007 | +0.43 | +0.50 | +0.56 | 119 | 16 |
| Yichang | +0.60 | 0.080 | +0.55 | +0.47 | +0.52 | 21 | 10 |
| Bazhong | +0.54 | 0.308 | +0.77 | +0.33 | +0.17 | 12 | 6 |
| Kathmandu | **+0.43** | 0.007 | +0.27 | +0.33 | +0.29 | 675 | 38 |
| Chiang Mai | +0.22 | 0.512 | +0.53 | +0.16 | +0.23 | 47 | 11 |
| Chandigarh | not estimable (<4 ranked stations) | | | | | | |

| gate | outcome |
|---|---|
| **D2 validity** — E3 vs E1_τ | **PASS**, and emphatically: pooled \|d\| = **0.002**, sign **9/9** |
| **D3** small-n inflation | **PASS**: r(E1, n) = **−0.175** — if anything *negative*, so skill is not an artefact of network size |
| D1 significant at p<0.05 | **6 of 9** |
| **D4 decision** | **6 of 9** significant *and* ≥0.40 → **middle branch: the claim STANDS, restated on a corrected estimator** |
| D5 analogues | Chiang Mai **+0.22, p = 0.51 (not significant)** · Kathmandu +0.43, p = 0.007 |

- **The estimator is now sound.** Two constructions that remove the temporal confound by
  different routes — per-hour network-mean removal, and pairwise concordance on co-observed
  hours only — agree to **0.002** across all nine cities. E3 needs no global quorum, which
  is precisely the design error that made C1 unevaluable (F.33) and is not repeated.
- **The headline claim does not change: partial and regime-bounded.** What changes is that
  it now rests on a statistic that cannot launder temporal skill, with per-city
  significance attached. The tally moves from *4 of 9 clearing the 0.40 gate* to
  **6 of 9 significant and above 0.40**.
- **Bazhong (+0.54, p=0.31) and Yichang (+0.60, p=0.08) are NOT significant** despite
  respectable ρ — small networks (n=6, n=10) with null p95 of +0.77 and +0.55. Reporting ρ
  without its own null would have overstated both.
- **🔴 The Kandy-relevant reading is unchanged or slightly worse.** Kandy's closest
  climatic analogue, Chiang Mai, is **not significant**; Kathmandu is significant but the
  weakest of the six. The cities most like Kandy remain the ones where the spatial pattern
  is least recoverable, and that is the line the transfer argument depends on.

**ACTION — the paper's spatial column should be replaced** by E1 with per-city p-values,
the tally restated as 6 of 9, and the sampling instability of F.32 disclosed as a
limitation. The qualitative conclusion the manuscript already draws survives intact.

---

## F.35 — 🔴 the fuel crisis has the WRONG SIGN: a shipped assumption is contradicted

`scripts/kandy_activity_shocks.py`, pre-registered in
`docs/prereg_activity_shocks_2026-08-07.md` (prior published: S1–S3 expected to hold, S4
least confident). Same estimator as F.22 — residuals against (month × hour × ventilation)
cells, ordinary working days only, controls are the **same calendar weeks in 2019 and 2023**.

| shock | n | effect | implied f | p |
|---|---:|---:|---|---:|
| COVID lockdown (2020-03-20 → 05-11) | 911 | **−57.8%** | 0.72–0.96 | <1e-4 |
| Fuel crisis, peak (2022-03 → 09) | 294 | **+18.0%** | — | 0.001 |
| Fuel crisis, full (2021-11 → 2022-09) | 522 | **+34.6%** | — | <1e-4 |

- **S1 PASS.** The lockdown effect (−57.8%) dwarfs the fixed-holiday effect (−15.6%),
  which is what must happen if the holiday instrument measures local activity.
  **This retrospectively supports F.22.**
- **S4 FAIL, as registered in advance.** Implied f of 0.72–0.96 is far above the converging
  band [0.26, 0.53]. The registered caveat fires: in 2020 lockdowns across India suppressed
  the **transboundary** source too, so this is not a clean local experiment. **Upper bound
  only; it says little about f.**
- **🔴 S2 FAIL, and this is the finding. The fuel crisis has the OPPOSITE SIGN.**
  Concentrations were **higher** during severe fuel scarcity, not lower. The mechanism is
  fuel **substitution**, not activity reduction: Sri Lanka's 2022 crisis brought daily
  multi-hour power cuts (diesel generators) and cooking-fuel scarcity (biomass and waste
  burning). Less traffic, more dirty combustion — and the second dominated.
- **CONSEQUENCE FOR A SHIPPED QUANTITY.** `FRAC_LOCAL_YEAR` hand-lowers f for **2021
  (0.21)** and **2022 (0.20)** on the reasoning that the fuel crisis cut local emissions,
  and the manuscript defends those values as "reasoned rather than fitted". **The data
  contradict the reasoning for those two years** — local emissions plausibly *rose*. The
  2020 lowering (0.25) is untouched by this and remains defensible.
- ⚠ **MY OWN GATE ERROR, again.** S3 compared |Sunday| < |fuel| < |lockdown| on
  **magnitudes without checking sign**, so a *positive* fuel effect satisfied an ordering
  test meant to require a negative one. It printed PASS; it is **void**, and reported as
  failed on inspection. Same class as the A2 error (F.33 arc) — **a directional gate must
  test direction.**
- **Bounds:** n = 294 on the peak window; the cell control removes meteorology and season
  but **not** year-to-year changes in the regional background, so part of the +18% could be
  a dirtier 2022 inflow rather than local substitution.

**Net:** 2 of 4 predictions met. The holiday line of evidence for f **survives and is
strengthened** by S1; the fuel-crisis rationale in `FRAC_LOCAL_YEAR` **does not survive**
and should be withdrawn from the manuscript's defence of the year-to-year variation.

---

## F.36 — Test B re-run on the corrected estimator: 2/3, and the gate that mattered FAILED

`scripts/zone_contrast_corrected.py`. Test B (zone contrast on terciles of the traffic
emission surface) passed **3/3** on hour-matched means. Those means are contaminated
(F.32–F.34), so the test was re-run on per-hour network-mean-removed anomalies. **Gates
unchanged** — only the contaminated input was replaced.

| city | obs Δ | model Δ | sign |
|---|---:|---:|---|
| Bogotá | +7.20 | +2.78 | agree |
| Baoji | +6.50 | +5.99 | agree |
| Xichang | +3.18 | +2.73 | agree |
| Bazhong | +2.93 | +0.69 | agree |
| Tai'an | +1.95 | +0.49 | agree |
| Medellín | +1.49 | +1.39 | agree |
| Kathmandu | +1.21 | +4.54 | agree |
| Yichang | +0.97 | −0.13 | **disagree** |
| Chiang Mai | −0.17 | −0.08 | agree |

| gate | result |
|---|---|
| B1 slope > 0, CI excludes 0 | **PASS** — +0.720 [+0.070, +1.591] |
| B2 sign agreement ≥ 7 of 9 | **PASS** — 8 of 9 |
| **B3 recovers ≥ 2 station-null cities** | **FAIL** — only Bazhong |

- **B3 was the point of the test**, and it failed. The motivation for reporting zones was
  that aggregation might recover structure where per-station ranking finds none. It does
  not: of the three cities not significant under the corrected estimator, Bazhong recovers,
  **Chiang Mai's contrast is negligible (|Δ_obs| = 0.17)** and **Yichang disagrees in sign**.
- **What survives is real but redundant.** Zone contrast is genuine (B1, B2) — but it adds
  no information where the station rank is already absent, so it is a coarser restatement of
  the same signal, not a rescue. **It must not be presented as a validated replacement for
  the station rank**, and the paper's spatial claim stays as F.34 left it.
- B1's interval is wide and its lower bound is barely positive (+0.07); the slope of 0.72
  again indicates the model's zone contrast is **under-dispersed by roughly a third**,
  consistent with the amplitude deficit found independently at Medellín.
- **Prior scored:** I predicted a lower slope (wrong — +0.643 → +0.720), sign agreement
  below 9/9 (right — 8/9), B1 surviving (right) and B2 marginal (wrong — it passed cleanly).
  Two of four elements correct.

**Consequence:** the "measure at a coarser resolution" idea is closed. Combined with Test A's
falsification (pooled stagnant−ventilated gap −0.001), **neither re-measurement route
rescues spatial skill at the cities that lack it.** The ceiling survives both attempts to
argue it away, which is a stronger statement of it than before they were tried.

---

## F.37 — 🔴🔴 THE EXTENSION TIER (2024–2026) CANNOT REPRESENT THE EPISODE REGIME

`scripts/extension_tier_audit.py` → `decomp/extension_tier_audit.{csv,json}`.
Triggered by a user report of "physically implausible" estimates after 2023. **The report
is correct, the defect is structural, and it had never been tested for.**

**What is fine.** Annual means, monthly means (within ±12% of the locked climatology, with
the seasonal shape intact), diurnal swing (ratio 0.99 to locked), diurnal phase (peak 07,
trough 14), background ratio and accumulation fraction. On every *aggregate* diagnostic the
extension tier looks healthy — which is why this survived a year of review.

**What is broken: the tail.**

| threshold | locked (hours/yr) | extension (hours/yr) | ratio |
|---|---:|---:|---:|
| > 35 µg/m³ (WHO IT-1) | 955 | 635 | 0.66 |
| > 45 | 310 | 108 | **0.35** |
| > 55 | 84.8 | **0.5** | **0.01** |
| > 65 | 21.8 | **0** | **0.00** |
| > 75 | 6.0 | **0** | **0.00** |

The extension T maxes at **56.5 µg/m³ across all three years** (2024 56.5 · 2025 54.8 ·
2026 56.0) — a ceiling at the **99.2nd percentile of the locked distribution**. Roughly
**69 hours per year that the locked years do produce are unrepresentable**. Three
consecutive years capping within 1.7 µg/m³ of each other is the signature of a structural
ceiling, not of weather.

**Root cause, confirmed in the code.** `sharpen_to_locked()` in
`kandy_driver_tier_build.py` corrects the GBM's regression-to-the-mean by multiplicative
(hour-of-day) and (month) **climatological** factors. Its own docstring states the limit
plainly: *"Phase and synoptic variability are untouched."* The synoptic scale — which is
exactly where episodes live — was never corrected. Three compounding mechanisms:
1. a quantile GBM predicts **leaf averages**, which shrinks the tail at every timescale;
2. tree ensembles **cannot extrapolate** beyond training targets, so the locked maximum is
   a hard ceiling and the achieved ceiling sits well below even that;
3. the tier is **lag-free**, removing the persistence by which multi-day episodes build.

**Secondary defect (audit check E).** Mean 90% interval width is **27.3 µg/m³ in the
extension against 29.4 in the locked years** — *narrower* on the tier that is *more*
uncertain. The `infl` coverage inflation is fitted on the locked period and the q05/q95
heads are damped by the same GBM, so the interval neither widens for extrapolation nor
compensates for the damped centre.

**Tertiary (2026 only).** 2026 is built **ERA5-ONLY**: no GEOS-CF chemistry prior and
**no boundary-layer height**. BLH is the primary driver of stagnation, so 2026 has no direct
information about the mechanism that produces episodes. The fallback was validated on level,
monthly *r* (0.996) and hourly *r* (0.807) — **never on the tail**, the same blind spot.

**Also: 2026 is a PARTIAL year** (January–July, 4,825 h). Its record mean of 20.68 must not
be compared with a full-year mean; on the common Jan–Jul window the locked years average
20.97, so 2026 is unremarkable rather than high.

**CONSEQUENCE.** Anything the extension tier says about **episodes, exceedance hours, or
health burden after 2023 is wrong and wrong in a specific direction — too clean.** A user
browsing 2024–2026 in the explorer would reasonably conclude Kandy stopped having haze
events. Aggregate/annual statements from the tier remain defensible.

**RECOMMENDED FIX (not yet implemented).** Quantile delta mapping: map the extension T's
empirical distribution onto the locked distribution per month, which restores the tail while
preserving the GBM's ranking of which hours are dirty. It is the standard tool for exactly
this bias and can be **validated by holding out a locked year**. It fixes the *distribution*,
not necessarily event *timing*, and that distinction must be stated. Until then the tier
should be labelled **"climatological — does not resolve episodes"** wherever it is shown.

---

## F.38 — the nocturnal hotspots and flat daytime: what is real, and what is a hand-set constant

User report: "midnight high pollution ... daytime pollution very low." Investigated at three
levels. **Two of the three findings exonerate the model; the third does not.**

**1. The basin-mean diurnal shape is CORRECT — verified against observation.** Normalised
against the FECT record (2019–2023), model and observed agree to <0.07 at every hour:

| | night 00–04 | midday 12–15 | night/midday |
|---|---:|---:|---:|
| observed | 0.865 | 0.756 | **1.145** |
| model | 0.847 | 0.763 | **1.110** |

**Kandy's nights genuinely are dirtier than its middays**, and the model is if anything
slightly *flatter* at night than the measurements. ⚠ **This refutes gotcha #54**, which
states deep-night 00–05 is "≈ the daily MINIMUM". It is not: the observed minimum is at
14:00 (0.725) and deep night sits ~15% above it. **Gotcha #54 must be corrected.**

**2. Daytime flatness is largely real.** The transport amplitude
`a(t)=clip(e(t)·18/(wind·BLH), 0, 0.5)` has a median of **0.007–0.013 at 10:00–15:00** —
essentially zero — so midday fields are near-uniform at the basin mean. Deep convective
mixing genuinely homogenises a basin this size; the `additive_v3` ε-floor exists precisely
because *perfectly* flat was wrong, and midday max/min is now 1.13 rather than 1.00.

**3. 🔴 The extreme hourly contrasts are set by a HAND-CHOSEN CONSTANT, not by physics.**
Per-hour spatial statistics (2023) show maximum pixels reaching **100–203 µg/m³ on nights
and rush hours whose basin mean is only 20–30**, with max/min ratios of **3.5–4.7 at
06–07 and 18–23** against **1.13 at midday**. The cause is the cap:

| hours | % of hours where a(t) SATURATES at 0.5 | median raw a(t) |
|---|---:|---:|
| 06–07 | 8.9 – 12.7% | 0.09 – 0.10 |
| 18–21 | 8.1 – 15.6% | 0.09 – 0.12 |
| 10–15 | 0.0% | 0.007 – 0.013 |
| all | 3.6% | 0.031 |

On the ~4% of hours that saturate — calm, shallow boundary layer, rush-hour emissions — the
amplitude is **not determined by the meteorology at all**; it is pinned at the constant
`0.5`, which is roughly **10× the median** and was hand-set, never calibrated. **Those are
exactly the hours a user notices**, and their spatial amplitude has no empirical support.
This is `A_transport`, the layer the paper already ships as an unvalidated scenario — but
the paper quotes the *annual* core/edge contrast (1.20–1.25×) while the hourly maps reach
**4×**, and that gap is nowhere disclosed.

**⚠ Our own W10 change interacts with this.** The measured evening-lobe correction raised
e(t) at 20:00–23:00 by **+42%** (and lowered 00:00–04:00 by 17%), which raises the
late-evening amplitude further. The correction is evidence-based (F.29) and was already
shrunk toward the prior, so it stands — but it makes disclosure of the nocturnal amplitude
more pressing, not less.

**ACTIONS.** (a) correct gotcha #54; (b) disclose that hourly contrast reaches ~4× where the
annual figure is 1.2×, and that the cap is a prior; (c) consider deriving the cap from the
zone-contrast slope (F.36 measured the model under-dispersed at 0.72 on *annual* zone
contrast, which is the only empirical handle on amplitude the project has); (d) the ε-floor
and the cap are the two hand-set constants that shape every hourly map and neither is
calibrated.

---

## F.39 — ✅ the extension tail is CORRECTED and validated; disclosure added

`scripts/extension_tail_correction.py` (+ `extension_interval_widening`), fixing F.37.

**Method.** Not a naive remap of the extension distribution onto the locked one — that
would erase genuine interannual differences. Instead the estimator's **own damping
signature** is measured and inverted: leave-one-year-out over 2019–2023 gives out-of-sample
driver-GBM predictions for years where truth is known; per month, the gap between predicted
and true quantiles gives a multiplicative factor **indexed by quantile**; that factor is
applied to the extension years by the quantile each hour occupies within its own month. The
ranking of hours is untouched, so real year-to-year differences survive (2025 remains the
cleanest year).

**Validation — leave-one-year-out, fit on four, correct the fifth:**

| | raw | corrected | truth | corrected/truth |
|---|---:|---:|---:|---:|
| mean | 18.71 | 19.07 | 19.05 | **1.00** |
| p99 | 44.60 | 54.89 | 54.85 | **1.00** |
| max | 55.76 | 79.54 | 84.84 | 0.94 |
| hours > 55 | **1.8** | **88.2** | **84.8** | **1.04** |

Both gates pass (p99 within 10%, level within 5%). Applied:

| year | mean | p99 | max | h>55 |
|---|---|---|---|---|
| 2024 | 19.13 → 19.48 | 46.5 → 56.1 | 56.5 → **91.7** | 1 → **101** |
| 2025 | 17.72 → 18.09 | 44.9 → 54.9 | 54.8 → **75.3** | 0 → **88** |
| 2026 | 20.68 → 21.01 | 45.3 → 55.3 | 56.0 → **79.4** | 2 → **50** |

Interval widening applied in the same pass: extension mean 90% width **27.3 → 41–49 µg/m³**
against 28–30 locked, so the less-certain tier is now the wider one. **All five audit flags
cleared**; T-lock exact; exporter **QA PASS 0.0015**; 18 invariant tests pass.

**🔴 THE LIMITATION, and it must travel with the number.** This corrects the **marginal
distribution** of episodes, **not their timing**. Hourly correlation with truth is unchanged
by construction (0.836–0.890) — the correction cannot improve the GBM's ranking of which
hours are dirty. A specific hour in 2024–2026 is indicative of conditions, not a reading.
Weakest year is 2022 (corrected 101 vs 154 true hours >55; max 71.6 vs 102.8): it contained
an exceptional episode beyond the reach of a quantile correction.

⚠ **Process defect caught during the rebuild:** `kandy_extension_fields.py` defaults to
`--years 2024 2025`, so the first rebuild silently left **2026's field stale against its
corrected anchor** — the gotcha #65/#70 family again (a partial rebuild desyncs a consumer).
Verified fixed: 2026 basin now 21.01, matching its corrected T.

**Disclosure shipped**, not just recorded: the exporter's `tier_note` and the public method
page now state that the estimator under-produced episodes, that the correction fixes
frequency and not timing, and — separately — that the hourly spatial *sharpness* is set by an
uncalibrated bounded constant (F.38), so the annual ~1.2× contrast is the defensible figure
and a single dramatic hour is not.

---

## F.40 — the partition plan STOPS at step 1 (as registered) — but confirms the premise and adds a fourth line on f

`scripts/panel_reference_partition.py`, pre-registered in
`docs/prereg_partition_identification_2026-08-07.md`. The plan was to make the local fraction
an **estimated, time-varying** quantity, validated by transfer the way every other claim is.
Step 1 built the thing an estimator would be scored against: a reference partition at the
panel cities, using their dense networks and a leakage-free core/periphery split by traffic-
emission percentile, with an hourly Lenschow lower envelope across peripheral stations.

**Gate outcome: 3 of 10 cities pass; P4 required 5. THE PLAN STOPS.**

| gate | result |
|---|---|
| P1 periphery genuinely peripheral (sep ≥ 0.25) | **8 of 8** — separation 0.62–0.68 everywhere |
| P3 not a network-geometry artefact | **8 of 8** |
| **P2 reference physically ordered (≥95%)** | **3 of 8** — the binding failure |
| **P4 ≥5 cities pass** | **3 of 10 → FAIL** |

Passing: Kathmandu (98% ordered), Medellín (97%), Bogotá (99%). Failing on P2: Yichang (75%),
Chiang Mai (78%), Tai'an (86%), Bazhong (87%), Baoji (95%, just short). Not estimable:
Xichang (0 usable hours), Chandigarh (1 peripheral station).

**🔴 The most interesting result is WHY P2 fails, and it is not a detail.** P2 fails when the
peripheral 10th percentile *exceeds the network mean* — i.e. the periphery is not cleaner
than the core. That happens in **13–25% of hours at five cities with real, dense networks**.
This is the same pathology as Kandy's `B > T` in 28.5% of hours (F.17), which we have been
treating as an artefact of our own background construction. **It is not.** An
observation-based background, built from actual peripheral monitors, incurs it too.
Background/increment decomposition at *hourly* resolution appears to be intrinsically
ill-posed a fifth to a quarter of the time, whatever the background is built from.

Note the confound, which is why this is not stated more strongly: the passing cities are the
three with the largest peripheral groups (13, 6, 5 stations) and the failures cluster at 4.
With four peripheral stations a 10th percentile is a noisy statistic. So P2's failure is part
physics and part sampling, and this design cannot separate them.

**✅ The descriptive output — the reason step 1 was worth running anyway.**

| quantity | value |
|---|---|
| mean `f_ref` across passing cities | **0.398** |
| mean seasonal swing in `f` | **0.196** (median month_max/month_min **1.66×**) |
| mean diurnal swing in `f` | **0.170** |

- **The user's physical premise is CONFIRMED by measurement.** The partition moves by a
  factor of ~1.7 within a year and by 0.17 across the day. **A per-year constant is
  inadequate**, and that is now measured at real cities rather than argued.
- ~~**A FOURTH independent line lands on ~0.4.**~~ **⚠ WITHDRAWN — see F.41.** `f_ref = 0.398` was reported here as corroborating the ~0.4 estimates. The daily-resolution re-run gives **0.243** from the same method, same cities, same stations — differing only in averaging window. The reference is **resolution-dependent across nearly the whole disputed range**, so neither value may be used as evidence on the level. The claim should not have been made before its robustness was tested. The three genuinely independent lines (coherence floor, hierarchical fit, NBRO) are unaffected — none depends on this reference.

**What is NOT permitted from here.** Relaxing P4 to 3, or loosening the reference definition,
after seeing that exactly three cities passed, would be the post-hoc screening this project
criticised in its own review. Any follow-up — restricting to dense networks and accepting
N=3, or defining the reference at daily rather than hourly resolution — is a **new
pre-registration** with its prior published in advance, and must state that the earlier design
failed first.

**Prior scored:** I predicted P1–P4 would pass (**wrong** — P2 fails at 5 cities) and that
`f_ref` would vary roughly two-fold by regime (**right** — 1.66×).

---

## F.41 — the partition route CLOSES: both references fail, the coarse-CTM alternative fails, and the capability is now stated

### The daily reference also fails (`prereg_partition_daily_2026-08-07.md`)

Registered as a second attempt with **thresholds unchanged**, testing whether the hourly
failure (F.40) was sampling noise. **Q4: 4 of 10 pass, 5 required. As registered there is no
third attempt; the route is abandoned.**

| city | peri n | hourly ordered | daily ordered | Δ |
|---|---:|---:|---:|---:|
| Bogotá | 6 | 99% | 100% | +1 |
| Medellín | 5 | 97% | 100% | +3 |
| Baoji | 6 | 95% | **99%** | +4 |
| Kathmandu | 13 | 98% | 98% | +0 |
| Bazhong | 4 | 87% | 93% | +6 |
| Tai'an | 4 | 86% | 89% | +3 |
| Chiang Mai | 4 | 78% | 83% | +5 |
| Yichang | 4 | 75% | **75%** | **+0** |

**D1 — noise or physics? Mostly PHYSICS.** Sparse networks improved +4 points, dense +2, but
**every sparse city stayed below the gate** and Yichang did not move at all. The Lenschow
reference requires local sources concentrated in the core; where the dominant source is
**regional biomass smoke (Chiang Mai)** or **peri-urban industry (Yichang)**, the periphery is
not background — it is a source region. 🔴 **Chiang Mai, Kandy's closest analogue, fails at
both resolutions**, so even a passing panel would not have contained the cities that resemble
the target.

**🔴 The registered falsifier fired.** The prereg stated: *"If the daily mean f_ref moves far
from the 0.398 measured hourly, the reference is resolution-dependent and NEITHER version
should be trusted."* It moved to **0.243** — spanning nearly the whole disputed range, from
the shipped 0.244 to the ~0.4 the other lines support. **F.40's "fourth independent line" is
withdrawn** (corrected in place). What IS robust across both resolutions is the **shape**:
seasonal swing **1.66× hourly, 1.67× daily**.

**Prior scored:** Q2 improving (right, but insufficient), Q4 passing with 5–7 (**wrong**, 4),
D1 mostly noise (**wrong**, mostly physics).

### The coarse-CTM urban-increment alternative also fails, and instructively

The EMEP/GAINS/uEMEP family is the closest established analogue: a coarse CTM supplies the
regional background, a finer model the urban increment. GEOS-CF at 0.25° physically cannot
resolve a 15 km city, so its cell over Kandy *is* regional air. Tested over 16,090 hours:

| | mean | ratio to T | B < T | daily r |
|---|---:|---:|---:|---:|
| GEOS-CF raw | 46.3 | 2.35× | 15.7% | 0.445 |
| GEOS-CF × 0.536 | 24.9 | 1.26× | **39.9%** | 0.445 |

Implied `f` by month: **+0.18 (Feb) to −1.75 (Oct)**, annual mean **−0.61**. The background
exceeds the total 60% of the time. **Why it fails is the point:** EMEP's regional level is
trusted because it is validated against a continent of rural monitors; GEOS-CF's level at
Kandy is not, and our only scaling factor (0.536) was calibrated to match **total** observed
PM, not background. A total-calibrated number used as a background guarantees incoherence.
The method is sound; its critical ingredient — a trusted rural level — is precisely what
Kandy lacks. A remaining variant (learn GEOS-CF's *rural* bias at panel cities and transfer
it) is **not attempted**: the monsoon months are where the bias is worst and where transfer
is least likely to hold.

### ✅ CAPABILITY STATEMENT — what this project can and cannot claim about the split

- **CAN: the annual level, to roughly ±0.1.** Three independent lines converge — coherence
  floor **≥0.41**, hierarchical fit **0.392 [0.258, 0.525]**, NBRO instrument **0.446**. None
  depends on the failed reference. The shipped 0.244 is refuted.
- **CAN: the seasonal shape, qualitatively.** ~1.66× swing within a year, measured at panel
  cities and stable across resolution.
- **CANNOT: a validated time-varying f.** Not for want of an estimator — for want of anything
  credible to score one against. Two reference designs failed; the coarse-CTM route failed.
- **PROBABLY CANNOT AT ALL: an hourly split.** `B > T` in 28.5% of hours at Kandy was assumed
  to be our construction's defect. **It is not** — observation-based references at cities with
  real networks incur 13–25% hourly and 7–25% daily. Hourly background/increment decomposition
  appears close to ill-posed however the background is built. **This is a transferable finding
  worth publishing**, and it is stronger than the caveat it replaces.
- **The decisive input is unchanged:** one monitor upwind of or inside the basin.

**Standing rule from here: no sixth background reformulation.** Five rebuilds, two reference
designs and one coarse-CTM route have now failed on gates set in advance. The partition is
reported as an annual bound with an interval, its seasonal variation described qualitatively,
and its hourly form declared unidentifiable.

---

## F.42 — external reviewer, two claims: one real defect in the locked tier, one stale UI text

An external reviewer reported that the local fraction reaches zero in 2019 and questioned
whether the model obeys advection–diffusion–deposition. Both checked against code and data.

### Claim 1 — zero local fraction. CORRECT, and the framing was wrong on our side.
`T ≤ B` in **24.9% of 2019 hours** (2% in January to **63% in October**; 34% of midday
hours). The reviewer's physical argument is the decisive one and we had not stated it:
**traffic, cooking and waste burning are continuous, so the local increment at an emitting
location is strictly positive at every hour, including in rain** — rain changes removal, not
emission. Therefore `B ≥ T` **is not a physical state**; it is evidence that **B is
over-estimated for that hour**. Reporting "0% local" describes the atmosphere incorrectly;
the defect is in the background estimate, not in the emissions.

| tier | spatial spread on `B ≥ T` hours | fully flat |
|---|---:|---:|
| `additive_v2` (locked, paper) | **0.00 µg/m³** | **100%** |
| `additive_v3` (shipped, app) | 1.33 µg/m³ (max/min 1.225) | 0% |

- 🔴 **The locked paper tier renders exactly flat on a quarter of 2019.** The ε-floor (F.11)
  already fixes this in the served tier; the scored tier still carries it and the manuscript
  should say so.
- 🔴 **A STALE UI STRING was found and fixed:** the app said *"the map is uniform by
  construction"* — true of v2, **false of the v3 tier actually served**, where the pattern
  floor keeps structure. The text described a tier the user was not looking at.
- **Fixed:** the app no longer prints a zero. It states that the background is over-estimated
  for that hour, that local emissions continue, that the true local share is above zero and
  unquantified, and that the map still carries the local pattern.

### Claim 2 — "does not follow advection–diffusion–deposition". HALF WRONG, and the other half matters.
`terrain_transport.py` **does** solve `u·∇C − ∇·(K∇C) + λC = S` on the SRTM terrain, with
channelled flow, katabatic drainage, ridge-suppressed diffusivity, a first-order deposition
loss (`LAM = 3e-6 s⁻¹`) and a road-network source; its three parameters were calibrated
across ten monitored valleys. So the claim that there is no such physics is wrong.

**But the shipped field is not a solution of that equation**, for four reasons now stated
publicly on the method page:
1. the solve is **steady-state** — no `∂C/∂t`, so the field has **no memory** and cannot
   accumulate an episode (the same structural gap as F.37);
2. only the **shape** is used — `C / C.mean()` clipped to [0.4, 4.0]; the solver's
   concentrations are discarded;
3. the **level is imposed**, not conserved — the T-lock replaces mass conservation with a
   statistical constraint;
4. the framework is a **source-apportionment decomposition**, not a chemical transport model.

**Actions taken:** new public `#physics-status` section stating all four points and the
design reason; the split section rewritten around the "background over-estimated, not
emissions absent" framing. **Action outstanding:** the manuscript should carry the same
statement, and should disclose that the *locked* tier is exactly flat on ~25% of hours.

---

## F.43 — ✅ THE COHERENCE CAP: the partition is fixed by physics, and f is ~0.48

An external reviewer supplied the argument that eight internal attempts had missed: **local
sources emit continuously, so at an emitting location the local increment is strictly
positive at every hour** — rain changes removal, not emission. Therefore `B ≤ T` always, and
a background at or above the total **is not a physical state**; it is an over-estimated
background. Reporting "0% local" described the atmosphere incorrectly.

**Implementation.** The background is daily-flat, so the constraint has a closed form — it is
the coherence bound already derived in F.17: cap each day's `B` at `(1 − F_MIN) ×
min_hour(T)` for that day. Daily-flat structure is preserved, a local share of at least
`F_MIN` is guaranteed at every hour, and it is a **derived** constraint, not a new degree of
freedom. Fires on 50–77% of hours.

**F_MIN is not a tuning knob, and the sweep proves it:**

| F_MIN | pooled f | zero-local hours | B_JJA/B_DJF |
|---:|---:|---:|---:|
| 0.00 | 0.477 | 2.57% | 0.390 |
| **0.02** | **0.483** | **0.08%** | **0.388** |
| 0.05 | 0.492 | 0.08% | 0.385 |
| 0.08 | 0.502 | 0.08% | 0.382 |

`f` moves by 0.025 across a fourfold change in the parameter. **The coherence constraint
alone forces f ≈ 0.48.** F_MIN = 0.02 was chosen as the smallest value that removes the
defect (0.08% residual vs 2.57% at zero), not to hit a target.

**f = 0.483 is consistent with every independent line**: above the coherence floor (≥0.41),
inside the hierarchical interval (0.392 [0.258, 0.525]), near the NBRO instrument (0.446),
inside the literature bracket [0.15, 0.50). The shipped 0.244 was below its own floor in
nine months of twelve and is now retired.

**Nothing else moves.** T-lock holds exactly: basin means 19.752 / 19.092 / 17.079 / 18.755 /
21.038 are unchanged, as are exposure and burden. Only the partition label changes — from
~25/75 to **~48/52**. Exporter QA PASS 0.0015; 18 invariant tests pass.

**🔴 The cost, stated plainly.** The wet/dry background ratio moves to **0.388** against an
observed reference of 0.53, and F.18 rejected a rebuild at 0.349 on exactly this gate. This
is the four-constraints-on-three-degrees-of-freedom problem resolving, and it is resolved in
favour of physics for a stated reason: the reviewer's constraint is **absolute**, whereas
W2's 0.53 is by our own record *"the softest line — inferred from FECT totals by origin, and
that inference itself assumes a local share, so a larger true f biases it."* **A reference
derived under an assumed f cannot adjudicate against changing f.** W2 is therefore
reclassified from a gate to a diagnostic, and the tension is disclosed rather than hidden.

**This supersedes the standing rule against a sixth background reformulation.** That rule was
written to stop re-deriving the background's *level* by fiat. This is not that: it imposes a
physical constraint the construction was violating, with the free parameter shown to be
inconsequential.
