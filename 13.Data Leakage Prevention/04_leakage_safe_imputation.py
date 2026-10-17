"""Leakage-safe imputation: fit median on train only."""
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.DataFrame({"x": [1.0, None, 3.0, 4.0, None, 6.0], "y": [0, 1, 0, 1, 0, 1]})
    train, test = train_test_split(df, test_size=0.33, random_state=0)
    median = train["x"].median()
    print("train median:", median)
    print("train filled:\n", train.assign(x=train["x"].fillna(median)))
    print("test filled:\n", test.assign(x=test["x"].fillna(median)))

if __name__ == "__main__":
    main()