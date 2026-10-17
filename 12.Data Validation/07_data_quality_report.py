"""Build a small data-quality report."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "id": [1, 2, None, 4],
        "score": [90, 85, None, 120],
        "cat": ["a", "b", "a", None],
    })
    report = pd.DataFrame({
        "nulls": df.isna().sum(),
        "null_pct": df.isna().mean().round(2),
        "n_unique": df.nunique(),
        "dtype": df.dtypes.astype(str),
    })
    print(report)

if __name__ == "__main__":
    main()