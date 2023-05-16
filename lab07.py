def search_index(linha: str, element: str) -> int: 
    vogais = ("a", "e", "i", "o", "u")

    if element == "vogal":
        for i in range(len(linha)):
            if linha[i] in vogais:
                return i
    elif element == "consoante":
        for i in range(len(linha)):
            if (
                (ord(linha[i]) >= 65 and ord(linha[i]) <= 90)
                or (ord(linha[i]) >= 97 and ord(linha[i]) <= 122)
            ):
                return i
    elif len(element) > 1:
        for i in range(len(linha)):
            if ord(linha[i]) >= 48 and ord(linha[i]) <= 57:
                return i

    return linha.index(element)

def main() -> None:
    operador: str = input()
    operando1: str = input()
    operando2: str = input()

    n_linhas: int = int(input())

    linhas: list[str] = []
    linha: str = ""

    for _ in range(n_linhas):
        linhas.append(input())
        linha += linhas[-1]


    pos1: int = search_index(linha, operando1)
    pos2: int = search_index(linha[pos1:], operando2) + pos1

    key: int = 0

    if operador == "+":
        key = pos1 + pos2
    elif operador == "-":
        key = pos1 - pos2
    else:
        key = pos1 * pos2

    print(key)

    for j in range(len(linhas)):
        result: str = ""

        for i in range(len(linhas[j])):
            result += chr(32 + (ord(linhas[j][i]) - 32 + key) % 95)

        print(result)


if __name__ == "__main__":
    main()
