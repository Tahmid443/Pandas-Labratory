"""Validate merge cardinality to catch unexpected duplication."""
import pandas as pd

def main():
    left = pd.DataFrame({"id": [1, 2, 3], "name": ["ann", "bob", "cy"]})
    right = pd.DataFrame({"id": [1, 2, 3], "score": [90, 85, 77]})

    # one-to-one
    ok = pd.merge(left, right, on="id", validate="one_to_one")
    print("one_to_one OK:\n", ok)

    # introduce duplicate key on right
    right_dup = pd.DataFrame({"id": [1, 1, 2], "score": [90, 91, 85]})
    try:
        pd.merge(left, right_dup, on="id", validate="one_to_one")
    except pd.errors.MergeError as e:
        print("\nCaught expected error:", e)

    # one-to-many
    print("\none_to_many:\n", pd.merge(left, right_dup, on="id", validate="one_to_many"))

if __name__ == "__main__":
    main()