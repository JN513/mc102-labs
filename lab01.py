def ganhou(e1: str, e2: str) -> bool:
    if e1 == "tesoura" and e2 == "papel":
        return 1
    if e1 == "papel" and e2 == "pedra":
        return 1
    if e1 == "pedra" and e2 == "lagarto":
        return 1
    if e1 == "spock" and e2 == "tesoura":
        return 1
    if e1 == "tesoura" and e2 == "lagarto":
        return 1
    if e1 == "lagarto" and e2 == "papel":
        return 1
    if e1 == "papel" and e2 == "spock":
        return 1
    if e1 == "spock" and e2 == "pedra":
        return 1
    if e1 == "pedra" and e2 == "tesoura":
        return 1

    return 0


es = input()
er = input()


r1 = ganhou(es, er)
r2 = ganhou(er, es)

if r1:
    print("Interestelar")
elif r2:
    print("Jornada nas Estrelas")
else:
    print("empate")
