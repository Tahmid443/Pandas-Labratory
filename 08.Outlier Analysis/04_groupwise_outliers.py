"""Detect outliers within each group."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "group": ["A", "A", "A", "B", "B", "B"],
        "value": [10, 11, 12, 100, 102, 101],
    })
    def zscore(s):
        return (s - s.mean()) / s.std(ddof=0) if s.std(ddof=0) else s * 0
    df["z"] = df.groupby("group")["value"].transform(zscore)
    df["outlier"] = df["z"].abs() > 1.5
    print(df)

if __name__ == "__main__":
    main()