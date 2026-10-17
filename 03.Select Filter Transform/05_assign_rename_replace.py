"""assign, rename, and replace."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "x"]})
    df2 = df.assign(c=df["a"] * 2, d=lambda d: d["a"] + 1)
    print("assign:\n", df2)

    df3 = df.rename(columns={"a": "alpha", "b": "beta"})
    print("\nrename:\n", df3)

    df4 = df.replace({"x": "X", 1: 100})
    print("\nreplace:\n", df4)

if __name__ == "__main__":
    main()