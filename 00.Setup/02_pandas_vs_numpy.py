"""Contrast NumPy arrays with pandas Series/DataFrame."""
import numpy as np
import pandas as pd

def main():
    arr = np.array([10, 20, 30, 40])
    s = pd.Series(arr, index=["w", "x", "y", "z"])
    print("NumPy array:", arr)
    print("pandas Series:\n", s)
    print("Label access s['y']:", s["y"])

    df = pd.DataFrame({"name": ["ann", "bob", "cy"], "score": [90, 85, 77]})
    print("\nDataFrame:\n", df)
    print("Column mean (pandas):", df["score"].mean())
    print("Column mean (numpy):", np.mean(df["score"].to_numpy()))

if __name__ == "__main__":
    main()