from typing import Any

mapa: list[list[str]] = []


class Monstro:
    def __init__(self, vida: int, dano: int, tipo: str, posicao: tuple[int]) -> None:
        self.vida = vida
        self.dano = dano
        self.tipo = tipo
        self.posica = posicao

    def dano(self, value: int) -> int:
        vida_temp = self.vida

        self.vida = min(self.vida - value, 0)

        return vida_temp - self.vida

    def mover(self):
        if self.tipo == "U":
            ...
        elif self.tipo == "D":
            ...
        elif self.tipo == "L":
            ...
        else:
            ...

        return self.posicao


class Objeto:
    def __init__(
        self, nome: str, tipo: str, posica: tuple[int, int], status: str
    ) -> None:
        self.nome = nome
        self.tipo = tipo
        self.posicao = posica
        self.status = status


class Player:
    def __init__(self, vida: int, dano: int, posicao: tuple[int, int]) -> None:
        self.vida = vida
        self.dano = dano
        self.posicao = posicao


class Mapa:
    def __init__(
        self,
        linhas: int,
        colunas: int,
        posicao_entrada: tuple[int, int],
        posicao_saida: tuple[int, int],
        objetos: dict[str, Objeto],
        posicoes_especiais: dict[tuple, list[tuple[Any, str]]],
        player=Player
    ) -> None:
        self.mapa = [["." for __ in range(colunas)] for _ in range(linhas)]

        self.mapa[posicao_entrada[0]][posicao_entrada[1]] = "P"
        self.mapa[posicao_saida[0]][posicao_saida[1]] = "*"

        self.posicao_entrada = posicao_entrada
        self.posicao_saida = posicao_saida

        self.objetos: dict[str, Objeto] = objetos
        self.posicoes_especiais: dict[tuple,
                                      list[tuple[Any, str]]] = posicoes_especiais

        self.link = player

        self.atualizar()

        self.printar()

    def printar(self):
        for linha in self.mapa:
            print(" ".join(linha))

        print()

    def atualizar(self):
        for i in self.posicoes_especiais.keys():
            x, y = i

            value = self.posicoes_especiais[i][0][0].tipo

            self.mapa[x][y] = value

    def run(self):
        ...


def main() -> None:
    vida_link, dano_link = list(map(int, input().split()))
    linhas, colunas = list(map(int, input().split()))

    objetos: dict[str, Objeto] = {}
    posicoes_especiais: dict[tuple, list[tuple[Any, str]]] = {}

    ponto_entrada = tuple(map(int, input().split(",")))

    ponto_saida = tuple(map(int, input().split(",")))

    link = Player(vida_link, dano_link, ponto_entrada)

    num_monstros: int = int(input())

    for _ in range(num_monstros):
        vida, ataque, tipo, posicao = input().split()
        vida = int(vida)
        ataque = int(ataque)
        posicao = tuple(map(int, posicao.split(",")))

        monstro = Monstro(vida, ataque, tipo, posicao)

        if not posicao in posicoes_especiais:
            posicoes_especiais[posicao] = [(monstro, "m")]
        else:
            posicoes_especiais[posicao].append((monstro, "m"))

    num_objetos: int = int(input())

    for _ in range(num_objetos):
        nome, tipo, posicao, status = input().split()

        posicao = tuple(map(int, posicao.split(",")))

        objeto = Objeto(nome, tipo, posicao, status)

        objetos[objeto.nome] = objeto

        if not posicao in posicoes_especiais:
            posicoes_especiais[posicao] = [(objeto, "o")]
        else:
            posicoes_especiais[posicao].append((objeto, "o"))

    mapa = Mapa(linhas, colunas, ponto_entrada, ponto_saida,
                objetos, posicoes_especiais, link)


if __name__ == "__main__":
    main()
