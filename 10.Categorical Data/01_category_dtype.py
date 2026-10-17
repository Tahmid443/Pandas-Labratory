"""Create and inspect category dtype."""
import pandas as pd

def main():
    s = pd.Series(["a", "b", "a", "c"], dtype="category")
    print(s)
    print("\ndtype:", s.dtype)
    print("categories:", list(s.cat.categories))
    print("codes:", s.cat.codes.tolist())
    print("memory (category):", s.memory_usage(deep=True))
    print("memory (object):  ", s.astype(object).memory_usage(deep=True))

if __name__ == "__main__":
    main()