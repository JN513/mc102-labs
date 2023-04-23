n = int(input())
jogadores = list(map(int, input().split()))
intervalos = list(map(int, input().split()))

meio = n // 2

if meio * 2 < n:
    meio += 1

index: int = 0

for i in range(0, meio):
    sum = intervalos[index + 1] - intervalos[index]
    jogadores[i] = jogadores[i] * sum

    jogadores[n - 1 - i] = jogadores[n - 1 - i] + (
        intervalos[len(intervalos) - index - 1]
        - intervalos[len(intervalos) - index - 2]
    )

    index += 2

index, value, qos = -1, -10000000, 0

for i, v in enumerate(jogadores):
    if v > value:
        index = i
        value = v
        qos = 0
    elif v == value:
        qos += 1

if qos:
    print("Rodada de cerveja para todos os jogadores!")
else:
    print(
        f"O jogador número {index+1} vai receber o melhor bolo da cidade pois venceu com {value} ponto(s)!"
    )
