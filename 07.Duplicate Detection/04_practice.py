"""Practice: dedupe a customer table keeping most recent record."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "customer_id": [1, 1, 2, 2],
        "updated": pd.to_datetime(["2024-01-01", "2024-03-01", "2024-02-01", "2024-01-15"]),
        "status": ["active", "inactive", "active", "active"],
    })
    latest = (df.sort_values("updated")
                .drop_duplicates(subset="customer_id", keep="last"))
    print(latest)

if __name__ == "__main__":
    main()