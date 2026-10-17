"""Detect obvious target leakage via correlation."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "target": [1, 0, 1, 0, 1, 0],
        "leaky": [1, 0, 1, 0, 1, 0],
        "ok":     [5, 3, 4, 2, 6, 1],
    })
    corr = df.corr()["target"].drop("target")
    print("correlation with target:\n", corr.round(2))
    print("\nsuspicious (|corr| > 0.9):\n", corr[corr.abs() > 0.9])

if __name__ == "__main__":
    main()