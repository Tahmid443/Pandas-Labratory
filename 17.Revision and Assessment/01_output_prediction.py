"""Predict the output of a small pandas snippet."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    print(df[df["a"] > 1]["b"].sum())
    # Answer: 5 + 6 = 11

if __name__ == "__main__":
    main()