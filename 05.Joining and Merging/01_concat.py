"""Concatenate DataFrames vertically and horizontally."""
import pandas as pd

def main():
    df1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df2 = pd.DataFrame({"a": [5, 6], "b": [7, 8]})
    print("vertical concat:\n", pd.concat([df1, df2], ignore_index=True))

    df3 = pd.DataFrame({"c": [9, 10]})
    print("\nhorizontal concat:\n", pd.concat([df1, df3], axis=1))

if __name__ == "__main__":
    main()