"""Check required columns exist and have no nulls."""
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, None], "score": [1.5, 2.5]})
    required = ["id", "score"]
    assert set(required).issubset(df.columns), "missing required columns"
    print("null counts:\n", df[required].isna().sum())
    assert not df["id"].isna().any(), "id contains nulls"

if __name__ == "__main__":
    main()