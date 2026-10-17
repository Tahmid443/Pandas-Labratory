"""Split BEFORE computing any statistics from the full data."""
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.DataFrame({
        "x": range(10),
        "y": [0, 1] * 5,
    })
    train, test = train_test_split(df, test_size=0.3, random_state=0)
    train_mean = train["x"].mean()
    print("train mean:", train_mean)
    print("train x filled:\n", train["x"].fillna(train_mean))
    print("test x filled with train mean:\n", test["x"].fillna(train_mean))

if __name__ == "__main__":
    main()