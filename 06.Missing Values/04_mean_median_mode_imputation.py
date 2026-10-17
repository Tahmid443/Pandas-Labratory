"""Imputation with mean, median, and mode."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "num": [1.0, np.nan, 3.0, 100.0],
        "cat": ["x", None, "x", "y"],
    })
    out = df.copy()
    out["num_mean"] = out["num"].fillna(out["num"].mean())
    out["num_median"] = out["num"].fillna(out["num"].median())
    out["cat"] = out["cat"].fillna(out["cat"].mode()[0])
    print(out)

if __name__ == "__main__":
    main()