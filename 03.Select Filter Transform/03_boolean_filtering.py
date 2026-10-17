"""Filter rows with boolean masks."""
import pandas as pd

def main():
    df = pd.DataFrame({"name": ["ann", "bob", "cy", "dan"], "score": [90, 85, 77, 95]})
    mask = df["score"] >= 85
    print("mask:\n", mask)
    print("\nfiltered:\n", df[mask])
    print("\ncombined (&):\n", df[(df["score"] >= 80) & (df["name"] != "bob")])
    print("\nisin:\n", df[df["name"].isin(["ann", "cy"])])

if __name__ == "__main__":
    main()