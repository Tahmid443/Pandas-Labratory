"""Extract year, month, day, weekday from datetimes."""
import pandas as pd

def main():
    s = pd.Series(pd.to_datetime(["2024-01-15 10:30", "2024-02-20 22:00"]))
    df = pd.DataFrame({
        "ts": s,
        "year": s.dt.year,
        "month": s.dt.month,
        "day": s.dt.day,
        "dow": s.dt.dayofweek,
        "hour": s.dt.hour,
    })
    print(df)

if __name__ == "__main__":
    main()