"""Create Series from lists, dicts, and scalars."""
import pandas as pd

def main():
    s_list = pd.Series([1, 2, 3])
    print("From list:\n", s_list)

    s_dict = pd.Series({"a": 10, "b": 20, "c": 30})
    print("\nFrom dict:\n", s_dict)

    s_scalar = pd.Series(5, index=["x", "y", "z"])
    print("\nFrom scalar with index:\n", s_scalar)

    print("\nvalues:", s_dict.values)
    print("index:", list(s_dict.index))
    print("dtype:", s_dict.dtype)

if __name__ == "__main__":
    main()