"""One-hot encode a categorical column."""
import pandas as pd

def main():
    df = pd.DataFrame({"color": ["red", "blue", "red", "green"]})
    ohe = pd.get_dummies(df["color"], prefix="color")
    print(pd.concat([df, ohe], axis=1))

if __name__ == "__main__":
    main()