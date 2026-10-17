"""Schema validation with pandera (skips if not installed)."""
import pandas as pd

def main():
    try:
        import pandera as pa
    except ImportError:
        print("pandera not installed; skipping demo.")
        return

    schema = pa.DataFrameSchema({
        "id": pa.Column(int, pa.Check.ge(0)),
        "score": pa.Column(float, pa.Check.in_range(0, 100)),
    })

    good = pd.DataFrame({"id": [1, 2], "score": [90.0, 85.0]})
    print(schema.validate(good))

    bad = pd.DataFrame({"id": [-1, 2], "score": [90.0, 85.0]})
    try:
        schema.validate(bad)
    except pa.errors.SchemaError as e:
        print("validation error caught")

if __name__ == "__main__":
    main()