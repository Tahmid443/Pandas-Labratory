"""Step 7: export to CSV / JSON (in-memory for demo)."""
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
    csv_out = df.to_csv(index=False)
    json_out = df.to_json(orient="records", date_format="iso")
    print("CSV length:", len(csv_out))
    print("JSON length:", len(json_out))
    print("\nfirst 2 CSV lines:")
    print("\n".join(csv_out.splitlines()[:2]))

if __name__ == "__main__":
    main()