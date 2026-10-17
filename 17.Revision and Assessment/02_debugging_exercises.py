"""Fix the bug: this snippet raises a KeyError."""
import pandas as pd

def buggy():
    df = pd.DataFrame({"Name": [1, 2]})
    return df["name"]  # wrong case

def fixed():
    df = pd.DataFrame({"Name": [1, 2]})
    return df["Name"]

def main():
    try:
        buggy()
    except KeyError as e:
        print("Caught bug:", e)
    print("Fixed:\n", fixed())

if __name__ == "__main__":
    main()