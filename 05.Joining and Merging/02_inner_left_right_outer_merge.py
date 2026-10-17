"""All four merge join types."""
import pandas as pd

def main():
    left = pd.DataFrame({"id": [1, 2, 3], "name": ["ann", "bob", "cy"]})
    right = pd.DataFrame({"id": [2, 3, 4], "score": [85, 77, 95]})

    for how in ["inner", "left", "right", "outer"]:
        print(f"\n=== {how} ===")
        print(pd.merge(left, right, on="id", how=how))

if __name__ == "__main__":
    main()