"""Fill missing values with a constant."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "a": [1, None, 3],
        "b": [np.nan, "x", "y"],
    })
    print("original:\n", df)
    print("\nfillna(0):\n", df.fillna(0))
    print("\nfillna per column:\n", df.fillna({"a": -1, "b": "missing"}))

if __name__ == "__main__":
    main()