"""Split into train / validation / test."""
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.DataFrame({"x": range(20), "y": [0, 1] * 10})
    X_train, X_tmp, y_train, y_tmp = train_test_split(
        df[["x"]], df["y"], test_size=0.4, random_state=0, stratify=df["y"]
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_tmp, y_tmp, test_size=0.5, random_state=0, stratify=y_tmp
    )
    print("train:", len(X_train), "val:", len(X_val), "test:", len(X_test))

if __name__ == "__main__":
    main()