# Pandas Interview Questions

1. **loc vs iloc** — label-based vs positional indexing.
2. **apply vs vectorized ops** — vectorized is faster; prefer it.
3. **transform vs aggregate** — transform returns same-shape output;
   aggregate collapses groups.
4. **How do you avoid SettingWithCopyWarning?** Use `.loc` or `.copy()`.
5. **How do you handle missing values?** `isna`, `dropna`, `fillna`,
   imputation strategies.
6. **How do you detect leakage?** Split first, fit only on train, audit
   correlations with target.
7. **How do you optimize a large DataFrame?** Downcast dtypes, use `category`,
   chunked reads, vectorized ops.
8. **How do you merge safely?** Use `validate=` to assert cardinality.
9. **How do you resample time series?** `df.resample("M").sum()` on a
   DatetimeIndex.
10. **What is the difference between `concat` and `merge`?** `concat` stacks or
    aligns by axis; `merge` joins on keys.