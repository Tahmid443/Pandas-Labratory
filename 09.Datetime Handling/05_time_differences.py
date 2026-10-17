"""Compute time differences between timestamps."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "start": pd.to_datetime(["2024-01-01", "2024-01-10"]),
        "end": pd.to_datetime(["2024-01-05", "2024-01-15"]),
    })
    df["days"] = (df["end"] - df["start"]).dt.days
    print(df)

if __name__ == "__main__":
    main()