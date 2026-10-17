"""Assertion-based validation."""
import pandas as pd

def main():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [0.0, 1.0, 2.0]})
    assert df["x"].between(0, 10).all(), "x out of range"
    assert (df["y"] >= 0).all(), "y must be nonnegative"
    assert df["x"].is_monotonic_increasing, "x not sorted"
    print("all assertions passed")

if __name__ == "__main__":
    main()