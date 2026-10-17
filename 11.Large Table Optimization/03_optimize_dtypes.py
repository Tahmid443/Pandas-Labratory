"""Downcast numeric dtypes to save memory."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "i": np.arange(1000),
        "f": np.random.rand(1000),
    })
    print("original:\n", df.dtypes)

    df["i"] = pd.to_numeric(df["i"], downcast="integer")
    df["f"] = pd.to_numeric(df["f"], downcast="float")
    print("\noptimized:\n", df.dtypes)

if __name__ == "__main__":
    main()