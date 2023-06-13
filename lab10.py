from dataclasses import dataclass
from math import floor


class Flecha:
    def __init__(self, tipo: str, quantidade: int) -> None:
        self.tipo: str = tipo
        self.quantidade: int = quantidade
        self.quantidade_inicial: int = quantidade

    def resetar_quantidade(self):
        self.quantidade = self.quantidade_inicial

    def foi_gasta(self) -> bool:
        return not self.quantidade == self.quantidade_inicial


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
        self.partes: dict[str, Parte] = partes.copy()

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
        dano = max(
            self.partes[parte].dano_maximo
            - (
                abs(self.partes[parte].coordenadas[0] - coordenada[0])
                + abs(self.partes[parte].coordenadas[1] - coordenada[1])
            ),
            0,
        )

        if (
            tipo == self.partes[parte].fraqueza
            or self.partes[parte].fraqueza == "todas"
        ):
            self.pts_vida = max(self.pts_vida - dano, 0)

            return dano, self.partes[parte].coordenadas == coordenada
        else:
            self.pts_vida = max(self.pts_vida - (dano // 2), 0)

            return dano // 2, self.partes[parte].coordenadas == coordenada

    def get_fraqueza(self, parte: str) -> str:
        return self.partes[parte].fraqueza


class Player:
    def __init__(
        self, pts_vida: int, flechas: dict[Flecha] = {}, string_to_parse: str = ""
    ) -> None:
        self.pts_vida: int = pts_vida
        self.max_vida: int = pts_vida
        self.flechas: dict[Flecha] = flechas
        self.estado: int = 0

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

    def usar_flecha(self, tipo: str) -> int:
        self.flechas[tipo].quantidade -= 1

        return self.flechas[tipo].quantidade

    def cura(self) -> None:
        self.pts_vida = min(
            self.pts_vida + floor(0.5 * self.max_vida), self.max_vida)

    def coletar_flechas(self) -> None:
        for i in self.flechas.keys():
            self.flechas[i].resetar_quantidade()

    def acabou_flecha(self) -> None:
        self.estado = 2

    def sem_flechas(self) -> bool:
        return self.estado == 2

    def morta(self) -> bool:
        return self.estado == 1

    def morreu(self) -> None:
        self.estado = 1

    def print_flechas_gastas(self):
        for i in self.flechas.keys():
            if self.flechas[i].foi_gasta():
                print(
                    f"- {self.flechas[i].tipo}: {self.flechas[i].quantidade_inicial - self.flechas[i].quantidade}/{self.flechas[i].quantidade_inicial}"
                )

    def tem_flechas(self) -> bool:
        for i in self.flechas.keys():
            if self.flechas[i].quantidade > 0:
                return True
        return False


maquinas: list[Maquina] = []


def tem_maquinas_vivas() -> bool:
    global maquinas

    for i in maquinas:
        if i.pts_vida > 0:
            return True

    return False


def get_dano_total() -> int:
    global maquinas

    dano: int = 0

    for i in maquinas:
        if i.pts_vida > 0:
            dano += i.pts_ataque

    return dano


def ler_maquinas(num_maquinas_combate: int) -> None:
    for i in range(num_maquinas_combate):
        vida, pts_ataque, num_partes = list(map(int, input().split()))

        maquinas.append(
            Maquina(pts_vida=vida, pts_ataque=pts_ataque, num_partes=num_partes))

        for _ in range(num_partes):
            nome_parte, fraqueza, dano_maximo, cx, cy = input().split(",")

            coordenadas: tuple[int, int] = (
                int(cx.strip()), int(cy.strip()))

            maquinas[i].adicionar_parte_by_object(
                Parte(
                    nome=nome_parte.strip(),
                    fraqueza=fraqueza.strip(),
                    dano_maximo=int(dano_maximo.strip()),
                    coordenadas=coordenadas,
                )
            )


def combate(aloy: Player) -> dict[int, dict[tuple[int, int], int]]:
    global maquinas
    interator: int = 0
    criticos: dict[int, dict[tuple[int, int], int]] = {}

    while True:
        interator += 1

        informarcoes_ataque = input().split(",")

        unidade_alvo = int(informarcoes_ataque[0].strip())
        parte_alvo = informarcoes_ataque[1].strip()
        flecha_usada = informarcoes_ataque[2].strip()
        coordenada = (
            int(informarcoes_ataque[3].strip()),
            int(informarcoes_ataque[4].strip()),
        )

        qtd = aloy.usar_flecha(flecha_usada)

        if qtd < 0:
            aloy.acabou_flecha()
            break

        dano, foi_critico = maquinas[unidade_alvo].dano(
            parte_alvo, coordenada, flecha_usada
        )

        if foi_critico:
            if unidade_alvo in criticos.keys():
                if coordenada in criticos[unidade_alvo].keys():
                    criticos[unidade_alvo][coordenada]["qtd"] += 1
                else:
                    criticos[unidade_alvo][coordenada] = {
                        "qtd": 1,
                        "parte": parte_alvo,
                    }
            else:
                criticos[unidade_alvo] = {}
                criticos[unidade_alvo][coordenada] = {
                    "qtd": 1, "parte": parte_alvo}

        if maquinas[unidade_alvo].pts_vida <= 0:
            print(f"Máquina {unidade_alvo} derrotada")

        if not tem_maquinas_vivas():
            break

        if interator % 3 == 0:
            dano = get_dano_total()

            aloy.pts_vida = max(aloy.pts_vida - dano, 0)

        if aloy.pts_vida <= 0:
            aloy.morreu()
            break

        if not aloy.tem_flechas():
            aloy.acabou_flecha()
            break

    return criticos


def main() -> None:
    global maquinas
    pts_vida: int = int(input())
    flechas_str: str = input()

    aloy = Player(pts_vida=pts_vida, string_to_parse=flechas_str)

    num_maquinas: int = int(input())

    indice: int = 0

    while num_maquinas:
        maquinas.clear()

        # Lendo as maquinas
        num_maquinas_combate: int = int(input())

        num_maquinas -= num_maquinas_combate

        ler_maquinas(num_maquinas_combate)

        # Hora do combate

        print(f"Combate {indice}, vida = {aloy.pts_vida}")

        indice += 1

        criticos: dict[int, dict[tuple[int, int], int]] = combate(aloy)

        print(f"Vida após o combate = {aloy.pts_vida}")

        if aloy.morta():
            print("Aloy foi derrotada em combate e não retornará a tribo.")
            break
        elif aloy.sem_flechas():
            print("Aloy ficou sem flechas e recomeçará sua missão mais preparada.")
            break
        else:
            print("Flechas utilizadas:")
            aloy.print_flechas_gastas()

            if len(criticos) > 0:
                print("Críticos acertados:")

                for k in sorted(criticos.keys()):
                    print(f"Máquina {k}:")

                    items_list = [item for item in criticos[k].items()]
                    items_list = sorted(
                        items_list, key=lambda x: x[1]["parte"])

                    for w in items_list:
                        print(f"- {w[0]}: {w[1]['qtd']}x")

        aloy.coletar_flechas()
        aloy.cura()

    if not aloy.morta() and not aloy.sem_flechas():
        print("Aloy provou seu valor e voltou para sua tribo.")


if __name__ == "__main__":
    main()
