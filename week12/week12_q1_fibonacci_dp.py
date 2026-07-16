"""
Q1. Implement Fibonacci three ways: (a) naive recursion, (b) memoization
    with @lru_cache, (c) bottom-up tabulation. Compare time complexity.

Answer:
    (a) Naive recursion:  O(2^n) — exponential, recomputes subproblems.
    (b) Memoization:      O(n)   — each subproblem computed once, cached.
    (c) Tabulation:       O(n)   — iterative, fills table bottom-up.

    Memoization = top-down (recursive + cache).
    Tabulation  = bottom-up (iterative + table).
"""

import time
from functools import lru_cache


# (a) Naive Recursion — O(2^n)
def fib_naive(n):
    """Naive recursive Fibonacci. O(2^n) time, O(n) space."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# (b) Memoization — O(n)
@lru_cache(maxsize=None)
def fib_memo(n):
    """Memoized Fibonacci using @lru_cache. O(n) time, O(n) space."""
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


def fib_memo_manual(n, cache=None):
    """Manual memoization with dict."""
    if cache is None:
        cache = {}
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fib_memo_manual(n - 1, cache) + fib_memo_manual(n - 2, cache)
    return cache[n]


# (c) Bottom-Up Tabulation — O(n)
def fib_tabulation(n):
    """Bottom-up tabulation. O(n) time, O(n) space."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib_optimized(n):
    """Space-optimized O(1). Only need last two values."""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def benchmark(fn, n, label):
    start = time.perf_counter()
    result = fn(n)
    elapsed = (time.perf_counter() - start) * 1000
    return result, elapsed


def demonstrate():
    print("=" * 70)
    print("Q1: Fibonacci — Three Approaches")
    print("=" * 70)
    print()

    # Show values
    print("--- Fibonacci Sequence ---")
    print(f"  First 15: {[fib_tabulation(i) for i in range(15)]}")
    print()

    # --- Naive recursion tree ---
    print("--- (a) Naive Recursion — O(2^n) ---")
    print()
    print("  fib(5) recursion tree:")
    print("                    fib(5)")
    print("                 /         \\")
    print("             fib(4)       fib(3)")
    print("            /     \\       /    \\")
    print("        fib(3)  fib(2) fib(2) fib(1)")
    print("        /   \\    / \\    / \\")
    print("     fib(2) fib(1) ... ...")
    print()
    print("  fib(3) computed 2 times! fib(2) computed 3 times!")
    print("  Massive redundancy → O(2^n)")
    print()

    # --- Memoization ---
    print("--- (b) Memoization (Top-Down) — O(n) ---")
    print()
    print("  Same recursion, but CACHE results:")
    print("  fib(5) → compute fib(4) → compute fib(3) → compute fib(2)")
    print("  fib(3) needed again? → return from cache! ★")
    print()
    print("  Each fib(k) computed exactly ONCE → O(n)")
    print()

    # --- Tabulation ---
    print("--- (c) Tabulation (Bottom-Up) — O(n) ---")
    print()
    print("  Fill table from bottom: dp[0]=0, dp[1]=1, dp[i] = dp[i-1]+dp[i-2]")
    print()
    n = 10
    dp = [0] * (n + 1)
    dp[1] = 1
    print(f"  {'i':>3} | {'dp[i-1]':>7} + {'dp[i-2]':>7} = {'dp[i]':>7}")
    print(f"  {'-'*3} | {'-'*7}   {'-'*7}   {'-'*7}")
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"  {i:>3} | {dp[i-1]:>7} + {dp[i-2]:>7} = {dp[i]:>7}")
    print()

    # --- Benchmarks ---
    print("--- Performance Comparison ---")
    print()
    print(f"  {'n':>4} | {'Naive':>12} | {'Memo':>12} | {'Tabulation':>12} | {'Optimized':>12}")
    print(f"  {'-'*4} | {'-'*12} | {'-'*12} | {'-'*12} | {'-'*12}")

    for n in [10, 20, 30, 35]:
        _, t1 = benchmark(fib_naive, n, "naive") if n <= 35 else (0, float('inf'))
        fib_memo.cache_clear()
        _, t2 = benchmark(fib_memo, n, "memo")
        _, t3 = benchmark(fib_tabulation, n, "tab")
        _, t4 = benchmark(fib_optimized, n, "opt")
        t1_str = f"{t1:.3f}ms" if t1 < 10000 else "too slow"
        print(f"  {n:>4} | {t1_str:>12} | {t2:.3f}ms{'':<4} | {t3:.3f}ms{'':<4} | {t4:.3f}ms")

    print()

    # --- Comparison ---
    print("--- Summary ---")
    print()
    print("  Approach    | Time   | Space | Style")
    print("  ------------|--------|-------|------------------")
    print("  Naive       | O(2^n) | O(n)  | Top-down, no cache")
    print("  Memoization | O(n)   | O(n)  | Top-down + cache")
    print("  Tabulation  | O(n)   | O(n)  | Bottom-up table")
    print("  Optimized   | O(n)   | O(1)  | Two variables only")


if __name__ == "__main__":
    demonstrate()
