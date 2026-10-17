"""Common aggregation functions."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "dept": ["HR", "IT", "IT", "HR", "IT"],
        "salary": [50, 70, 72, 48, 80],
    })
    g = df.groupby("dept")["salary"]
    print("sum:\n", g.sum())
    print("\ncount:\n", g.count())
    print("\nmin/max:\n", g.agg(["min", "max"]))
    print("\nstd:\n", g.std())

if __name__ == "__main__":
    main()