"""Join on index."""
import pandas as pd

def main():
    left = pd.DataFrame({"score": [90, 85]}, index=["ann", "bob"])
    right = pd.DataFrame({"grade": ["A", "B"]}, index=["ann", "bob"])
    print(left.join(right))
    print("\njoin with how='outer':\n",
          left.join(right, how="outer"))

if __name__ == "__main__":
    main()