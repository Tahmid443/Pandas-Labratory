"""Drop rows/columns with missing values."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [None, "x", "y"],
        "c": ["p", "q", None],
    })
    print("original:\n", df)
    print("\ndropna (any):\n", df.dropna())
    print("\ndropna (how='all'):\n", df.dropna(how="all"))
    print("\ndropna (axis=1, subset=['a','b']):\n",
          df.dropna(axis=1, subset=["a", "b"]))
    print("\ndropna (thresh=2):\n", df.dropna(thresh=2))

if __name__ == "__main__":
    main()