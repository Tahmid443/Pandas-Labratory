"""Complete preprocessing pipeline from raw data to model input."""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def main():
    df = pd.DataFrame({
        "age": [25, np.nan, 40, 50, 33, 28],
        "city": ["A", "B", "A", "C", "B", None],
        "target": [0, 1, 0, 1, 0, 1],
    })
    X = df.drop(columns="target")
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=0, stratify=y
    )

    num_pipe = Pipeline([
        ("imp", SimpleImputer(strategy="median")),
        ("scale", StandardScaler()),
    ])
    cat_pipe = Pipeline([
        ("imp", SimpleImputer(strategy="most_frequent")),
        ("ohe", OneHotEncoder(handle_unknown="ignore")),
    ])
    pre = ColumnTransformer([
        ("num", num_pipe, ["age"]),
        ("cat", cat_pipe, ["city"]),
    ]).fit(X_train)

    print("train transformed:\n", pre.transform(X_train))
    print("test transformed:\n", pre.transform(X_test))

if __name__ == "__main__":
    main()