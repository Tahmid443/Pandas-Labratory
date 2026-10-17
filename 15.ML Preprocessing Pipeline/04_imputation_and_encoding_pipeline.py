"""Pipeline: impute then encode."""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

def main():
    df = pd.DataFrame({
        "num": [1.0, np.nan, 3.0],
        "cat": ["a", None, "b"],
    })
    num_pipe = Pipeline([("imp", SimpleImputer(strategy="median"))])
    cat_pipe = Pipeline([
        ("imp", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder()),
    ])
    ct = ColumnTransformer([
        ("num", num_pipe, ["num"]),
        ("cat", cat_pipe, ["cat"]),
    ])
    out = ct.fit_transform(df)
    print(out)

if __name__ == "__main__":
    main()