"""Step 6: validate the cleaned dataset."""
import io
import pandas as pd

CLEAN_CSV = """id,name,dept,salary,start_date
1,ann,HR,50000,2024-01-01
2,bob,IT,60000,2024-02-01
3,cy,IT,72000,2024-03-01
4,dan,HR,48000,2024-03-01
"""

def main():
    df = pd.read_csv(io.StringIO(CLEAN_CSV), parse_dates=["start_date"])
    assert df["id"].is_unique, "id not unique"
    assert df["salary"].notna().all(), "salary has nulls"
    assert df["start_date"].notna().all(), "start_date has nulls"
    assert df["salary"].between(0, 1_000_000).all(), "salary out of range"
    print("validation OK")
    print(df)

if __name__ == "__main__":
    main()