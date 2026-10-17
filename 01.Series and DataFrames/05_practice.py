"""Practice: build a small DataFrame and inspect it."""
import pandas as pd

def main():
    data = {
        "product": ["apple", "banana", "cherry", "date"],
        "price": [1.2, 0.5, 3.0, 2.2],
        "qty": [10, 20, 5, 7],
    }
    df = pd.DataFrame(data)
    df["total"] = df["price"] * df["qty"]
    print(df)
    print("\nTotal revenue:", df["total"].sum())
    print("Cheapest product:", df.loc[df["price"].idxmin(), "product"])

if __name__ == "__main__":
    main()