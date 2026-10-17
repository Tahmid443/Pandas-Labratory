"""Chronological time-series split (no look-ahead)."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=10, freq="D"),
        "value": range(10),
    }).sort_values("date")

    cutoff = df["date"].iloc[7]
    train = df[df["date"] <= cutoff]
    test = df[df["date"] > cutoff]
    print("train max date:", train["date"].max())
    print("test min date: ", test["date"].min())

if __name__ == "__main__":
    main()