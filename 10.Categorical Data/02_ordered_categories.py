"""Ordered categories and comparisons."""
import pandas as pd

def main():
    s = pd.Series(
        ["low", "high", "medium", "low"],
        dtype=pd.CategoricalDtype(categories=["low", "medium", "high"], ordered=True),
    )
    print(s)
    print("\nmax:", s.max(), " min:", s.min())
    print("\n>= medium:\n", s[s >= "medium"])

if __name__ == "__main__":
    main()