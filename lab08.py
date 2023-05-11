from typing import Any as any


def sorted_param(filme: dict[str, int]) -> tuple[int, int]:
    """Função utilizada para ordenar os filmes de uma determinada
    categoria, a função e utilizada apenas em um sorted

    Args:
        filme (dict[str, int]): Recebe um dicionario com chaves
        str e valores inteiros

    Returns:
        tuple[int, int]: retorna um tupla de dois inteiros
    """
    return -filme["pont"], -filme["qtd"]


def sort_filmes(filme: dict[str, int]) -> tuple[int, int]:
    """Função utilizada para ordenar os filmes de uma determinada
    categoria, a função e utilizada apenas em um sorted

    Args:
        filme (dict[str, int]): Recebe um dicionario com chaves
        str e valores inteiros

    Returns:
        tuple[int, int]: retorna um tupla de dois inteiros
    """
    return -filme["vitorias"], -filme["pont"]


def main() -> None:
    """
    Função principal utilizada para leitura e impressão dos dados
    """
    qtd_filmes_indicados: int = int(input())
    filmes: dict[str, dict[str, any]] = {}

    for _ in range(qtd_filmes_indicados):
        filme: str = input()

        filmes[filme.strip()] = {"vitorias": 0, "total_points": 0}

    qtd_avaliacoes: int = int(input())
    filmes_categoria: dict[str, dict[str, any]] = {}

    for _ in range(qtd_avaliacoes):
        avaliacao: list[str] = input().split(",")

        if avaliacao[-3].strip() in filmes[avaliacao[-2].strip()].keys():
            filmes[avaliacao[-2].strip()][avaliacao[-3].strip()] = [
                filmes[avaliacao[-2].strip()]
                [avaliacao[-3].strip()][0] +
                int(avaliacao[-1]),
                filmes[avaliacao[-2].strip()]
                [avaliacao[-3].strip()][1] + 1
            ]
        else:
            filmes[avaliacao[-2].strip()][avaliacao[-3].strip()
                                          ] = [int(avaliacao[-1]), 1]

        if not avaliacao[-3].strip() in filmes_categoria.keys():
            filmes_categoria[avaliacao[-3].strip()] = {
                "filmes": {avaliacao[-2].strip()},
                "vencedor": ""
            }
        else:
            filmes_categoria[avaliacao[-3].strip()
                             ]["filmes"].add(avaliacao[-2].strip())

    for i in filmes_categoria.keys():
        values: list[dict[str, any]] = [
            {"nome": key, "pont":
             filmes[key][i][0] / filmes[key][i][1],
             "qtd": filmes[key][i][1]}
            for key in filmes_categoria[i]["filmes"]
        ]

        values = sorted(values, key=sorted_param)

        filmes[values[0]["nome"]]["vitorias"] = \
            filmes[values[0]["nome"]]["vitorias"] + 1
        filmes_categoria[i]["vencedor"] = values[0]["nome"]

    for filme in filmes:
        points = 0

        for categoria in filmes[filme]:
            if categoria != "vitorias" and categoria != "total_points":
                points += filmes[filme][categoria][0] / \
                    filmes[filme][categoria][1]

        filmes[filme]["total_points"] = points

    values = [
        {"nome": filme, "pont": filmes[filme]["total_points"],
            "vitorias": filmes[filme]["vitorias"]}
        for filme in filmes
    ]

    values = sorted(values, key=sort_filmes)

    filmes_zerados: list[str] = [
        filme for filme in filmes if filmes[filme]["total_points"] == 0]

    filmes_categoria = dict(sorted(filmes_categoria.items()))

    print("#### abacaxi de ouro ####\n\ncategorias simples")

    dict_filme_keys: list[str] = list(filmes_categoria.keys())

    for index in range(1, len(dict_filme_keys)):
        print(
            f"categoria: {dict_filme_keys[index]}\n- "
            f"{filmes_categoria[dict_filme_keys[index]]['vencedor']}"
        )

    print(
        f"categoria: {dict_filme_keys[0]}\n- "
        f"{filmes_categoria[dict_filme_keys[0]]['vencedor']}\n\n"
        f"categorias especiais\nprêmio pior filme do ano\n- "
        f"{values[0]['nome']}\nprêmio não merecia estar aqui\n- ", end=""
    )

    if len(filmes_zerados):
        print(", ".join(filmes_zerados))
    else:
        print("sem ganhadores")


if __name__ == "__main__":
    main()
