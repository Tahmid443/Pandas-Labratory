"""Fit a Pipeline on train only, then transform test."""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def main():
    train = pd.DataFrame({"x": [1.0, np.nan, 3.0]})
    test = pd.DataFrame({"x": [np.nan, 10.0]})

    pipe = Pipeline([("imp", SimpleImputer(strategy="mean"))]).fit(train)
    print("train transformed:\n", pipe.transform(train))
    print("test transformed:\n", pipe.transform(test))

if __name__ == "__main__":
    main()