"""Merge on multiple key columns."""
import pandas as pd

def main():
    left = pd.DataFrame({
        "region": ["E", "E", "W"],
        "product": ["A", "B", "A"],
        "sales": [10, 20, 15],
    })
    right = pd.DataFrame({
        "region": ["E", "E", "W"],
        "product": ["A", "B", "A"],
        "price": [1.0, 2.0, 1.5],
    })
    merged = pd.merge(left, right, on=["region", "product"], how="inner")
    merged["revenue"] = merged["sales"] * merged["price"]
    print(merged)

if __name__ == "__main__":
    main()