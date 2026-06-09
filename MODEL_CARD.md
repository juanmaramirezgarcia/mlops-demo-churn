# Model card — churn model

| | |
|---|---|
| **Version** | 1.1 |
| **Trained on** | data/churn_sample.csv, extract of 1 June 2026 |
| **Algorithm** | Logistic regression, 4 features (adds promotions) |
| **Accuracy (hold-out)** | 0.93 |
| **Owner (accountable)** | Product owner, Customer Retention |
| **Maintainer (responsible)** | ML engineer, Data Platform team |
| **Monitoring** | Weekly: share of empty features, churn rate vs. prediction |
| **Retrain trigger** | Accuracy below 0.85 on the monthly labelled sample |
