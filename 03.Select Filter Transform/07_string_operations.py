"""Vectorized string methods via .str accessor."""
import pandas as pd

def main():
    s = pd.Series(["  Alpha ", "beta", "GAMMA", None])
    print("upper:\n", s.str.upper())
    print("\nstrip:\n", s.str.strip())
    print("\nlower + contains 'a':\n", s.str.lower().str.contains("a", na=False))
    print("\nreplace:\n", s.str.replace("a", "@", regex=False))
    print("\nsplit:\n", s.str.split("a"))

if __name__ == "__main__":
    main()