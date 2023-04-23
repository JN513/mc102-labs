import sys

sys.stdout.reconfigure(encoding="utf-8")

print(
    "Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação."
)


def print_options(include_two: bool = False) -> None:
    print("(0) Não\n(1) Sim")
    if include_two:
        print("(2) Sim, realizo testes e invasão de sistemas")


line = input("Seu SO anterior era Linux?\n")
print_options()

if line == "1":
    line = input("É programador/ desenvolvedor ou de áreas semelhantes?\n")
    print_options(1)
    if line == "1":
        line = input(
            "Gostaria de algo pronto para uso ao invés de ficar configurando o SO?\n"
        )
        print_options()
        if line == "1":
            line = input("Já utilizou Debian ou Ubuntu?\n")
            print_options()
            if line == "1":
                print(
                    "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Manjaro, ApricityOS."
                )
            elif line == "0":
                print(
                    "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: OpenSuse, Ubuntu Mint, Ubuntu Mate, Ubuntu."
                )
            else:
                print("Opção inválida, recomece o questionário.")
        elif line == "0":
            line = input("Já utilizou Arch Linux?\n")
            print_options()
            if line == "1":
                print(
                    "Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições: Gentoo, CentOS, Slackware."
                )
            elif line == "0":
                print(
                    "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Antergos, Arch Linux."
                )
            else:
                print("Opção inválida, recomece o questionário.")
        else:
            print("Opção inválida, recomece o questionário.")
    elif line == "2":
        print(
            "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Kali Linux, Black Arch."
        )
    elif line == "0":
        print(
            "Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são: Ubuntu Mint, Fedora."
        )
    else:
        print("Opção inválida, recomece o questionário.")
elif line == "0":
    line = input("Seu SO anterior era um MacOS?\n")
    print_options()

    if line == "1":
        print(
            "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: ElementaryOS, ApricityOS."
        )
    elif line == "0":
        print(
            "Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são: Ubuntu Mate, Ubuntu Mint, Kubuntu, Manjaro."
        )
    else:
        print("Opção inválida, recomece o questionário.")
else:
    print("Opção inválida, recomece o questionário.")
