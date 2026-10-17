"""Mixed data-cleaning mini-challenge."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "id": [1, 2, 2, 3],
        "date": ["2024-01-01", "2024-02-01", "2024-02-01", "not a date"],
        "value": ["10", "20", None, "40"],
        "cat": ["A", "B", "B", None],
    })
    df = df.drop_duplicates(subset="id")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce").fillna(0)
    df["cat"] = df["cat"].fillna("unknown")
    print(df)
    print("\ndtypes:\n", df.dtypes)

if __name__ == "__main__":
    main()