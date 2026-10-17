"""Compare CSV vs JSON vs Parquet sizes for the same data."""
import io
import pandas as pd

def main():
    df = pd.DataFrame({
        "id": range(1000),
        "value": [i * 0.5 for i in range(1000)],
        "label": ["a", "b"] * 500,
    })

    csv_bytes = len(df.to_csv(index=False).encode())
    json_bytes = len(df.to_json(orient="records").encode())
    print(f"CSV bytes:    {csv_bytes}")
    print(f"JSON bytes:   {json_bytes}")

    try:
        buf = io.BytesIO()
        df.to_parquet(buf, engine="pyarrow")
        print(f"Parquet bytes: {len(buf.getvalue())}")
    except ImportError:
        print("Parquet skipped (pyarrow not installed).")

if __name__ == "__main__":
    main()