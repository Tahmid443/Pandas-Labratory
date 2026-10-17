"""Basic groupby usage."""
import pandas as pd

def main():
    df = pd.DataFrame({
        "dept": ["HR", "IT", "IT", "HR", "IT"],
        "salary": [50, 70, 72, 48, 80],
    })
    g = df.groupby("dept")
    print("groups:", list(g.groups.keys()))
    print("\nmean salary by dept:\n", g["salary"].mean())
    print("\nsize:\n", g.size())
    for name, sub in g:
        print(f"\n{name}:\n{sub}")

if __name__ == "__main__":
    main()