"""Remove duplicate rows."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "a": [1, 1, 2, 3, 3],
        "b": ["x", "x", "y", "z", "z"],
    })
    print("original:\n", df)
    print("\ndrop_duplicates:\n", df.drop_duplicates())
    print("\ndrop_duplicates keep='last':\n", df.drop_duplicates(keep="last"))
    print("\nsubset ['a']:\n", df.drop_duplicates(subset=["a"]))

if __name__ == "__main__":
    main()