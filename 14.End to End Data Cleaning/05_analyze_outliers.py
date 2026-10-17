"""Step 5: analyze outliers on salary."""
import io
import pandas as pd

RAW_CSV = """id,name,dept,salary
1,ann,HR,50000
2,bob,IT,60000
3,cy,IT,72000
4,dan,HR,48000
5,eve,IT,900000
"""

def main():
    df = pd.read_csv(io.StringIO(RAW_CSV))
    q1, q3 = df["salary"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["is_outlier"] = (df["salary"] < lo) | (df["salary"] > hi)
    print(df)

if __name__ == "__main__":
    main()