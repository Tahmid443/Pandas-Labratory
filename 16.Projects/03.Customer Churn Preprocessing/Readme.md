# Project 3 — Customer Churn Preprocessing

**Goal:** Build a leakage-safe preprocessing pipeline for a churn dataset.

**Suggested steps:**
1. Separate features and target (`churn`).
2. Stratified train/validation/test split.
3. Impute + one-hot encode + scale inside a `ColumnTransformer`.
4. Fit on train only, transform validation/test.
5. Save the fitted pipeline for reuse.

**Deliverables:** fitted `Pipeline` + transformed matrices.