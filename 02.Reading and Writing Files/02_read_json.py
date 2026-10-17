"""Read JSON from an in-memory buffer."""
import io
import pandas as pd

def main():
    json_text = '[{"id":1,"name":"ann"},{"id":2,"name":"bob"}]'
    df = pd.read_json(io.StringIO(json_text))
    print(df)

if __name__ == "__main__":
    main()