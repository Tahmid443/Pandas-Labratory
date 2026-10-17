"""Collapse rare categories into 'Other'."""
import pandas as pd

def main():
    s = pd.Series(["a"] * 90 + ["b"] * 5 + ["c"] * 3 + ["d"] * 2, dtype="category")
    counts = s.value_counts()
    rare = counts[counts < 5].index
    s2 = s.cat.add_categories(["Other"]).where(~s.isin(rare), "Other")
    s2 = s2.cat.remove_unused_categories()
    print(s2.value_counts())

if __name__ == "__main__":
    main()