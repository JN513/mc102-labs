# Vetores responsaveis por permitir o movimento em volta de um ponto
direction_x = [-1, 0, 1, 0]
direction_y = [0, -1, 0, 1]
matriz: list[list[str]]  # Matriz com a representação da sala

# Quantas posições o robo percorreu que seriam as proximas no caminho
nexts_positions: int = 0


def verifica_pos(y: int, x: int) -> bool:
    """Função responsavel por verificar se o
    ponto que estou esta dentro da matriz

    Args:
        y (int): indice da linha atual
        x (int): indice da coluna atual

    Returns:
        bool: True se o ponto esta na matriz e False caso contrario
    """
    global matriz

    return y < len(matriz) and x < len(matriz[0]) and y >= 0 and x >= 0


def get_next_positon(y: int, x: int) -> tuple[int, int]:
    """Retorna a proxima posição que o robo deve ir
      seguindo o padrão de movimento estabelecido

    Args:
        y (int): indice da linha atual
        x (int): indice da coluna atual

    Returns:
        tuple[int, int]: Retorna o indice da linha e da coluna
        da proxima posição a se visitar
    """
    size = len(matriz[0])
    if y % 2 == 0:  # Se estou em uma linha par avanço para direita
        if x == size - 1:
            return y + 1, x
        else:
            return y, x + 1
    else:  # Se for impar avanço para esquerda
        if x == 0:
            return y + 1, x
        else:
            return y, x - 1


def is_next_position(y: int, x: int, a: int, b: int) -> bool:
    """Função responsavel por verificar se um ponto
    e o proximo ponto da verificação

    Args:
        y (int): indice da linha atual
        x (int): indice da coluna atual
        a (int): indice da linha do ponto que quero saber se e o proximo
        b (int): indice da coluna do ponto que quero saber se e o proximo

    Returns:
        bool: True se o ponto e o proximo ponto a partir do ponto atual
        False caso contrario
    """
    return (a, b) == get_next_positon(y, x)


def print_matriz() -> None:
    """Função responsavel por printar a matriz"""
    global matriz

    for linha in matriz:
        print(" ".join(linha))

    print()


def check(y: int, x: int, interator: int = 0) -> tuple[int, int]:
    """Função responsavel por verificar os pontos vizinhos a um ponto

    Args:
        y (int): indice da linha atual
        x (int): indice da coluna atual
        interator (int, optional):
        algumento para contabilizar a minha profundidad atual. Defaults to 0.

    Returns:
        tuple[int, int]: retorno o ponto que final no qual parei
    """
    global matriz
    global nexts_positions
    a: int = y
    b: int = x

    # Marco o ponto atual como visitado
    matriz[y][x] = "."

    # Verifico os 4 vizinhos
    for i in range(4):
        dir_xi = x + direction_x[i]
        dir_yi = y + direction_y[i]

        # Olho se o ponto esta dentro do intervalo
        if not verifica_pos(dir_yi, dir_xi):
            continue

        # Se o ponto que estou olhando e uma sujeira
        if matriz[dir_yi][dir_xi] == "o":
            # Verific se ele e o proximo ponto da sequencia,
            # se sim intero next_positions
            if (
                is_next_position(y, x, dir_yi, dir_xi)
            ) and nexts_positions == interator:
                nexts_positions += 1

            # Marco que estou nessa posição
            matriz[dir_yi][dir_xi] = "r"
            print_matriz()
            # Marco que ja passei por essa posição
            matriz[dir_yi][dir_xi] = "."

            # verifico os vizinhos desse ponto
            a, b = check(dir_yi, dir_xi, interator=interator + 1)

            # Retorno o ponto no qual a recursão parou
            return a, b
    # Retorno o proprio ponto caso ele não tenha ido em nenhum vizinho
    return a, b


def voltar(y: int, x: int, a: int, b: int) -> None:
    """Função responsavel por voltar a posição
    no qual o robo começou a limpar a sujeira

    Args:
        y (int): indice da linha que ele precisa voltar
        x (int): indice da coluna que ele precisa voltar
        a (int): indice da linha atual
        b (int): indice da coluna atual
    """
    global matriz
    voltas: int = 1

    i = 0

    # Repito o processo enquanto eu precisar estar voltando
    while i < voltas:
        i += 1
        if b > x:  # Se a coluna que o robo esta, esta a frente da inicial
            while b > x:
                # Repito até voltar a coluna x

                matriz[a][b] = "."

                b -= 1

                matriz[a][b] = "r"

                print_matriz()

                # Verifico os pontos vizinhos do ponto que o robo esta
                k, d = check(a, b)

                # Se parei em um ponto diferente do atual reinicio o ciclo
                if (k, d) != (a, b):
                    # Começo a voltar à partir do novo ponto atual
                    a, b = k, d
                    voltas += 1
                    break
        elif b < x:  # Se a coluna que o robo esta, esta a atrás da inicial
            while b < x:
                # Repito até avançar a coluna x
                matriz[a][b] = "."

                b += 1

                matriz[a][b] = "r"

                print_matriz()

                # Verifico os pontos vizinhos do ponto que o robo esta
                k, d = check(a, b)

                # Se parei em um ponto diferente do atual reinicio o ciclo
                if (k, d) != (a, b):
                    # Começo a voltar à partir do novo ponto atual
                    a, b = k, d
                    voltas += 1
                    break

        # Se preciso reiniciar o processo de volta, reinicio o ciclo
        if voltas > i:
            continue

        # Se a linha que o robo esta, esta a abaixo da inicial
        while a > y:
            # Repito até subir a linha y
            matriz[a][b] = "."

            a -= 1

            matriz[a][b] = "r"

            print_matriz()

            # Verifico os pontos vizinhos do ponto que o robo esta
            k, d = check(a, b)

            # Se parei em um ponto diferente do atual reinicio o ciclo
            if (k, d) != (a, b):
                # Começo a voltar à partir do novo ponto atual
                a, b = k, d
                voltas += 1
                break


def varredura_horizontal(i: int, truncate: bool = False) -> None:
    """Função responsavel por realizar a varredura pelas colunas de uma linha

    Args:
        i (int): Linha atual
        truncate (bool, optional): Atributo usado para saber se e um caminho
        normal ou está retornando ao fim. Defaults to False.
    """
    global matriz
    global nexts_positions

    # Inicio e fim da linha
    start = 0
    end = len(matriz[0])

    # Ultimas posições
    lastx: int = 0
    lasty: int = 0

    # Sentido do movimeno
    passo = 1

    # Se a minha linha atual mais o truncate for par avanço para direita
    if (i + truncate % 2) == 0 and passo == -1:
        passo = 1
        start, end = end + 1, start + 1
    # Se a minha linha atual mais o truncate for impar avanço para esquerda
    elif (i + truncate) % 2 == 1 and passo == 1:
        passo = -1
        start, end = end - 1, start - 1

    # Percorro os elementos da linha
    for j in range(start, end, passo):
        # Verifico se já passei pelas proximas posições
        if nexts_positions:
            nexts_positions -= 1
            continue

        # Falo que a posição anterior já foi visitada
        matriz[lastx][lasty] = "."

        # Marco que o robo esta na posição atual
        matriz[i][j] = "r"

        # Se truncate for false e o robo não estiver no ponto inicial da linha
        if not (truncate and j == 0):
            print_matriz()

        # A posição atual agora sera a anterior
        lastx, lasty = i, j

        # Verifico os vizinhos da posição atual
        a, b = check(i, j)

        # Se a posição que o robo parou após a verificação for diferente
        # da atual e não for a proxima posição
        if (a != i or b != j) and not is_next_position(i, j, a, b):
            # Se eu já passei pelas proximas posições
            if nexts_positions:
                v, w = i, j

                # Marco as proximas posições como visitadas
                for _ in range(nexts_positions):
                    v, w = get_next_positon(v, w)

                    matriz[v][w] = "."

                # Volto pro ponto de partida do ultimo ponto da
                # sequencia que parei
                voltar(v, w, a, b)
                matriz[v][w] = "."
            else:
                # Volto pro ponto de partida do ultimo ponto da
                # sequencia que parei
                voltar(i, j, a, b)
                matriz[i][j] = "."


def varredura() -> None:
    """Função responsavel por realizar a varredura"""
    global matriz

    # Verifico todas as linhas
    for i in range(len(matriz)):
        varredura_horizontal(i)

    # Se a matriz for par passo outra varredura horizontal para
    # ir para ultima posição da matriz
    if len(matriz) % 2 != 1:
        varredura_horizontal(len(matriz) - 1, truncate=True)


def main() -> None:
    # Leio o numero de linhas da matriz
    numero_de_linhas: int = int(input())

    global matriz

    # Leio a matriz
    matriz = [input().split() for _ in range(numero_de_linhas)]

    # Inicio a varredura
    varredura()


# Inicio o algoritmo caso esse codigo não esteja sendo usado como modulo
if __name__ == "__main__":
    main()
