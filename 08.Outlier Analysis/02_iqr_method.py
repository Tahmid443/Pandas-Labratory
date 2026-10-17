"""Outlier detection with the IQR rule."""
import pandas as pd

def main():
    s = pd.Series([10, 12, 11, 13, 12, 11, 100])
    q1, q3 = s.quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    print(f"Q1={q1}, Q3={q3}, IQR={iqr}, bounds=({lo}, {hi})")
    print("outliers:\n", s[(s < lo) | (s > hi)])

if __name__ == "__main__":
    main()