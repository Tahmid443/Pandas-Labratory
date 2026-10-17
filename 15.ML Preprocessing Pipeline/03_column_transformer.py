"""ColumnTransformer example."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def main():
    df = pd.DataFrame({
        "num": [1.0, 2.0, 3.0],
        "cat": ["a", "b", "a"],
    })
    ct = ColumnTransformer([
        ("num", StandardScaler(), ["num"]),
        ("cat", OneHotEncoder(), ["cat"]),
    ])
    out = ct.fit_transform(df)
    print(out)

if __name__ == "__main__":
    main()