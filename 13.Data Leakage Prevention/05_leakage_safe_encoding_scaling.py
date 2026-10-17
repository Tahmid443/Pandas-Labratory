"""Leakage-safe encoding + scaling using ColumnTransformer."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def main():
    df = pd.DataFrame({
        "color": ["red", "blue", "red", "green", "blue", "green"],
        "num": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
        "y": [0, 1, 0, 1, 0, 1],
    })
    X = df.drop(columns="y")
    train, test = train_test_split(X, test_size=0.33, random_state=0)

    pre = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["color"]),
        ("num", StandardScaler(), ["num"]),
    ])
    X_train = pre.fit_transform(train)
    X_test = pre.transform(test)
    print("train shape:", X_train.shape)
    print("test shape:", X_test.shape)

if __name__ == "__main__":
    main()