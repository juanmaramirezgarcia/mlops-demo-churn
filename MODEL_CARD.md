# Model card — churn model

| | |
|---|---|
| **Version** | 1.0 |
| **Trained on** | data/churn_sample.csv, extract of 1 March 2026 |
| **Algorithm** | Logistic regression, 3 features |
| **Accuracy (hold-out)** | 0.91 |
| **Owner (accountable)** | Product owner, Customer Retention |
| **Maintainer (responsible)** | ML engineer, Data Platform team |
| **Monitoring** | Weekly: share of empty features, churn rate vs. prediction |
| **Retrain trigger** | Accuracy below 0.85 on the monthly labelled sample |
