"""Select columns by name, list, and dtype."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2], "b": [3.0, 4.0], "c": ["x", "y"]})
    print("Single column:\n", df["a"])
    print("\nList of columns:\n", df[["a", "c"]])
    print("\nNumeric columns:\n", df.select_dtypes(include="number"))
    print("\nObject columns:\n", df.select_dtypes(include="object"))

if __name__ == "__main__":
    main()