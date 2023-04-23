dp = [-1 for _ in range(100005)]


def fibonacci(n: int) -> int:
    if n < 2:
        return n

    if dp[n] == -1:
        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return dp[n]


n = int(input())

print(f"O termo na posição {n} da sequência de Fibonacci é: {fibonacci(n)}.")
