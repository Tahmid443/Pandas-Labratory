"""Read/write Parquet using an in-memory BytesIO (requires pyarrow)."""
import io
import pandas as pd

def main():
    df = pd.DataFrame({"id": [1, 2, 3], "val": [1.1, 2.2, 3.3]})
    buf = io.BytesIO()
    try:
        df.to_parquet(buf, engine="pyarrow")
        buf.seek(0)
        back = pd.read_parquet(buf, engine="pyarrow")
        print("Round-tripped Parquet:\n", back)
    except ImportError:
        print("pyarrow not installed; skipping Parquet demo.")

if __name__ == "__main__":
    main()