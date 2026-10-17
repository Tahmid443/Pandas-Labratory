"""Vectorized ops vs Python loop (speed demo)."""
import time
import numpy as np
import pandas as pd

def main():
    n = 1_000_000
    s = pd.Series(np.random.rand(n))

    t0 = time.perf_counter()
    loop_result = [x * 2 for x in s]
    t_loop = time.perf_counter() - t0

    t0 = time.perf_counter()
    vec_result = s * 2
    t_vec = time.perf_counter() - t0

    print(f"loop: {t_loop:.4f}s  vectorized: {t_vec:.4f}s")
    print("speedup ~", round(t_loop / t_vec, 1), "x")

if __name__ == "__main__":
    main()