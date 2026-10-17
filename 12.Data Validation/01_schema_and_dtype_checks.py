"""Check column presence and dtypes."""
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, 2], "score": [1.5, 2.5]})
    expected = {"id": "int64", "score": "float64"}
    for col, dtype in expected.items():
        assert col in df.columns, f"missing {col}"
        assert str(df[col].dtype) == dtype, f"{col} dtype {df[col].dtype} != {dtype}"
    print("schema OK")

if __name__ == "__main__":
    main()