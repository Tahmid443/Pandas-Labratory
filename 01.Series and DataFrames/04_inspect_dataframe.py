"""Inspect a DataFrame: head, tail, info, describe, shape."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "id": range(10),
        "value": [i * 1.5 for i in range(10)],
        "label": ["a", "b"] * 5,
    })
    print("head:\n", df.head(3))
    print("\ntail:\n", df.tail(2))
    print("\nshape:", df.shape)
    print("\ninfo:")
    df.info()
    print("\ndescribe:\n", df.describe(include="all"))

if __name__ == "__main__":
    main()