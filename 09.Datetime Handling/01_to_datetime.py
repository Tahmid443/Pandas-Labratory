"""Convert strings to datetimes."""
import pandas as pd

def main():
    s = pd.Series(["2024-01-01", "2024-02-15", "not a date"])
    print("original:\n", s)
    print("\nto_datetime (errors='coerce'):\n",
          pd.to_datetime(s, errors="coerce"))
    print("\nwith format:\n",
          pd.to_datetime(["2024/03/01", "2024/03/02"], format="%Y/%m/%d"))

if __name__ == "__main__":
    main()