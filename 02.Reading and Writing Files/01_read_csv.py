"""Read CSV from an in-memory buffer (no disk needed)."""
import io
import pandas as pd

def main():
    csv_text = "id,name,score\n1,ann,90\n2,bob,85\n3,cy,77\n"
    df = pd.read_csv(io.StringIO(csv_text))
    print(df)
    print("\ndtypes:\n", df.dtypes)

if __name__ == "__main__":
    main()