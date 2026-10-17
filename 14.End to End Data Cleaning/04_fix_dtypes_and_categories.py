"""Step 4: fix dtypes and use categorical."""
import io
import pandas as pd

RAW_CSV = """id,name,dept,salary,start_date
1, ann,HR,50000,2024-01-01
2,bob,IT,,2024-02-01
3, cy,IT,72000,not a date
4,dan,HR,48000,2024-03-01
"""

def main():
    df = pd.read_csv(io.StringIO(RAW_CSV))
    df["name"] = df["name"].str.strip()
    df["dept"] = df["dept"].astype("category")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
    df["start_date"] = pd.to_datetime(df["start_date"], errors="coerce")
    print(df)
    print("\ndtypes:\n", df.dtypes)

if __name__ == "__main__":
    main()