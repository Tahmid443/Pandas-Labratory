"""Practice: combined missing-value handling."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "age": [25.0, np.nan, 40.0, np.nan],
        "city": ["A", None, "B", "A"],
        "score": [90.0, 85.0, np.nan, 70.0],
    })
    df["age"] = df["age"].fillna(df["age"].median())
    df["city"] = df["city"].fillna("unknown")
    df["score"] = df["score"].fillna(df["score"].mean())
    print(df)
    print("\nremaining missing:", df.isna().sum().sum())

if __name__ == "__main__":
    main()