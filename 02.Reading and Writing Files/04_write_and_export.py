"""Export a DataFrame to CSV and JSON strings."""
import io
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, 2], "name": ["ann", "bob"]})
    csv_str = df.to_csv(index=False)
    print("CSV:\n", csv_str)
    json_str = df.to_json(orient="records")
    print("JSON:", json_str)

if __name__ == "__main__":
    main()