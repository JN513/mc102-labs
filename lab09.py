direction_x = [-1, 0, 1, 0]
direction_y = [0, -1, 0, 1]
matriz: list[list[str]]

nexts_positions: int = 0


def verifica_pos(y: int, x: int) -> bool:
    global matriz

    return y < len(matriz) and x < len(matriz[0]) and y >= 0 and x >= 0


def get_next_positon(y: int, x: int) -> tuple[int, int]:
    size = len(matriz[0])
    if y % 2 == 0:
        if x == size - 1:
            return y + 1, x
        else:
            return y, x + 1
    else:
        if x == 0:
            return y + 1, x
        else:
            return y, x - 1


def is_next_position(y: int, x: int, a: int, b: int) -> bool:
    return (a, b) == get_next_positon(y, x)


def print_matriz() -> None:
    global matriz

    for linha in matriz:
        print(" ".join(linha))

    print()


def check(y: int, x: int, interator=0) -> tuple[int, int]:
    global matriz
    global nexts_positions

    matriz[y][x] = "."
    print(f"xy _ {x} {y}")

    queue: list[tuple] = list()

    for i in range(4):
        dir_xi = x + direction_x[i]
        dir_yi = y + direction_y[i]

        # print(f"xy {dir_yi} - {dir_xi}")

        if not verifica_pos(dir_yi, dir_xi):
            continue

        if matriz[dir_yi][dir_xi] == "o":
            if (is_next_position(y, x, dir_yi, dir_xi)) and nexts_positions == interator:
                nexts_positions += 1
            queue.append((dir_yi, dir_xi))

    a: int = y
    b: int = x

    while len(queue) > 0:
        print(f"ab - {a} {b}, {queue} ")

        if matriz[queue[0][0]][queue[0][1]] == ".":
            queue.pop(0)
            continue

        a, b = queue.pop(0)

        matriz[a][b] = "r"
        print(f"ab - {a} {b}, {queue} ")
        print_matriz()

        matriz[a][b] = "."

        v, w = check(a, b, interator=interator + 1)

        print(f"vw - {v} {w}, ab - {a} {b}, {queue} ")

        if (a, b) != (v, w):
            print(f"vw - {v} {w}, ab - {a} {b}, {queue} {len(queue)}")
            a, b = v, w
        else:
            print("clear queue")
            queue.clear()
            print(f"len: {len(queue)}")

        # a, b = v, w

    return a, b


def voltar(y: int, x: int, a: int, b: int) -> None:
    global matriz
    # print("voltar")
    voltas: int = 1

    for _ in range(voltas):

        if b > x:
            # print("fdp")
            while b > x:
                matriz[a][b] = "."

                b -= 1

                matriz[a][b] = "r"

                print_matriz()

                k, d = check(a, b)

                if (k, d) != (a, b):
                    # y, x = k, d
                    a, b = k, d
                    voltas += 1
                    continue
        elif b < x:
            # print("eu")
            while b < x:
                matriz[a][b] = "."

                b += 1

                matriz[a][b] = "r"

                print_matriz()

                k, d = check(a, b)

                if (k, d) != (a, b):
                    # y, x = k, d
                    a, b = k, d
                    voltas += 1
                    continue

        while a > y:
            matriz[a][b] = "."

            a -= 1

            matriz[a][b] = "r"

            print_matriz()

            k, d = check(a, b)

            if (k, d) != (a, b):
                # y, x = k, d
                a, b = k, d
                voltas += 1
                continue


def varredura_horizontal(i: int, truncate: bool = False) -> bool:
    global matriz
    global nexts_positions

    start = 0
    end = len(matriz[0])

    lastx: int = 0
    lasty: int = 0

    passo = 1

    if (i + truncate % 2) == 0 and passo == -1:
        passo = 1
        start, end = end + 1, start + 1
    elif (i + truncate) % 2 == 1 and passo == 1:
        passo = -1
        start, end = end - 1, start - 1

    for j in range(start, end, passo):
        if nexts_positions:
            nexts_positions -= 1
            continue

        matriz[lastx][lasty] = "."

        matriz[i][j] = "r"

        if not (truncate and j == 0):
            print_matriz()

        lastx, lasty = i, j

        a, b = check(i, j)

        print(f"{a} {b} - {i} {j} - {nexts_positions}")

        if (a != i or b != j) and not is_next_position(i, j, a, b):
            if nexts_positions:
                v, w = i, j
                for _ in range(nexts_positions):
                    v, w = get_next_positon(v, w)
                    # print(f"v,w {v} {w} - {i} { j}")
                    matriz[v][w] = "."
                print(f"voltar v,w {v} {w} - {i} { j} - {a} {b}")

                voltar(v, w, a, b)
                matriz[v][w] = "."
            else:
                print(f"voltar v,w {i} { j} - {a} {b}")
                voltar(i, j, a, b)
                matriz[i][j] = "."


def varredura() -> None:
    global matriz

    for i in range(len(matriz)):
        varredura_horizontal(i)

    if len(matriz) % 2 != 1:
        varredura_horizontal(len(matriz) - 1, truncate=True)


def main() -> None:
    numero_de_linhas: int = int(input())

    global matriz

    matriz = [input().split() for _ in range(numero_de_linhas)]

    varredura()


if __name__ == "__main__":
    main()
