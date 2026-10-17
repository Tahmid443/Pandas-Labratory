"""Group-based split to keep groups intact."""
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

def main():
    df = pd.DataFrame({
        "group": [1, 1, 2, 2, 3, 3, 4, 4],
        "x": range(8),
    })
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=0)
    train_idx, test_idx = next(splitter.split(df, groups=df["group"]))
    print("train groups:", sorted(df.iloc[train_idx]["group"].unique()))
    print("test groups: ", sorted(df.iloc[test_idx]["group"].unique()))

if __name__ == "__main__":
    main()