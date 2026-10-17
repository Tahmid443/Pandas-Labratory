"""Localize and convert timezones."""
import pandas as pd

def main():
    s = pd.Series(pd.to_datetime(["2024-01-01 12:00", "2024-06-01 12:00"]))
    localized = s.dt.tz_localize("US/Eastern")
    converted = localized.dt.tz_convert("UTC")
    print("localized:\n", localized)
    print("\nUTC:\n", converted)

if __name__ == "__main__":
    main()