"""Range and domain checks."""
import pandas as pd

def main():
    df = pd.DataFrame({"age": [0, 40, 130], "gender": ["M", "F", "X"]})

    bad_age = df[(df["age"] < 0) | (df["age"] > 120)]
    print("bad ages:\n", bad_age)

    valid_gender = {"M", "F"}
    bad_gender = df[~df["gender"].isin(valid_gender)]
    print("bad genders:\n", bad_gender)

if __name__ == "__main__":
    main()