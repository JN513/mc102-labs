from dataclasses import dataclass


class Flecha:
    def __init__(self, tipo: str, quantidade: int) -> None:
        self.tipo: str = tipo
        self.quatidade: int = quantidade
        self.quantidade_inicial: int = quantidade

    def resetar_quantidade(self):
        self.quatidade = self.quantidade_inicial


@dataclass
class Parte:
    nome: str
    fraqueza: str
    dano_maximo: int
    coordenadas: tuple[int, int]


class Maquina:
    def __init__(
        self,
        pts_vida: int,
        pts_ataque: int,
        num_partes: int,
        partes: dict[str, Parte] = {},
    ) -> None:
        self.pts_vida: int = pts_vida
        self.pts_ataque: int = pts_ataque
        self.num_partes: int = num_partes
        self.partes: dict[str, Parte] = partes

    def adicionar_parte(self, nome, fraqueza, dano_maximo, coordenadas) -> None:
        self.partes[nome] = Parte(
            nome=nome,
            fraqueza=fraqueza,
            dano_maximo=dano_maximo,
            coordenadas=coordenadas,
        )

    def adicionar_parte_by_object(self, parte: Parte) -> None:
        self.partes[parte.nome] = parte

    def adicionar_partes(self, partes: list[Parte]) -> None:
        for i in partes:
            self.partes[i.nome] = i

    def dano(
        self, parte: str, coordenada: tuple[int, int], tipo: str
    ) -> tuple[int, bool]:
        dano = self.partes[parte].dano_maximo - (
            abs(self.partes[parte].coordenadas[0] - coordenada[0])
            + abs(self.partes[parte].coordenadas[1] - coordenada[1])
        )
        if tipo == parte:
            self.pts_vida -= dano
            return dano, dano == self.partes[parte].dano_maximo
        else:
            self.pts_vida -= dano // 2
            return dano // 2, 0


class Player:
    def __init__(
        self, pts_vida: int, flechas: dict[Flecha] = {}, string_to_parse: str = ""
    ) -> None:
        self.pts_vida: int = pts_vida
        self.flechas: dict[Flecha] = flechas

        if string_to_parse:
            self.parse_flechas_by_string(string_to_parse)

    def parse_flechas_by_string(self, string_to_parse: str = "") -> None:
        lista: list[str] = string_to_parse.split()

        for i in range(0, len(lista), 2):
            self.flechas[lista[i]] = Flecha(
                tipo=lista[i], quantidade=int(lista[i + 1]))

    def recolher_flechas(self) -> None:
        for flecha in self.flechas.keys():
            self.flechas[flecha].resetar_quantidade()


maquinas: list[Maquina] = []


def main() -> None:
    global maquinas
    pts_vida: int = int(input())
    flechas_str: str = input()

    aloy = Player(pts_vida=pts_vida, string_to_parse=flechas_str)

    num_maquinas: int = int(input())

    num_maquinas_combate: int = int(input())

    for i in range(num_maquinas_combate):
        v, p, q = list(map(int, input().split()))

        maquinas.append(Maquina(pts_vida=v, pts_ataque=p, num_partes=q))

        for _ in range(q):
            nome_parte, fraqueza, dano_maximo, cx, cy = input().split(",")

            coordenadas: tuple[int, int] = (int(cx.strip()), int(cy.strip()))

            maquinas[i].adicionar_parte_by_object(
                Parte(
                    nome=nome_parte,
                    fraqueza=fraqueza,
                    dano_maximo=dano_maximo,
                    coordenadas=coordenadas,
                )
            )

    indice: int = 0

    while True:
        informarcoes_ataque = input().split(",")

        indice += 1

        unidade_alvo = int(informarcoes_ataque[0])
        parte_alvo = informarcoes_ataque[1]
        coordenada = (informarcoes_ataque[2], informarcoes_ataque[3])

        print(f"Combate {indice}, vida = {aloy.pts_vida}")

        dano, foi_critico = maquinas[unidade_alvo].dano(parte_alvo, coordenada)

        if maquinas[unidade_alvo].pts_vida <= 0:
            print(f"Maquina {unidade_alvo} derrotada")

        print(f"Vida após o combate = {aloy.pts_vida}")


if __name__ == "__main__":
    main()
