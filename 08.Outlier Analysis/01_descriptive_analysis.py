"""Describe numeric data and inspect quantiles."""
import numpy as np
import pandas as pd

def main():
    np.random.seed(0)
    s = pd.Series(np.random.normal(0, 1, 100))
    print("describe:\n", s.describe())
    print("\nquantiles:\n", s.quantile([0.05, 0.25, 0.5, 0.75, 0.95]))

if __name__ == "__main__":
    main()