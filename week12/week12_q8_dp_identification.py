"""
Q8. Which problems can be solved with DP? Explain why.
    (a) Shortest path  (b) All permutations  (c) Min edit distance  (d) Sorting

Answer:
    DP applies when a problem has:
    1. OPTIMAL SUBSTRUCTURE: optimal solution built from optimal sub-solutions.
    2. OVERLAPPING SUBPROBLEMS: same subproblems solved repeatedly.

    (a) Shortest path → YES ✓ (Bellman-Ford, Floyd-Warshall)
    (b) All permutations → NO ✗ (no overlapping subproblems, use backtracking)
    (c) Min edit distance → YES ✓ (classic DP — Levenshtein distance)
    (d) Sorting → NO ✗ (no overlapping subproblems, comparison-based)
"""


def edit_distance(word1, word2):
    """Minimum edit distance (Levenshtein). Classic DP. O(m×n)."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # Delete
                    dp[i][j-1],     # Insert
                    dp[i-1][j-1],   # Replace
                )

    return dp[m][n], dp


def demonstrate():
    print("=" * 70)
    print("Q8: Which Problems Can Be Solved with DP?")
    print("=" * 70)
    print()

    # --- Two requirements ---
    print("--- Two Requirements for DP ---")
    print()
    print("  1. OPTIMAL SUBSTRUCTURE:")
    print("     The optimal solution contains optimal solutions to subproblems.")
    print("     Example: shortest path A→C via B = shortest(A→B) + shortest(B→C)")
    print()
    print("  2. OVERLAPPING SUBPROBLEMS:")
    print("     The same subproblem is solved multiple times.")
    print("     Example: fib(5) recomputes fib(3) multiple times.")
    print()
    print("  Both conditions must hold for DP to be applicable!")
    print()

    # --- Analysis ---
    print("=" * 50)
    print("(a) SHORTEST PATH IN A GRAPH — YES ✓")
    print("=" * 50)
    print()
    print("  Optimal substructure: ✓")
    print("    shortest(A→C) = min over B of (shortest(A→B) + edge(B,C))")
    print()
    print("  Overlapping subproblems: ✓")
    print("    Multiple paths may query shortest distance to same node.")
    print()
    print("  DP algorithms: Bellman-Ford O(VE), Floyd-Warshall O(V³)")
    print("  (Dijkstra is greedy but exploits optimal substructure too)")
    print()

    print("=" * 50)
    print("(b) GENERATING ALL PERMUTATIONS — NO ✗")
    print("=" * 50)
    print()
    print("  Optimal substructure: Not applicable (no optimization)")
    print("  Overlapping subproblems: ✗")
    print("    Each permutation is UNIQUE — no repeated subproblems.")
    print()
    print("  Correct approach: BACKTRACKING")
    print("  We need to ENUMERATE all solutions, not optimize one.")
    print()

    print("=" * 50)
    print("(c) MINIMUM EDIT DISTANCE — YES ✓")
    print("=" * 50)
    print()
    print("  Optimal substructure: ✓")
    print("    edit(word1[:i], word2[:j]) depends on sub-edits")
    print()
    print("  Overlapping subproblems: ✓")
    print("    Multiple paths through the DP table share sub-solutions.")
    print()

    # Demo
    w1, w2 = "horse", "ros"
    dist, dp = edit_distance(w1, w2)
    print(f"  Example: '{w1}' → '{w2}'")
    print(f"  Edit distance: {dist}")
    print()

    print("  DP Table:")
    header = "       ε  " + "  ".join(f" {c}" for c in w2)
    print(f"  {header}")
    for i in range(len(w1) + 1):
        label = 'ε' if i == 0 else w1[i-1]
        row = f"  {label}  "
        for j in range(len(w2) + 1):
            row += f" {dp[i][j]:>2}"
        print(row)
    print()
    print("  Operations: insert, delete, replace (each cost 1)")
    print("  horse → rorse (replace h→r) → ros (delete r,e) → 3 edits")
    print()

    print("=" * 50)
    print("(d) SORTING AN ARRAY — NO ✗")
    print("=" * 50)
    print()
    print("  Optimal substructure: Partially (merge sort divides)")
    print("  Overlapping subproblems: ✗")
    print("    Each subarray is unique — no repeated computation.")
    print()
    print("  Correct approach: Divide & Conquer (merge sort, quicksort)")
    print("  These are NOT DP because subproblems don't overlap.")
    print()

    # --- Summary Table ---
    print("--- Summary ---")
    print()
    print("  Problem               | DP? | Optimal   | Overlapping | Better approach")
    print("                        |     | substruct.| subproblems |")
    print("  ----------------------|-----|-----------|-------------|----------------")
    print("  (a) Shortest path     | YES | ✓         | ✓           | Bellman-Ford/FW")
    print("  (b) All permutations  | NO  | N/A       | ✗           | Backtracking")
    print("  (c) Edit distance     | YES | ✓         | ✓           | 2D DP table")
    print("  (d) Sorting           | NO  | Partial   | ✗           | Divide & Conquer")
    print()

    # --- DP vs other paradigms ---
    print("--- DP vs Other Paradigms ---")
    print()
    print("  Paradigm          | When to use")
    print("  ------------------|---------------------------------------------")
    print("  DP                | Optimization + overlapping subproblems")
    print("  Greedy            | Optimization + greedy choice property")
    print("  Divide & Conquer  | Independent (non-overlapping) subproblems")
    print("  Backtracking      | Enumerate all solutions, constraints")
    print()
    print("  Key test: 'Am I solving the same subproblem multiple times?'")
    print("  If YES → DP. If NO → probably D&C or Greedy.")


if __name__ == "__main__":
    demonstrate()
