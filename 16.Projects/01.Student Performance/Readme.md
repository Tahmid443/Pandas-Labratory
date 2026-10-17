# Project 1 — Student Performance

**Goal:** Load a synthetic student dataset, clean it, and analyze relationships
between study hours, attendance, and final score.

**Suggested steps:**
1. Load the synthetic CSV (see companion code in this course, section 14).
2. Fix dtypes (`score` numeric, `date` datetime, `subject` categorical).
3. Handle missing scores with median per subject.
4. Summarize performance by subject.
5. Flag outliers (|z| > 2) and export.

**Deliverables:** cleaned CSV + a short report.