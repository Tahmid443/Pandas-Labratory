"""Step 1: load and inspect synthetic raw data."""
import io
import pandas as pd

RAW_CSV = """id,name,dept,salary,start_date
1, ann,HR,50000,2024-01-01
2,bob,IT,,2024-02-01
3, cy,IT,72000,not a date
4,dan,HR,48000,2024-03-01
4,dan,HR,48000,2024-03-01
"""

def load():
    return pd.read_csv(io.StringIO(RAW_CSV))

def main():
    df = load()
    print(df)
    print("\ninfo:")
    df.info()
    print("\nmissing:\n", df.isna().sum())

if __name__ == "__main__":
    main()