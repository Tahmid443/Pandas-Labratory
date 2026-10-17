"""Named aggregation for clear output column names."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "dept": ["HR", "IT", "IT", "HR", "IT"],
        "salary": [50, 70, 72, 48, 80],
    })
    out = df.groupby("dept").agg(
        avg_salary=("salary", "mean"),
        total_salary=("salary", "sum"),
        n=("salary", "size"),
    )
    print(out)

if __name__ == "__main__":
    main()