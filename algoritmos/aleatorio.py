def soma(lista: list[int]) -> int:
    if len(lista) == 1:
        return lista[0]

    return lista[0] + soma(lista[1:])


def fatorial(num: int) -> int:
    if num == 1:
        return 1

    return num * fatorial(num - 1)


dp = [0 for _ in range(10000005)]

dp[1] = 1


def fibonacci(n: int) -> int:
    if n < 2:
        return n

    if not dp[n]:
        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]


print(soma([1, 2, 3, 4, 5]))

print(fatorial(5))

print(fibonacci(4))


def soma1(n) -> int:
    if n < 2:
        return n
    elif n % 2 == 1:
        return n + soma1(n - 2)
    elif n % 2 == 0:
        return soma1(n - 1)


print(soma1(8))
