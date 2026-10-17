"""Benchmark sum: python sum vs numpy vs pandas."""
import time
import numpy as np
import pandas as pd

def main():
    arr = np.random.rand(1_000_000)
    s = pd.Series(arr)

    t0 = time.perf_counter(); _ = sum(arr); t_py = time.perf_counter() - t0
    t0 = time.perf_counter(); _ = arr.sum(); t_np = time.perf_counter() - t0
    t0 = time.perf_counter(); _ = s.sum(); t_pd = time.perf_counter() - t0

    print(f"python sum: {t_py:.4f}s")
    print(f"numpy sum:  {t_np:.4f}s")
    print(f"pandas sum: {t_pd:.4f}s")

if __name__ == "__main__":
    main()