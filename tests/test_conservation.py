"""The pattern multiplying T(t) must have unit spatial mean at every hour, or the field drifts off T(t)."""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kandymodel.assemble.decomp_map import unit_mean_pattern  # noqa: E402


def test_unit_mean_pattern():
    rng = np.random.default_rng(0)
    c = rng.normal(size=256); c = (c - c.mean()) / c.std()
    S = 1.0 + 0.3 * c + 0.05 * rng.normal(size=256); S = S / S.mean()   # covaries with c, as on the valley floor
    w = rng.uniform(0, 1, size=500)
    SM = unit_mean_pattern(S[None, :], c[None, :], 0.15, w)
    assert np.abs(SM.mean(axis=1) - 1.0).max() < 1e-6
