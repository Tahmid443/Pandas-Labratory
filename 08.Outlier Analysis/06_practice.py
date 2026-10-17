"""Practice: flag and treat outliers per group."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "team": ["X", "X", "X", "Y", "Y", "Y"],
        "score": [1, 2, 3, 10, 11, 100],
    })

    def bounds(s):
        q1, q3 = s.quantile([0.25, 0.75])
        iqr = q3 - q1
        return q1 - 1.5 * iqr, q3 + 1.5 * iqr

    df["lo"] = df.groupby("team")["score"].transform(lambda s: bounds(s)[0])
    df["hi"] = df.groupby("team")["score"].transform(lambda s: bounds(s)[1])
    df["is_outlier"] = (df["score"] < df["lo"]) | (df["score"] > df["hi"])
    print(df)

if __name__ == "__main__":
    main()