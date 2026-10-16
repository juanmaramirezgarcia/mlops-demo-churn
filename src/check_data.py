"""Run the data validation rules on the training extract. Exit code 1 stops the pipeline."""
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate import DataValidationError, validate  # noqa: E402

path = Path(__file__).resolve().parents[1] / "data" / "churn_sample.csv"
df = pd.read_csv(path)
try:
    validate(df)
except DataValidationError as err:
    print(f"DATA VALIDATION FAILED: {err}")
    sys.exit(1)
print(f"Data validation passed: {len(df)} rows, {df.shape[1]} columns, no missing columns, no mostly-empty features.")
