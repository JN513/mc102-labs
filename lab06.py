def padronizar_vetores(
    vetor1: list, vetor2: list, compesador: int = 0, divisao: bool = False
):
    if len(vetor1) > len(vetor2):
        vetor2.extend([compesador for _ in range(len(vetor1) - len(vetor2))])
    elif len(vetor1) < len(vetor2):
        vetor1.extend(
            [
                abs(compesador - divisao)
                for _ in range(len(vetor2) - len(vetor1))
            ]
        )

    return vetor1, vetor2


def soma_vetores(vetor1: list, vetor2: list) -> list:
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2)

    return [vetor1[i] + vetor2[i] for i in range(len(vetor1))]


def subtrai_vetores(vetor1: list, vetor2: list) -> list:
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2)

    return [vetor1[i] - vetor2[i] for i in range(len(vetor1))]


def multiplica_vetores(vetor1: list, vetor2: list) -> list:
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2, compesador=1)

    return [vetor1[i] * vetor2[i] for i in range(len(vetor1))]


def divide_vetores(vetor1: list, vetor2: list) -> list:
    vetor1, vetor2 = padronizar_vetores(
        vetor1, vetor2, compesador=1, divisao=True)

    return [vetor1[i] // vetor2[i] for i in range(len(vetor1))]


def multiplicao_escalar(vetor: list, escalar: int) -> list:
    return [i * escalar for i in vetor]


def n_duplicacao(vetor: list, n: int) -> list:
    return vetor * n


def soma_elementos(vetor: list) -> int:
    soma: int = 0

    for i in vetor:
        soma += i

    return soma


def produto_interno(vetor1: list, vetor2: list) -> int:
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2, compesador=1)
    soma: int = 0

    for i in range(len(vetor1)):
        soma += vetor1[i] * vetor2[i]

    return soma


def multiplica_todos(vetor1: list, vetor2: list) -> list:
    vetor_resultado: list = []

    for i in vetor1:
        soma_temporaria: int = 0

        for j in vetor2:
            soma_temporaria += i * j

        vetor_resultado.append(soma_temporaria)

    return vetor_resultado


def correlacao_cruzada(vetor: list, mascara: list) -> list:
    vetor_resultado: list = []

    for i in range(len(vetor) - len(mascara) + 1):
        soma_temporaria: int = 0

        for j in range(len(mascara)):
            soma_temporaria += vetor[i + j] * mascara[j]

        vetor_resultado.append(soma_temporaria)

    return vetor_resultado


def main() -> None:
    vetor = list(map(int, input().split(",")))

    while True:
        linha = input()

        if linha == "fim":
            break

        vetor2 = list(map(int, input().split(",")))

        if linha == "soma_vetores":
            vetor = soma_vetores(vetor, vetor2)
            print(vetor)
        elif linha == "subtrai_vetores":
            vetor = subtrai_vetores(vetor, vetor2)
            print(vetor)
        elif linha == "multiplica_vetores":
            vetor = multiplica_vetores(vetor, vetor2)
            print(vetor)
        elif linha == "divide_vetores":
            vetor = divide_vetores(vetor, vetor2)
            print(vetor)
        elif linha == "multiplicacao_escalar":
            vetor = multiplicao_escalar(vetor, vetor2[0])
            print(vetor)
        elif linha == "n_duplicacao":
            vetor = n_duplicacao(vetor, vetor2[0])
            print(vetor)
        elif linha == "soma_elementos":
            print(f"[{soma_elementos(vetor)}]")
        elif linha == "produto_interno":
            print(f"[{produto_interno(vetor, vetor2)}]")
        elif linha == "multiplica_todos":
            vetor = multiplica_todos(vetor, vetor2)
            print(vetor)
        elif linha == "correlacao_cruzada":
            vetor = correlacao_cruzada(vetor, vetor2)
            print(vetor)


if __name__ == "__main__":
    main()
