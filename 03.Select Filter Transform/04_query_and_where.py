"""query() for filtering, where() for conditional replacement."""
import pandas as pd

def main():
    df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [10, 20, 30, 40]})
    print("query a > 2:\n", df.query("a > 2"))
    print("\nquery with variable:")
    threshold = 25
    print(df.query("b > @threshold"))

    masked = df.where(df["a"] > 2, other=0)
    print("\nwhere (a > 2 else 0):\n", masked)

if __name__ == "__main__":
    main()