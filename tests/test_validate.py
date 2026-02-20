import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from validate import DataValidationError, validate  # noqa: E402


def good_df():
    return pd.DataFrame({
        "customer_id": [1, 2, 3, 4],
        "tenure_months": [1.0, 12.0, 24.0, 36.0],
        "monthly_charges": [90.0, 60.0, 55.0, 40.0],
        "support_tickets": [5, 2, 1, 0],
        "churned": [1, 0, 0, 0],
    })


def test_good_data_passes():
    validate(good_df())


def test_missing_column_fails():
    df = good_df().drop(columns=["support_tickets"])
    with pytest.raises(DataValidationError):
        validate(df)


def test_mostly_empty_feature_fails():
    df = good_df()
    df.loc[:, "tenure_months"] = np.nan
    with pytest.raises(DataValidationError):
        validate(df)
