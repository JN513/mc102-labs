from typing import Any


class Flecha:
    def __init__(self, tipo: str, quantidade: int) -> None:
        self.tipo: str = tipo
        self.quatidade: int = quantidade
        self.quantidade_inicial: int = quantidade

    def resetar_quantidade(self):
        self.quatidade = self.quantidade_inicial


class Maquina:
    def __init__(
        self, pts_vida: int, pts_ataque: int, num_partes: int, partes: list[Any] = []
    ) -> None:
        self.pts_vida: int = pts_vida
        self.pts_ataque: int = pts_ataque
        self.num_partes: int = num_partes
        self.partes: list[Any] = partes

    def adicionar_parte(self):
        ...


class Player:
    def __init__(
        self, pts_vida: int, flechas: list[Flecha] = [], string_to_parse: str = ""
    ) -> None:
        self.pts_vida = pts_vida
        self.flechas = flechas

        if string_to_parse:
            self.parse_flechas_by_string(string_to_parse)

    def parse_flechas_by_string(self, string_to_parse: str = "") -> None:
        lista: list[str] = string_to_parse.split()

        for i in range(0, len(lista), 2):
            self.flechas.append(
                Flecha(tipo=lista[i], quantidade=int(lista[i + 1])))

    def recolher_flechas(self) -> None:
        for flecha in self.flechas:
            flecha.resetar_quantidade()


maquinas: list[Maquina] = []


def main() -> None:
    global maquinas
    pts_vida: int = int(input())
    flechas_str: str = input()

    aloy = Player(pts_vida=pts_vida, flechas=flechas_str)

    num_maquinas: int = int(input())

    num_maquinas_combate: int = int(input())

    for i in range(num_maquinas):
        maquinas.append(Maquina())


if __name__ == "__main__":
    main()
