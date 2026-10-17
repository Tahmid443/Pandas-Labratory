"""Practice: monthly revenue with gaps filled."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "ts": pd.to_datetime(["2024-01-05", "2024-01-20", "2024-03-10"]),
        "amount": [100, 150, 200],
    }).set_index("ts")
    monthly = df["amount"].resample("ME").sum().fillna(0)
    print(monthly)

if __name__ == "__main__":
    main()