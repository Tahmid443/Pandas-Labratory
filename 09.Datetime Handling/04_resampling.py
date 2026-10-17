"""Resample a time series to daily / weekly frequency."""
import pandas as pd

def main():
    idx = pd.date_range("2024-01-01", periods=10, freq="h")
    s = pd.Series(range(10), index=idx)
    print("hourly:\n", s)
    print("\ndaily sum:\n", s.resample("D").sum())
    print("\nweekly sum:\n", s.resample("W").sum())

if __name__ == "__main__":
    main()