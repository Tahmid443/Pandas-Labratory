"""Final assessment: clean, validate, and export a tiny dataset."""
import io
import pandas as pd

RAW = """id,customer,amount,date,category
1,ann,100,2024-01-01,A
2,bob,,2024-01-02,B
2,bob,,2024-01-02,B
3,cy,300,not a date,A
"""

def main():
    df = pd.read_csv(io.StringIO(RAW))

    # 1. dedupe
    df = df.drop_duplicates(subset="id")

    # 2. fix dtypes
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["category"] = df["category"].astype("category")

    # 3. impute amount
    df["amount"] = df["amount"].fillna(df["amount"].median())

    # 4. validate
    assert df["id"].is_unique
    assert df["amount"].notna().all()

    # 5. export (in-memory)
    out_csv = df.to_csv(index=False)
    print(df)
    print("\nExported CSV length:", len(out_csv))

if __name__ == "__main__":
    main()