"""Ordinal encode an ordered categorical column."""
import pandas as pd

def main():
    s = pd.Series(
        ["medium", "low", "high"],
        dtype=pd.CategoricalDtype(categories=["low", "medium", "high"], ordered=True),
    )
    codes = s.cat.codes
    print("values:\n", s)
    print("codes:\n", codes)

if __name__ == "__main__":
    main()