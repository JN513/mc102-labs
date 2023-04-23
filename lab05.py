def join(lista: list, sum: str = "") -> str:
    """
    Função para converter uma lista em uma string,
    concatecando cada elemento ao final de uma string
    """
    str_temp = str(lista[0])

    for i in range(1, len(lista)):
        str_temp += f"{sum}{lista[i]}"

    return str_temp


def swap(a: int, b: int) -> tuple:
    """
    Função para realizar a troca de valores entre duas variaveis,
    A recebe o valor de B e B recebe o valor de A
    """
    temp = a
    a = b
    b = temp

    return a, b


def reverter(genoma: str, i: int, j: int) -> str:
    """
    Função para reverter uma pedaço da string, o valor da posicao i vai para j e vice versa
    """
    if j >= len(genoma):
        j = len(genoma) - 1

    if i >= len(genoma):
        return genoma

    genoma = list(genoma)

    while True:
        genoma[i], genoma[j] = swap(genoma[i], genoma[j])

        j -= 1
        i += 1

        if i >= j:
            break

    return join(genoma)


def transpor(genoma: str, i: int, j: int, k: int) -> str:
    """
    Função para inverter dois intervalos distintos de texto em uma string
    """
    part1 = ""  # String com o primeiro intervalo
    part2 = ""  # String com o segundo intervalo

    if i > len(genoma) - 1:
        return genoma

    for y in range(i, j + 1):
        part1 += genoma[y]

    if j < len(genoma):
        if k > len(genoma):
            k = len(genoma) - 1

        for y in range(j + 1, k + 1):
            part2 += genoma[y]

    return genoma[:i] + part2 + part1 + genoma[k + 1 :]


def combinar(genoma: str, g: str, i: int):
    """
    Função para inserir uma string g em uma posição especifica de outra string
    """
    return genoma[:i] + g + genoma[i:]


def concatenar(genoma: str, g: str) -> str:
    """
    Função para inserir uma string no final de outra
    """
    return genoma + g


def remover(genoma: str, i: int, j: int) -> str:
    """
    Função para remover os elementos de um intevalo de especifico em uma string
    """
    return genoma[:i] + genoma[j + 1 :]


def transpor_e_reverter(genoma: str, i: int, j: int, k: int) -> str:
    """
    Função para inverter dois intervalos distintos de texto em uma string
    e apos isso inverter a soma dos dois intervalos invertidos
    """
    genoma = transpor(genoma, i, j, k)

    return reverter(genoma, i, k)


def buscar(genoma: str, g: str) -> int:
    """
    Busca e verifica quantas vezes uma string especifica esta contida dentro de outra string
    """
    qtd, i = (
        0,
        0,
    )  # variavel com a quantidade de aparições de g em genoma, e i o interador

    while True:
        if i + len(g) > len(genoma):
            break

        ok = True  # Verificador se g está contido nesse intervalo de genoma

        for k in range(i, i + len(g)):
            if g[k - i] != genoma[k]:
                ok = False
                break

        if (
            ok
        ):  # se achou ele pula esse intervalo que e igual a g, se não ele apenas verifica apartir da proxima posição
            qtd += 1
            i += len(g)
        else:
            i += 1

    return qtd


def buscar_bidirecional(genoma: str, g: str) -> int:
    """
    Busca e verifica quantas vezes uma string especifica esta
    contida dentro de outra string e realiza o mesmo com o inverso
    """
    r = buscar(genoma, g)

    genoma = reverter(genoma, 0, len(genoma) - 1)

    return r + buscar(genoma, g)


def main() -> None:
    """
    Função principal do programa
    """
    genoma = input()  # Realiza a leitura do genoma

    while True:  # Executa infinitamente até receber uma condição de parada
        linha = input().split()  # Realiza a leitura da linha

        if linha[0] == "sair":
            break
        elif linha[0] == "reverter":
            genoma = reverter(genoma, int(linha[1]), int(linha[2]))
        elif linha[0] == "transpor":
            genoma = transpor(genoma, int(linha[1]), int(linha[2]), int(linha[3]))
        elif linha[0] == "combinar":
            genoma = combinar(genoma, linha[1], int(linha[2]))
        elif linha[0] == "concatenar":
            genoma = concatenar(genoma, linha[1])
        elif linha[0] == "remover":
            genoma = remover(genoma, int(linha[1]), int(linha[2]))
        elif linha[0] == "transpor_e_reverter":
            genoma = transpor_e_reverter(
                genoma, int(linha[1]), int(linha[2]), int(linha[3])
            )
        elif linha[0] == "buscar":
            print(buscar(genoma, linha[1]))
        elif linha[0] == "buscar_bidirecional":
            print(buscar_bidirecional(genoma, linha[1]))
        elif linha[0] == "mostrar":
            print(genoma)


if (
    __name__ == "__main__"
):  # Verifica se o meu programa não está sendo utilizado como modulo
    main()
