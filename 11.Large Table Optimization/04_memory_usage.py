"""Report per-column memory usage."""
import numpy as np
import pandas as pd

def main():
    df = pd.DataFrame({
        "i": np.arange(1000),
        "s": ["label"] * 1000,
        "f": np.random.rand(1000),
    })
    print(df.memory_usage(deep=True))
    print("\ntotal MB:", df.memory_usage(deep=True).sum() / 1e6)

if __name__ == "__main__":
    main()