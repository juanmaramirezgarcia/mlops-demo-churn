"""Data validation: stop the pipeline before training if the data is not what we expect."""
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "tenure_months", "monthly_charges", "support_tickets",
                    "promo_weeks_last_quarter", "churned"]


class DataValidationError(Exception):
    """Raised when the incoming data does not match the expected schema."""


def validate(df: pd.DataFrame) -> None:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise DataValidationError(f"Missing required columns: {missing}")
    if len(df) == 0:
        raise DataValidationError("Dataset is empty")

    # Empty numeric values used to be filled with 0 downstream, which the model
    # read as "a customer with zero months of tenure". Reject them instead.
    numeric = ["tenure_months", "monthly_charges", "support_tickets", "promo_weeks_last_quarter"]
    empty_share = df[numeric].isna().mean()
    too_empty = empty_share[empty_share > 0.05]
    if not too_empty.empty:
        raise DataValidationError(
            f"More than 5% empty values in: {too_empty.index.tolist()} "
            f"({too_empty.round(2).to_dict()}). Check the upstream extract."
        )
