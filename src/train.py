"""Train the churn model and save it to models/churn.pkl.  Run from the repo root: python src/train.py"""
import pickle
import sys
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from validate import validate  # noqa: E402

FEATURES = ["tenure_months", "monthly_charges", "support_tickets"]


def load_data(path: Path = ROOT / "data" / "churn_sample.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def train(df: pd.DataFrame) -> LogisticRegression:
    model = LogisticRegression(max_iter=500)
    model.fit(df[FEATURES], df["churned"])
    return model


if __name__ == "__main__":
    df = load_data()
    validate(df)
    model = train(df)
    (ROOT / "models").mkdir(exist_ok=True)
    with open(ROOT / "models" / "churn.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Model trained on", len(df), "customers")
