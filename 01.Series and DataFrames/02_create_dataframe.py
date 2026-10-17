"""Create DataFrames from dicts, lists of dicts, and records."""
import pandas as pd

def main():
    df_dict = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    print("From dict of lists:\n", df_dict)

    df_records = pd.DataFrame([
        {"x": 1, "y": "p"},
        {"x": 2, "y": "q"},
    ])
    print("\nFrom list of dicts:\n", df_records)

    df_columns = pd.DataFrame([[1, 2], [3, 4]], columns=["c1", "c2"])
    print("\nFrom 2D list with columns:\n", df_columns)

if __name__ == "__main__":
    main()