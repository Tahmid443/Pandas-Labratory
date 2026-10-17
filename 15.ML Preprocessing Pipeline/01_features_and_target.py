"""Separate features and target."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "age": [25, 32, 47, 51],
        "city": ["A", "B", "A", "C"],
        "churn": [0, 1, 0, 1],
    })
    X = df.drop(columns="churn")
    y = df["churn"]
    print("X:\n", X)
    print("\ny:\n", y)

if __name__ == "__main__":
    main()