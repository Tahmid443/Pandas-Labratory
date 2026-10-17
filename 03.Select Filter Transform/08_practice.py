"""Practice: filter, transform, and select."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "name": ["Ann", "Bob", "Cara", "Dan"],
        "dept": ["HR", "IT", "IT", "HR"],
        "salary": [50000, 70000, 72000, 48000],
    })
    result = (
        df[df["salary"] > 50000]
        .assign(bonus=lambda d: d["salary"] * 0.1)
        .sort_values("salary", ascending=False)[["name", "salary", "bonus"]]
    )
    print(result)

if __name__ == "__main__":
    main()