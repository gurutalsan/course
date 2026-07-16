"""
Q6. Longest Common Subsequence (LCS) of 'abcde' and 'ace'.
    Draw complete DP table. Reconstruct the actual subsequence.

Answer:
    dp[i][j] = LCS length of text1[:i] and text2[:j].
    If chars match: dp[i][j] = dp[i-1][j-1] + 1
    Else:           dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    LCS of 'abcde' and 'ace' = 'ace' (length 3).
    Time: O(m×n), Space: O(m×n).
"""


def lcs(text1, text2):
    """LCS with full DP table for visualization."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n], dp


def reconstruct_lcs(text1, text2, dp):
    """Backtrack through DP table to find the actual subsequence."""
    i, j = len(text1), len(text2)
    result = []

    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            result.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


def demonstrate():
    print("=" * 70)
    print("Q6: Longest Common Subsequence (LCS)")
    print("=" * 70)
    print()

    t1, t2 = 'abcde', 'ace'
    length, dp = lcs(t1, t2)
    subseq = reconstruct_lcs(t1, t2, dp)

    print(f"  text1: '{t1}'")
    print(f"  text2: '{t2}'")
    print(f"  LCS:   '{subseq}' (length {length})")
    print()

    # --- Complete DP Table ---
    print("--- Complete DP Table ---")
    print()
    header = "     ε  " + "  ".join(f"{c:>2}" for c in t2)
    print(f"  {header}")
    print(f"  {'':>3} {''.join(f'{j:>4}' for j in range(len(t2)+1))}")
    print(f"  {'':>3} {'----' * (len(t2)+1)}")

    for i in range(len(t1) + 1):
        label = 'ε' if i == 0 else t1[i-1]
        row = f"  {label} {i} |"
        for j in range(len(t2) + 1):
            row += f" {dp[i][j]:>2} "
        print(row)
    print()

    # --- How the table is built ---
    print("--- How Each Cell Is Computed ---")
    print()
    print("  if text1[i-1] == text2[j-1]:  dp[i][j] = dp[i-1][j-1] + 1  (diagonal + 1)")
    print("  else:                          dp[i][j] = max(dp[i-1][j], dp[i][j-1])")
    print()

    # Trace key cells
    print("--- Trace Key Cells ---")
    print()
    for i in range(1, len(t1) + 1):
        for j in range(1, len(t2) + 1):
            if t1[i-1] == t2[j-1]:
                print(f"  dp[{i}][{j}]: '{t1[i-1]}'=='{t2[j-1]}' → dp[{i-1}][{j-1}]+1 = {dp[i-1][j-1]}+1 = {dp[i][j]} ★ match")
            else:
                print(f"  dp[{i}][{j}]: '{t1[i-1]}'≠'{t2[j-1]}' → max(dp[{i-1}][{j}], dp[{i}][{j-1}]) = max({dp[i-1][j]}, {dp[i][j-1]}) = {dp[i][j]}")
    print()

    # --- Reconstruct ---
    print("--- Reconstructing the LCS ---")
    print()
    print("  Start at dp[5][3] = 3, backtrack:")
    i, j = len(t1), len(t2)
    steps = []
    while i > 0 and j > 0:
        if t1[i-1] == t2[j-1]:
            steps.append(f"  ({i},{j}): '{t1[i-1]}'=='{t2[j-1]}' → take it, go diagonal ↖")
            i -= 1; j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            steps.append(f"  ({i},{j}): go up ↑ (dp[{i-1}][{j}]={dp[i-1][j]} > dp[{i}][{j-1}]={dp[i][j-1]})")
            i -= 1
        else:
            steps.append(f"  ({i},{j}): go left ← (dp[{i}][{j-1}]={dp[i][j-1]} ≥ dp[{i-1}][{j}]={dp[i-1][j]})")
            j -= 1
    for s in steps:
        print(s)
    print(f"\n  LCS = '{subseq}' ✓")
    print()

    # --- Test cases ---
    print("--- Test Cases ---\n")
    tests = [
        ('abcde', 'ace', 3), ('abc', 'abc', 3),
        ('abc', 'def', 0), ('', 'abc', 0),
        ('AGGTAB', 'GXTXAYB', 4),
    ]
    for a, b, expected in tests:
        got, dp_t = lcs(a, b)
        sub = reconstruct_lcs(a, b, dp_t)
        print(f"  '{a}' vs '{b}' → LCS='{sub}' len={got} {'✓' if got==expected else '✗'}")

    print()
    print("  Time: O(m×n) | Space: O(m×n)")


if __name__ == "__main__":
    demonstrate()
