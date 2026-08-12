# Data

This directory holds the inputs `scripts/regenerate_all.py` needs, so a fresh clone can
rebuild the Kandy field end to end without hunting for anything. About 8 MB.

Everything here is a **derived product** — a processed grid or a model intermediate — not a
third-party raw observation. That distinction is deliberate and is explained below.

## What is here

| path | what it is | derived from |
|---|---|---|
| `raw/geos_cf/kandy_geos_cf_*.csv` | hourly chemistry prior over the basin, 2019–2025 | NASA GEOS-CF |
| `processed/stage1_v3/T_anchor/T_kandy_hourly_*.parquet` | the temporal anchor `T(t)`, three quantiles | this model |
| `processed/stage1_v3/vandonkelaar_kandy_annual.csv` | annual basin level per year | ACAG/van Donkelaar V6.GL02.04 |
| `processed/decomp/B_background_hourly_*_v2.parquet` | the regional background `B(t)` | this model |
| `processed/decomp/S_emit_kandy.npz` | satellite emission surface | van Donkelaar V6.GL02.04 |
| `processed/decomp/S_traffic_kandy.npz` | congestion-weighted traffic emission surface | OpenStreetMap road graph |
| `processed/decomp/M_confinement_kandy.npz` | terrain confinement factor | SRTM |
| `processed/decomp/population_kandy.npz` | population grid | WorldPop |
| `processed/pinn_inputs/kandy_windninja_library.npz` | mass-consistent diagnostic wind library | WindNinja over SRTM |
| `processed/pinn_inputs/kandy_terrain_*.npz`, `kandy_elev_grid_100m.npz` | terrain descriptors | SRTM |

Run `python scripts/regenerate_all.py` and the outputs land under
`data/processed/decomp/` and `results/figures/`. Those outputs are about 1 GB and are not
tracked; they are reproduced from what is here.

## What is deliberately NOT here, and why

**Ground-sensor observations are not redistributed.** The two local low-cost sensors are
third-party research instruments, and the analogue-city validation data belong to national
and municipal monitoring networks under their own terms. Publishing someone else's raw
measurements is not ours to do, however freely we were able to read them.

The model intermediates derived from those measurements — the anchor `T(t)` above — *are*
published, because they are this project's own output. So the field is fully reproducible;
re-deriving the anchor from scratch requires obtaining the sensor data at source.

Sources, all publicly reachable: OpenAQ (`openaq.org`), the CNEMC archive for the Chinese
cities, SIATA for Medellín, Air4Thai for Chiang Mai, and AirNow for the Colombo reference.
The Kandy sensors are operated by FECT and are not a public series.

**Reanalysis and satellite inputs are not mirrored either**, beyond the GEOS-CF extract
above — ERA5, ERA5-Land, GPM IMERG, MODIS, TROPOMI and VIIRS are all large, versioned, and
better fetched from their own archives than copied here. The scripts that pull them are in
`scripts/`, and the exact products and periods are listed in the technical reference.

## Attribution

If you use these grids, cite the upstream sources as well as this work:

- **van Donkelaar et al.**, ACAG surface PM2.5 V6.GL02.04 — the annual level anchor and `S_emit`
- **NASA GMAO GEOS-CF** — the chemistry prior
- **OpenStreetMap contributors** — the road graph behind `S_traffic`, ODbL
- **NASA SRTM** — terrain
- **WorldPop** — population, CC-BY
- **WindNinja** (USFS Missoula Fire Sciences Laboratory) — the diagnostic wind solver

## A note on the licence

The code in this repository is MIT. That covers the code and this project's own derived
products. It does not and cannot re-license the upstream data, which carries the terms of
each source above.
