def join(lista: list, sum: str = "") -> str:
    str_temp = str(lista[0])

    for i in range(1, len(lista)):
        str_temp += f"{sum}{lista[i]}"

    return str_temp


dias = int(input())

for k in range(dias):  # Percorre todos os dias
    numero_de_animais_que_brigam = int(input())

    brigas = []
    procedimentos = {}
    animais_atendidos = []
    animais_n_atendidos = []
    sv_invalido = []
    qtd_brigas = 0
    animais = []

    for _ in range(numero_de_animais_que_brigam):
        brigas.append(input().split())

    procedimentos_qtd = (
        input().split()
    )  # entrada com procedimentos e quantidades de cada
    numero_de_atendimentos_requisitados = int(input())

    for i in range(0, len(procedimentos_qtd), 2):
        procedimentos[procedimentos_qtd[i]] = int(procedimentos_qtd[i + 1])
        """
        Como a entrada e uma especie de chave valor a cada 2 elementos, 
        digo que a os elementos impare são as chaves e os pares os valores, e percorro minha lista 2 a 2
        """

    animais_procedimentos = []

    for _ in range(numero_de_atendimentos_requisitados):
        animal = input().split()
        animais.append(animal[0])

        if animal[1] in procedimentos.keys():
            if procedimentos[animal[1]] > 0:
                procedimentos[animal[1]] -= 1

                animais_atendidos.append(animal[0])

            else:
                animais_n_atendidos.append(animal[0])
        else:
            sv_invalido.append(animal[0])

    for i in brigas:
        if i[0] in animais and i[1] in animais:
            qtd_brigas += 1

    print(f"Dia: {k+1}\nBrigas: {qtd_brigas}")

    if len(animais_atendidos):
        print(f"Animais atendidos: {join(animais_atendidos, ', ')}")

    if len(animais_n_atendidos):
        print(f"Animais não atendidos: {join(animais_n_atendidos, ', ')}")

    for i in sv_invalido:
        print(f"Animal {i} solicitou procedimento não disponível.")

    if k != dias - 1:
        print()
