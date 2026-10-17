"""Cap (winsorize) outliers using IQR bounds."""
import pandas as pd

def main():
    df = pd.DataFrame({"value": [10, 12, 11, 13, 12, 11, 100]})
    q1, q3 = df["value"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["capped"] = df["value"].clip(lo, hi)
    print(df)

if __name__ == "__main__":
    main()