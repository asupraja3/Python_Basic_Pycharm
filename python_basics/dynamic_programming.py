#Dynamic programming basics
#Dynamic programming is a method for solving complex problems by breaking them down into simpler
# subproblems. It is applicable when the problem can be divided into overlapping subproblems
# that can be solved independently.

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
# Example usage
if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n} is {fibonacci(n)}")
    # This will compute the Fibonacci number for n=10 using dynamic programming with memoization.
    # The memo dictionary stores previously computed Fibonacci numbers to avoid redundant
    # calculations.
# This approach significantly reduces the time complexity from exponential to linear.
# Dynamic programming is particularly useful for optimization problems where the solution can be
# constructed from solutions to smaller subproblems.
# Key concepts in dynamic programming include:
# 1. **Overlapping Subproblems**: The problem can be broken down into smaller subproblems that
# are reused multiple times.
# 2. **Optimal Substructure**: The optimal solution to the problem can be constructed from the
# optimal solutions of its subproblems.
# 3. **Memoization**: Storing the results of expensive function calls and reusing them when the
# same inputs occur again.
# 4. **Tabulation**: Building a table in a bottom-up manner to store the results of subproblems,
# which can be used to solve larger problems.
# Dynamic programming is a powerful technique that can lead to efficient algorithms for problems
# that would otherwise be intractable.
# It is often used in algorithms for optimization, such as finding the shortest path in a graph,
# solving knapsack problems, and many others.
# Some common examples of dynamic programming problems include:
# 1. **Fibonacci Sequence**: Calculating Fibonacci numbers efficiently using memoization or
# tabulation.
# 2. **Knapsack Problem**: Finding the maximum value that can be obtained with a given weight
# limit.
# 3. **Longest Common Subsequence**: Finding the longest subsequence that appears in the same
# order in two sequences.
# 4. **Edit Distance**: Calculating the minimum number of operations required to convert one
# string into another.
# 5. **Matrix Chain Multiplication**: Finding the most efficient way to multiply a chain of
# matrices.
# 6. **Coin Change Problem**: Finding the minimum number of coins needed to make a certain
# amount of money.
# 7. **Dynamic Programming on Trees**: Solving problems related to trees, such as finding the
# diameter or the maximum path sum.
