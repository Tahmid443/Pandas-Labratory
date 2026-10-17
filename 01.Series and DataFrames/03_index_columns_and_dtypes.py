"""Inspect and set index, columns, and dtypes."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"], "c": [1.5, 2.5, 3.5]})
    print("Original:\n", df)
    print("columns:", list(df.columns))
    print("index:", list(df.index))
    print("dtypes:\n", df.dtypes)

    df = df.set_index("a")
    print("\nAfter set_index('a'):\n", df)

    df["b"] = df["b"].astype("category")
    df["c"] = df["c"].astype("float32")
    print("\nAfter dtype changes:\n", df.dtypes)

if __name__ == "__main__":
    main()