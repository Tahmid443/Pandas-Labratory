"""Practice: multi-key groupby with named aggregation."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "region": ["E", "E", "W", "W", "E"],
        "product": ["A", "B", "A", "B", "A"],
        "sales": [10, 20, 15, 25, 12],
    })
    out = df.groupby(["region", "product"]).agg(
        total=("sales", "sum"),
        avg=("sales", "mean"),
        n=("sales", "size"),
    )
    print(out)

if __name__ == "__main__":
    main()