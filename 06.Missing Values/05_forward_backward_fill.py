"""Forward fill and backward fill."""
import numpy as np
import pandas as pd

def main():
    s = pd.Series([1.0, np.nan, np.nan, 4.0, np.nan])
    print("original:\n", s.tolist())
    print("ffill:\n", s.ffill().tolist())
    print("bfill:\n", s.bfill().tolist())
    print("ffill limit=1:\n", s.ffill(limit=1).tolist())

if __name__ == "__main__":
    main()