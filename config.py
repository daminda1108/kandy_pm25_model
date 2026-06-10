"""
config.py — Central configuration for the Kandy PM2.5 additive-decomposition model.
Canonical constants, study-area coordinates, paths, and download settings live here;
import this module rather than restating any value. The package reads only a handful
of these (KANDY_CENTRE_LAT/LON, KANDY_PINN_BBOX, KOALA_ANCHOR_UG_M3); the remaining
download / model-default constants are retained for provenance.
"""

from pathlib import Path

# ─────────────────────────────────────────────
# GOOGLE EARTH ENGINE
# ─────────────────────────────────────────────

GEE_PROJECT = "kandypinn"

# ─────────────────────────────────────────────
# CANONICAL CONSTANTS — single source of truth (added 2026-05-08 per audit §6.2)
# These values are referenced by paper drafts, kernel scripts, and validation
# routines. If a downstream file disagrees with the value here, the downstream
# file is wrong. Update this block, never restate the values elsewhere.
# ─────────────────────────────────────────────

# KOALA PM2.5 anchor (Senarathna et al. 2024, CJS 53(2):197–206)
# 12-month low-cost-sensor campaign, n=12 monthly aggregates, multi-sensor.
# Reported annual mean ± 17.5% bound → [20.2, 28.8] µg/m³.
# NOTE (2026-06-04 area-vs-floor correction): this is a valley-FLOOR / near-core
# level — the KOALA/NIFS monitor (7.2839 N, 80.6322 E) sits ~27 m above the local
# valley floor, ~0.7 km S of Kandy lake. It is NOT the basin AREA mean (that is the
# VanD basin reading ~19.7, corroborated by GHAP ~17). The decomposition level
# anchor uses VanD's area mean directly (β≡1); KOALA is reproduced at the NIFS pixel
# by the confinement field, not forced. See features/vandonkelaar.py + gotcha #51.
KOALA_ANCHOR_UG_M3 = 24.5225

# CAMS EAC4 over Kandy, 2019 annual mean, raw (uncorrected)
CAMS_KANDY_2019_MEAN_UG_M3 = 40.98

# Stage A flat-annual bias correction factor (KOALA / CAMS_2019)
CAMS_BIAS_FACTOR_FLAT = round(KOALA_ANCHOR_UG_M3 / CAMS_KANDY_2019_MEAN_UG_M3, 4)
# = 0.5984 (used as `apply_koala_monthly_correction()` flat-annual ratio)

# GEOS-CF PM25_RH35_GCC over Kandy, annual mean over the available window
# (Jan 2018 – Apr 2026). Used as denominator for Kandy zero-shot c_prior scaling.
GEOS_CF_KANDY_MEAN_UG_M3 = 45.7

# Per-city station means and GEOS-CF means (used for Stage C residual learning).
# station_mean / geos_mean = city_ratio; c_prior_scaled = c_prior × city_ratio.
# All values verified against the Kaggle convcnp_loocv_v1 kernel and SESLOG.
STATION_CITY_MEANS_UG_M3 = {
    "medellin"     : 21.7,
    "chiangmai"    : 12.2,
    "kathmandu"    : 61.2,
    "bogota"       : 16.5,
    "mexico_city"  : 21.2,
    "kandy"        : KOALA_ANCHOR_UG_M3,   # KOALA anchor stands in for station mean
}

GEOS_CITY_MEANS_UG_M3 = {
    "medellin"     : 26.5,
    "chiangmai"    : 23.0,
    "kathmandu"    : 77.4,
    "bogota"       : 20.4,
    "mexico_city"  : 97.4,
    "kandy"        : GEOS_CF_KANDY_MEAN_UG_M3,
}

CITY_RATIOS = {
    city: round(STATION_CITY_MEANS_UG_M3[city] / GEOS_CITY_MEANS_UG_M3[city], 4)
    for city in GEOS_CITY_MEANS_UG_M3
}
# CITY_RATIOS["kandy"] == 0.5360 (locked; the Kandy zero-shot c_prior scalar)

# Convenience aliases for the most-cited values
KANDY_GEOS_CF_RATIO = CITY_RATIOS["kandy"]   # = 0.5360 (used in paper §3.2.5)

# Native data resolution at which results are reported.
# (Optional 100m presentation downscaling is labelled as such; not a model output.)
NATIVE_RESOLUTION_KM = 1.0
NATIVE_RESOLUTION_TIMESTEP = "hourly"

# Validation framing (use these labels; do not write "validation" at zero-shot targets)
ZERO_SHOT_VALIDATION_LABEL = "structural-consistency check pending field validation"

# ─────────────────────────────────────────────
# STUDY AREA
# ─────────────────────────────────────────────

# Broad bounding box for satellite data downloads (ERA5, MODIS, TROPOMI)
KANDY_BBOX = {
    "lat_min": 7.10,
    "lat_max": 7.50,
    "lon_min": 80.45,
    "lon_max": 80.85,
}

# PINN domain: 15×15 km centred on Kandy city centre
# Justified by ERA5 grid scale (~28km) — captures all sub-grid terrain
# including Hantana (SW, 7km) and Knuckles massif (NE, 18-28km)
KANDY_CENTRE_LAT = 7.2906
KANDY_CENTRE_LON = 80.6337

_HALF_DEG_LAT = 0.0676   # 7.5 km / 111.0 km per degree
_HALF_DEG_LON = 0.0677   # 7.5 km / (111.0 × cos(7.29°))

KANDY_PINN_BBOX = {
    "lat_min": round(KANDY_CENTRE_LAT - _HALF_DEG_LAT, 6),  # 7.2230°N
    "lat_max": round(KANDY_CENTRE_LAT + _HALF_DEG_LAT, 6),  # 7.3582°N
    "lon_min": round(KANDY_CENTRE_LON - _HALF_DEG_LON, 6),  # 80.5660°E
    "lon_max": round(KANDY_CENTRE_LON + _HALF_DEG_LON, 6),  # 80.7014°E
}

# Central coordinates
KANDY_CENTER = {"lat": 7.2906, "lon": 80.6337}

# ─────────────────────────────────────────────
# TIME RANGE
# ─────────────────────────────────────────────

DATA_START_YEAR  = 2000
DATA_END_YEAR    = 2025   # inclusive; 25 years of data
DATA_START_MONTH = 1
DATA_END_MONTH   = 12

# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────

ROOT_DIR = Path(__file__).parent          # kandy_pm25/
DATA_DIR = ROOT_DIR / "data"

# Raw downloads
RAW_DIR         = DATA_DIR / "raw"
MODIS_RAW_DIR   = RAW_DIR / "modis_aod"
TROPOMI_RAW_DIR = RAW_DIR / "tropomi"
ERA5_RAW_DIR    = RAW_DIR / "era5"
CAMS_RAW_DIR    = RAW_DIR / "cams"          # CAMS EAC4 PM2.5 — gap-fill + co-variate
DEM_RAW_DIR     = RAW_DIR / "dem"
LC_RAW_DIR      = RAW_DIR / "land_cover"
NDVI_RAW_DIR    = RAW_DIR / "ndvi"
GT_RAW_DIR      = RAW_DIR / "ground_truth"
MERRA2_RAW_DIR  = RAW_DIR / "merra2"          # MERRA-2 aerosol PM2.5
VAN_DONKELAAR_DIR = RAW_DIR / "van_donkelaar"  # Van Donkelaar V5.GL.04 annual PM2.5


# Processed
PROC_DIR        = DATA_DIR / "processed"
FEATURES_DIR    = PROC_DIR / "features"
MERGED_DIR      = PROC_DIR / "merged"
PINN_INPUT_DIR  = PROC_DIR / "pinn_inputs"

# Results
RESULTS_DIR     = ROOT_DIR / "results"
FIGURES_DIR     = RESULTS_DIR / "figures"
TABLES_DIR      = RESULTS_DIR / "tables"
MODELS_DIR      = RESULTS_DIR / "models"
VALIDATION_DIR  = RESULTS_DIR / "validation"

# ─────────────────────────────────────────────
# ERA5 CONFIGURATION
# ─────────────────────────────────────────────

ERA5_SINGLE_LEVEL_VARIABLES = [
    "10m_u_component_of_wind",      # u
    "10m_v_component_of_wind",      # v
    "2m_temperature",               # T2m
    "2m_dewpoint_temperature",      # Td2m → RH
    "surface_pressure",             # SP
    "total_precipitation",          # TP
    "boundary_layer_height",        # BLH  ← most critical
    "surface_solar_radiation_downwards",  # SSRD
    "total_column_water_vapour",    # TCWV
]

ERA5_PRESSURE_LEVEL_VARIABLES = [
    "temperature",                  # For 925 hPa inversion detection
    "geopotential",
]

ERA5_PRESSURE_LEVELS = ["925", "850", "700"]

# ERA5-Land at ~9 km — for better skin temperature
ERA5_LAND_VARIABLES = [
    "2m_temperature",
    "skin_temperature",
    "2m_dewpoint_temperature",
]

# ERA5 grid resolution (degrees)
ERA5_RESOLUTION = 0.25       # Single levels
ERA5_LAND_RESOLUTION = 0.1   # ERA5-Land

# ─────────────────────────────────────────────
# MODIS MAIAC AOD CONFIGURATION
# ─────────────────────────────────────────────

MODIS_PRODUCT   = "MCD19A2.061"   # MAIAC Land AOD, Collection 6.1
MODIS_AOD_BAND  = "AOD_55"        # 550 nm AOD channel
MODIS_QA_BAND   = "AOD_QA"        # Quality assurance flags
MODIS_AOD_SCALE = 0.001           # Scale factor to apply
MODIS_AOD_MIN   = 0.0             # Valid AOD range
MODIS_AOD_MAX   = 5.0

# ─────────────────────────────────────────────
# TROPOMI CONFIGURATION
# ─────────────────────────────────────────────

TROPOMI_COLLECTIONS = {
    "NO2":  "S5P_OFFL_L2__NO2____",
    "CO":   "S5P_OFFL_L2__CO_____",
    "AER_AI": "S5P_OFFL_L2__AER_AI_",
    "AER_LH": "S5P_OFFL_L2__AER_LH_",
}
TROPOMI_QA_THRESHOLD = 0.5   # Minimum QA value (0–1)

# ─────────────────────────────────────────────
# HIMAWARI-8 AHI — NOT USABLE FOR SRI LANKA
# ─────────────────────────────────────────────
# Geostationary at 140.7°E. Full disk covers ~80°E to ~160°W.
# Sri Lanka is at 80.6°E — extreme western edge, high viewing zenith angle.
# AOD retrievals unreliable at limb geometry. DO NOT USE for Kandy.
# Kept for reference only.

HIMAWARI_RAW_DIR       = RAW_DIR / "himawari"

# ─────────────────────────────────────────────
# TOPOGRAPHY FEATURE CONSTANTS
# ─────────────────────────────────────────────

# Valley depth reference — approximate depth of Kandy bowl (m)
KANDY_VALLEY_DEPTH_M = 400.0

# TPI (Topographic Position Index) search radius
TPI_RADIUS_M = 2000.0  # 2 km neighbourhood

# Katabatic Flow Proxy — slope temperature gradient threshold (°C/m)
KATABATIC_TEMP_LAPSE = 0.0065   # Dry adiabatic lapse rate (K/m)

# Thermal Inversion Index pressure level (hPa)
INVERSION_PRESSURE_LEVEL = 925  # Compare T925 vs surface

# ─────────────────────────────────────────────
# MODEL CONFIGURATION (Stage 1)
# ─────────────────────────────────────────────

XGBOOST_DEFAULT_PARAMS = {
    # Tuned via 100-trial Optuna LOMO-CV objective (2026-03-07)
    # Best mean LOMO RMSE: 4.818 µg/m³ vs 4.925 default (saved: results/models/xgboost_best_params.json)
    # Key findings: strong L1 (reg_alpha=12.4), non-zero gamma (1.98), shallow trees (depth=5)
    "n_estimators":      1184,
    "learning_rate":     0.008216557622222474,
    "max_depth":         5,
    "subsample":         0.7671508181415934,
    "colsample_bytree":  0.9104394470417163,
    "colsample_bylevel": 0.9744748155917816,
    "min_child_weight":  3,
    "gamma":             1.980599561405435,
    "reg_alpha":         12.447006316112198,
    "reg_lambda":        2.7135425208026795e-05,
    "objective":         "reg:squarederror",
    "eval_metric":       "rmse",
    "n_jobs":            -1,
    "random_state":      42,
    "early_stopping_rounds": 50,
}

LIGHTGBM_DEFAULT_PARAMS = {
    "n_estimators":     500,
    "learning_rate":    0.05,
    "num_leaves":       63,
    "max_depth":        -1,
    "subsample":        0.8,
    "colsample_bytree": 0.8,
    "min_child_samples": 20,
    "reg_alpha":        0.1,
    "reg_lambda":       1.0,
    "objective":        "regression",
    "metric":           "rmse",
    "n_jobs":           -1,
    "random_state":     42,
    "verbose":          -1,
}

RANDOM_FOREST_DEFAULT_PARAMS = {
    "n_estimators": 300,
    "max_depth":    None,
    "max_features": "sqrt",
    "min_samples_split": 5,
    "min_samples_leaf":  2,
    "n_jobs":       -1,
    "random_state": 42,
}

# Cross-validation strategy (§1.5 of design doc)
CV_FOLDS        = 5
CV_STRATEGIES   = ["temporal", "blocked_spatial", "leave_season_out"]
CV_DEFAULT      = "temporal"  # Primary; all three required for paper
TRAIN_TEST_RATIO = 0.8

# Uncertainty quantification — quantile regression (§1.6)
QUANTILE_ALPHAS = [0.05, 0.50, 0.95]  # 90% prediction intervals

# ─────────────────────────────────────────────
# PHYSICAL CONSTANTS
# ─────────────────────────────────────────────

G_MS2         = 9.81          # Gravitational acceleration (m/s²)
RD            = 287.05        # Specific gas constant for dry air (J/kg/K)
CP            = 1005.0        # Specific heat at constant pressure (J/kg/K)
KAPPA         = RD / CP       # Poisson constant
KARMAN        = 0.41          # Von Kármán constant
T0_K          = 273.15        # 0°C in Kelvin
P0_HPA        = 1013.25       # Standard sea-level pressure (hPa)

# PM2.5 reference value (µg/m³)
WHO_PM25_ANNUAL_GUIDELINE  = 5.0   # WHO 2021 guideline
WHO_PM25_24H_GUIDELINE     = 15.0  # WHO 2021 24h guideline
INDIA_NAAQS_PM25_ANNUAL    = 40.0  # NAAQS (relevant as regional comparison)

# ─────────────────────────────────────────────
# RANDOM SEED
# ─────────────────────────────────────────────

RANDOM_SEED = 42

# ─────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────

LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"
