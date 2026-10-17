"""Outlier detection using z-scores."""
import pandas as pd

def main():
    s = pd.Series([10, 12, 11, 13, 12, 11, 100])
    z = (s - s.mean()) / s.std(ddof=0)
    print("z-scores:\n", z.round(2))
    print("\n|z| > 2:\n", s[z.abs() > 2])

if __name__ == "__main__":
    main()