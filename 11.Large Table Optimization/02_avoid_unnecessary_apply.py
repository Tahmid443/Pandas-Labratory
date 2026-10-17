"""Demonstrate replacing apply with vectorized logic."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({"a": np.arange(10), "b": np.arange(10) * 2})
    slow = df.apply(lambda row: row["a"] + row["b"], axis=1)
    fast = df["a"] + df["b"]
    print("apply result:\n", slow.values)
    print("vectorized result:\n", fast.values)

if __name__ == "__main__":
    main()