"""Filter rows by date ranges."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "ts": pd.to_datetime([
            "2024-01-01", "2024-01-15", "2024-02-01", "2024-02-15"
        ]),
        "v": [1, 2, 3, 4],
    })
    mask = (df["ts"] >= "2024-01-10") & (df["ts"] < "2024-02-01")
    print(df[mask])

if __name__ == "__main__":
    main()