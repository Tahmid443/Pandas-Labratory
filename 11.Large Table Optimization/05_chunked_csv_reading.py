"""Read a CSV in chunks and aggregate."""
import io
import pandas as pd

def main():
    csv_text = "id,value\n" + "\n".join(f"{i},{i*2}" for i in range(10))
    total = 0
    for chunk in pd.read_csv(io.StringIO(csv_text), chunksize=3):
        total += chunk["value"].sum()
    print("sum via chunks:", total)

if __name__ == "__main__":
    main()