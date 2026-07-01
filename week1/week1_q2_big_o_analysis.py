"""
Q2. Analyze this code and state its Big O:

    def mystery(n):
        for i in range(n):
            for j in range(n):
                print(i + j)

Answer: O(n²) — Quadratic Time

Explanation:
    - The outer loop runs n times (i = 0, 1, ..., n-1).
    - For EACH iteration of the outer loop, the inner loop also runs n times
      (j = 0, 1, ..., n-1).
    - The print(i + j) operation inside is O(1).
    - Total operations = n × n × 1 = n²

    Therefore, Big O = O(n²)
"""


def mystery(n):
    """Original function from the question."""
    count = 0
    for i in range(n):
        for j in range(n):
            print(i + j, end=" ")
            count += 1
        print()  # newline after each row
    return count


def analyze_mystery():
    """Analyze and demonstrate the O(n²) behavior."""
    print("=" * 60)
    print("Q2: Big O Analysis of mystery(n)")
    print("=" * 60)
    print()

    # Show the code
    print("Code:")
    print("  def mystery(n):")
    print("      for i in range(n):        ← runs n times")
    print("          for j in range(n):    ← runs n times (for EACH i)")
    print("              print(i + j)      ← O(1) operation")
    print()
    print("Analysis:")
    print("  Outer loop iterations:  n")
    print("  Inner loop iterations:  n (per outer iteration)")
    print("  Total print calls:      n × n = n²")
    print()

    # Demonstrate with small values
    print("--- Demonstration ---")
    print()
    test_values = [2, 3, 4, 5, 10]
    print(f"  {'n':>5}  |  {'Total Operations (n²)':>20}  |  {'n²':>6}")
    print(f"  {'-'*5}  |  {'-'*20}  |  {'-'*6}")

    for n in test_values:
        count = 0
        for i in range(n):
            for j in range(n):
                count += 1
        print(f"  {n:>5}  |  {count:>20}  |  {n**2:>6}")

    print()
    print("  n² matches total operations every time → O(n²) confirmed.")
    print()

    # Visual: show the grid for n=4
    print("--- Visual Grid for n=4 ---")
    print("  (Each cell = one print(i+j) call)")
    print()
    n = 4
    print("       j=0  j=1  j=2  j=3")
    for i in range(n):
        row = f"  i={i}  "
        for j in range(n):
            row += f" {i+j:>3} "
        print(row)
    print()
    print(f"  Total cells = {n} × {n} = {n**2} = n²")
    print()
    print("ANSWER: The time complexity is O(n²) — Quadratic Time.")


if __name__ == "__main__":
    analyze_mystery()
