"""Detect missing values."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [np.nan, "x", "y"],
        "c": ["p", "q", None],
    })
    print(df)
    print("\nisna:\n", df.isna())
    print("\ncount per column:\n", df.isna().sum())
    print("\nany missing per column:\n", df.isna().any())

if __name__ == "__main__":
    main()