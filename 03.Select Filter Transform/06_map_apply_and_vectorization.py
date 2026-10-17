"""Compare map, apply, and vectorized operations."""
import numpy as np
import pandas as pd

def main():
    s = pd.Series([1, 2, 3, 4])

    print("map (x*10):\n", s.map(lambda x: x * 10))
    print("\napply (x**2):\n", s.apply(lambda x: x ** 2))
    print("\nvectorized (s * 3):\n", s * 3)

    mapping = {1: "one", 2: "two", 3: "three", 4: "four"}
    print("\nmap with dict:\n", s.map(mapping))

    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    print("\nDataFrame.apply sum per column:\n", df.apply(np.sum))

if __name__ == "__main__":
    main()