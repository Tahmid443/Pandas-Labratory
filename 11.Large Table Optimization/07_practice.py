"""Practice: optimize a wide-ish DataFrame."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "id": np.arange(100_000),
        "cat": np.random.choice(["a", "b", "c"], 100_000),
        "val": np.random.rand(100_000),
    })
    before = df.memory_usage(deep=True).sum()
    df["id"] = pd.to_numeric(df["id"], downcast="integer")
    df["cat"] = df["cat"].astype("category")
    df["val"] = pd.to_numeric(df["val"], downcast="float")
    after = df.memory_usage(deep=True).sum()
    print(f"before={before/1e6:.2f}MB  after={after/1e6:.2f}MB")

if __name__ == "__main__":
    main()