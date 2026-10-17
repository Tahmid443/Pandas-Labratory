"""Check a column is a unique key."""
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, 1, 2]})
    is_unique = not df["id"].duplicated().any()
    print("is_unique:", is_unique)
    print("duplicate ids:\n", df[df["id"].duplicated(keep=False)])

if __name__ == "__main__":
    main()