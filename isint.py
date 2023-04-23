def isint(x: str) -> bool:
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]

    for i in x:
        if not i in digits:
            return False

    return True


def ler_numero() -> int:
    while True:
        n = input()
        if isint(n):
            return int(n)
        else:
            print("Valor invalido")


def quadrado_lista(l: list, process: function):
    for i in range(len(l)):
        l[i] = process(l[i])

    return l


def quadrado(n):
    return n * n


print(f"Numero: {ler_numero()}")


print(quadrado_lista([1, 2, 3], quadrado))

x = [1, 2, 3, 4, 6, 7, 9]
