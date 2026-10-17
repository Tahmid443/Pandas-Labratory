"""Practice: merge customers, orders, and products."""
import pandas as pd

def main():
    customers = pd.DataFrame({"cid": [1, 2], "name": ["ann", "bob"]})
    orders = pd.DataFrame({"oid": [10, 11, 12], "cid": [1, 1, 2], "pid": ["p1", "p2", "p1"]})
    products = pd.DataFrame({"pid": ["p1", "p2"], "price": [5.0, 8.0]})

    merged = (
        orders.merge(customers, on="cid")
              .merge(products, on="pid")
    )
    merged["total"] = merged["price"]
    summary = merged.groupby("name").agg(orders=("oid", "size"), revenue=("total", "sum"))
    print(merged)
    print("\nSummary:\n", summary)

if __name__ == "__main__":
    main()