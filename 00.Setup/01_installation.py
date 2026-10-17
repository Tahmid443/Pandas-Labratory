"""Verify pandas/numpy installation and versions."""
import sys

def main():
    print("Python:", sys.version.split()[0])
    try:
        import numpy as np
        import pandas as pd
        print("numpy:", np.__version__)
        print("pandas:", pd.__version__)
    except ImportError as e:
        print("Missing dependency:", e)
        print("Install with: pip install pandas numpy")
        return

    df = pd.DataFrame({"a": [1, 2, 3], "b": [4.0, 5.0, 6.0]})
    print("\nSmoke test DataFrame:")
    print(df)
    print("\nSetup OK.")

if __name__ == "__main__":
    main()