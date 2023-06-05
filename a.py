def voltar(y: int, x: int, a: int, b: int) -> None:
    global matriz
    voltas: int = 1

    for _ in range(voltas):
        print(f"voltar yx {y} {x}, {a} {b}")
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
                    break
        elif b < x:
            # print("eu")
            while b < x:
                matriz[a][b] = "."

                b += 1

                matriz[a][b] = "r"

                print_matriz()

                k, d = check(a, b)
                print(f"voltar kd 1 {k} {d}, {a} {b}")

                if (k, d) != (a, b):
                    # y, x = k, d
                    print("oxe")
                    a, b = k, d
                    voltas += 1
                    print(f"voltar kd 3 {k} {d}, {a} {b}")
                    break

        if voltas > _:
            print(f"continue kd 1 {y} {x}, {a} {b}")
            continue

        while a > y:
            matriz[a][b] = "."

            a -= 1

            matriz[a][b] = "r"

            print_matriz()

            k, d = check(a, b)
            print(f"voltar kd 2 {k} {d}, {a} {b}")

            if (k, d) != (a, b):
                # y, x = k, d
                a, b = k, d
                voltas += 1
                break

        # Continue no loop externo for
        else:
            continue
