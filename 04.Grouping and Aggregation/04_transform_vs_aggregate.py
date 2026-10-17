"""transform returns same-shape; aggregate collapses groups."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "dept": ["HR", "IT", "IT", "HR", "IT"],
        "salary": [50, 70, 72, 48, 80],
    })
    df["dept_mean"] = df.groupby("dept")["salary"].transform("mean")
    df["above_mean"] = df["salary"] > df["dept_mean"]
    print(df)

    print("\naggregate:\n", df.groupby("dept")["salary"].mean())

if __name__ == "__main__":
    main()