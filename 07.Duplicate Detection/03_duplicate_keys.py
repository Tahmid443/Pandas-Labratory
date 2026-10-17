"""Find duplicate keys and report counts."""
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, 2, 2, 3, 3, 3], "val": range(6)})
    counts = df["id"].value_counts()
    dup_keys = counts[counts > 1]
    print("value counts:\n", counts)
    print("\nduplicate keys:\n", dup_keys)
    print("\nrows with duplicate ids:\n", df[df["id"].isin(dup_keys.index)])

if __name__ == "__main__":
    main()