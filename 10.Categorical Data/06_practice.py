"""Practice: bucket numeric values into categories."""
import pandas as pd

def main():
    df = pd.DataFrame({"amount": [5, 50, 500, 5000]})
    df["bucket"] = pd.cut(
        df["amount"],
        bins=[0, 10, 100, 1000, float("inf")],
        labels=["tiny", "small", "medium", "large"],
        include_lowest=True,
    )
    print(df)
    print("\ndtype:", df["bucket"].dtype)

if __name__ == "__main__":
    main()