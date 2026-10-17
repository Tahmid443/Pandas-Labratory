# Project 2 — Retail Sales Analysis

**Goal:** Merge orders, customers, and products; compute revenue by customer
segment and month.

**Suggested steps:**
1. Load three CSVs (orders, customers, products).
2. Validate merge cardinality (`validate="many_to_one"`).
3. Compute `revenue = qty * price`.
4. Resample monthly revenue.
5. Report top 5 customers by revenue.

**Deliverables:** monthly revenue table + top-customer list.