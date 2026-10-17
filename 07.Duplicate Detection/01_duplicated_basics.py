"""Detect duplicate rows."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "a": [1, 1, 2, 3],
        "b": ["x", "x", "y", "z"],
    })
    print(df)
    print("\nduplicated:\n", df.duplicated())
    print("\nduplicated (keep=False):\n", df.duplicated(keep=False))

if __name__ == "__main__":
    main()