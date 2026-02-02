"""Data validation: stop the pipeline before training if the data is not what we expect."""
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "tenure_months", "monthly_charges", "support_tickets", "churned"]


class DataValidationError(Exception):
    """Raised when the incoming data does not match the expected schema."""


def validate(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    if len(df) == 0:
        raise DataValidationError("Dataset is empty")
