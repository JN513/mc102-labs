direction_x = [1, 0, -1, 0]
direction_y = [0, 1, 0, -1]


def verifica_pos(matriz: list[list[str]], x: int, y: int) -> bool:
    return y < len(matriz) and x < len(matriz[0]) and y >= 0 and x >= 0


def print_matriz(matriz: list[list[str]]) -> None:
    for linha in matriz:
        print(" ".join(linha))


def check(matriz: list[list[str]], y: int, x: int) -> list[list[str]]:
    #print_matriz(matriz)

    queue: list[tuple] = list()

    for i in range(4):
        dir_xi = x + direction_x[i]
        dir_yi = y + direction_y[i]

        if not verifica_pos(matriz, dir_xi, dir_yi):
            continue

        if matriz[dir_yi][dir_xi] == "o":
            queue.append((dir_yi, dir_xi))

    while len(queue) > 0:
        ...

    return matriz


def varredura(matriz: list[list[str]]) -> list[list[str]]:
    start = 0
    end = len(matriz[0])
    passo = 1
    for i in range(len(matriz)):
        if i % 2 == 0 and passo == -1:
            passo = 1
            start, end = end, start
        elif passo == 1:
            passo = -1
            start, end = end, start

        for j in range(start, end, passo):
            print_matriz(matriz)
            if matriz[i][j] == "o":
                check(matriz, i, j)


def main() -> None:
    numero_de_linhas: int = int(input())

    matriz: list[list] = [input().split() for _ in range(numero_de_linhas)]

    varredura(matriz)


if __name__ == "__main__":
    main()
