def padronizar_vetores(
    vetor1: list[int],
    vetor2: list[int],
    compesador: int = 0,
    divisao: bool = False
) -> tuple[list[int], list[int]]:
    """
    Função responsavel por padronizar dois vetores de tamanho distintos
    seguindo algum criterio pre definido, o parametro compesador e o valor
    a ser adicionado nas posições extras do vetor menor e divisão indica
    que a operação a ser realizada com os vetores e uma divisão e a ordem
    do maior e menor tem importancia. Retorna 2 vetores com o mesmo tamanho
    """
    if len(vetor1) > len(vetor2):
        # Se o vetor 1 for o maior extende o segundo com a
        # quantidade de casas da diferença
        vetor2.extend([
            compesador for _ in range(len(vetor1) - len(vetor2))
        ])
    elif len(vetor1) < len(vetor2):
        # Se o vetor 2 for o maior extende o segundo com a
        # quantidade de casas da diferença
        vetor1.extend(
            [abs(compesador - divisao)  # transforma 0 em 1 e 1 em 0
             for _ in range(len(vetor2) - len(vetor1))]
        )

    return vetor1, vetor2


def soma_vetores(vetor1: list[int], vetor2: list[int], escalar: int = 1) \
        -> list[int]:
    """
    Função responsavel por realizar a soma de dois vetores, o parametro escalar
    e o escalar por qual os elementos do segundo vetor serão multiplicados
    antes de serem somados. Retorna um unico vetor onde cada posição e a soma
    dos dois valores de mesma posição nos vetores recebidos
    """
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2)

    return [vetor1[i] + (escalar * vetor2[i]) for i in range(len(vetor1))]


def subtrai_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """
    Subtrai um vetor de outro, utiliza a soma com um escalar -1 multiplicado
    ao segundo vetor. retorna um unico vetor onde cada posição e a subtração
    dos dois valores de mesma posição nos vetores recebidos
    """
    return soma_vetores(vetor1, vetor2, escalar=-1)


def multiplica_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """
    Mutiplica 2 vetores. retorna um unico vetor onde cada posição e a
    multiplicação dos dois valores de mesma posição nos vetores recebidos
    """
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2, compesador=1)

    return [vetor1[i] * vetor2[i] for i in range(len(vetor1))]


def divide_vetores(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """
    Divide 2 vetores. retorna um unico vetor onde cada posição e a divisão
    dos dois valores de mesma posição nos vetores recebidos
    """
    vetor1, vetor2 = padronizar_vetores(
        vetor1, vetor2, compesador=1, divisao=True)

    return [vetor1[i] // vetor2[i] for i in range(len(vetor1))]


def multiplicacao_escalar(vetor: list[int], escalar: int) -> list[int]:
    """
    Multiplica os valores de todas as posições de um vetor por um escalar
    interio. Retorna um vetor onde cada posição corresponde a posição do
    vetor incial vezes o escalar
    """
    return [i * escalar for i in vetor]


def n_duplicacao(vetor: list[int], n: int) -> list[int]:
    """
    Duplica um vetor n vezes. O retorno e um vetor n vezes maior
    """
    return vetor * n


def soma_elementos(vetor: list[int]) -> int:
    """
    Soma todos os elementos de um vetor em um unico valor,
    retorna um valor inteiro com a soma do vetor
    """
    soma: int = 0

    for i in vetor:
        soma += i

    return soma


def produto_interno(vetor1: list[int], vetor2: list[int]) -> int:
    """
    Realiza o produto interno de 2 vetores. Retorna um valor inteiro
    correspondente ao valor do produto interno dos dois vetores
    """
    vetor1, vetor2 = padronizar_vetores(vetor1, vetor2, compesador=1)
    soma: int = 0

    for i in range(len(vetor1)):
        soma += vetor1[i] * vetor2[i]

    return soma


def multiplica_todos(vetor1: list[int], vetor2: list[int]) -> list[int]:
    """
    Multiplica todos os elementos de 2 vetores de forma a cobrir todas as
    possibilidades de multiplicação e gera um vetor novo, onde cada posição
    e o somatorio do valor da posição corresponte no vetor1 vezes cada elemento
    no vetor2
    """
    vetor_resultado: list[int] = []

    for i in vetor1:
        soma_temporaria: int = 0

        for j in vetor2:
            soma_temporaria += i * j

        vetor_resultado.append(soma_temporaria)

    return vetor_resultado


def correlacao_cruzada(vetor: list[int], mascara: list[int]) -> list[int]:
    """
    Realiza a correlação cruzada entre um vetor e uma mascara
    """
    vetor_resultado: list[int] = []

    for i in range(len(vetor) - len(mascara) + 1):
        soma_temporaria: int = 0

        for j in range(len(mascara)):
            soma_temporaria += vetor[i + j] * mascara[j]

        vetor_resultado.append(soma_temporaria)

    return vetor_resultado


def main() -> None:
    """
    Função principal responsavel pela execução do programa
    """
    vetor = list(map(int, input().split(",")))

    while True:
        # Repete infinitamente até ser parado por um brake
        linha = input()

        if linha == "fim":  # Para o programa
            break

        if linha == "soma_elementos":
            vetor = [soma_elementos(vetor)]
            print(vetor)
            continue

        vetor2 = list(map(int, input().split(",")))

        if linha == "soma_vetores":
            vetor = soma_vetores(vetor, vetor2)
        elif linha == "subtrai_vetores":
            vetor = subtrai_vetores(vetor, vetor2)
        elif linha == "multiplica_vetores":
            vetor = multiplica_vetores(vetor, vetor2)
        elif linha == "divide_vetores":
            vetor = divide_vetores(vetor, vetor2)
        elif linha == "multiplicacao_escalar":
            vetor = multiplicacao_escalar(vetor, vetor2[0])
        elif linha == "n_duplicacao":
            vetor = n_duplicacao(vetor, vetor2[0])
        elif linha == "produto_interno":
            vetor = [produto_interno(vetor, vetor2)]
        elif linha == "multiplica_todos":
            vetor = multiplica_todos(vetor, vetor2)
        elif linha == "correlacao_cruzada":
            vetor = correlacao_cruzada(vetor, vetor2)

        print(vetor)


if __name__ == "__main__":
    main()
