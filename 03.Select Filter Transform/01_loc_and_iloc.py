"""Label-based loc vs position-based iloc."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, index=["x", "y", "z"])
    print(df)
    print("\nloc['y']:\n", df.loc["y"])
    print("\nloc['y', 'b']:", df.loc["y", "b"])
    print("\niloc[0]:\n", df.iloc[0])
    print("\niloc[0, 1]:", df.iloc[0, 1])
    print("\nloc['x':'y']:\n", df.loc["x":"y"])

if __name__ == "__main__":
    main()