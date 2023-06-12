from typing import Any, Callable


def mergeSort(
    vetor: list[Any], funcao: Callable[[Any, Any], bool] = lambda x, y: x < y
) -> list[Any]:
    if len(vetor) > 1:
        meio: int = len(vetor) // 2
        primeira_metade: list[Any] = vetor[:meio]
        segunda_metade: list[Any] = vetor[meio:]

        primeira_metade = mergeSort(primeira_metade, funcao)
        segunda_metade = mergeSort(segunda_metade, funcao)

        i: int = 0
        j: int = 0
        k: int = 0

        while i < len(primeira_metade) and j < len(segunda_metade):
            if funcao(primeira_metade[i], segunda_metade[j]):
                vetor[k] = primeira_metade[i]
                i += 1
            else:
                vetor[k] = segunda_metade[j]
                j += 1
            k += 1

        while i < len(primeira_metade):
            vetor[k] = primeira_metade[i]
            i += 1
            k += 1

        while j < len(segunda_metade):
            vetor[k] = segunda_metade[j]
            j += 1
            k += 1

    return vetor


def binarySearch(vetor: list[int], item: Any, inicio: int = 0, fim: int = None) -> int:
    fim = len(vetor) if fim is None else fim
    meio: int = inicio + (fim - inicio) // 2

    print(f"meio: {meio}, li {vetor}, ini {inicio}, fi: {fim}")

    if inicio > fim:
        return -1

    if vetor[meio] == item:
        return meio

    else:
        if vetor[meio] > item:
            return binarySearch(vetor, item, inicio=inicio, fim=meio)

        elif vetor[meio] < item:
            return binarySearch(vetor, item, inicio=meio, fim=fim)

    return -1


# l = [(10, 2), (2, 10), (2, 5), (5, 2), (8, 9), (9, 8), (10, 1)]
# print(mergeSort(l, lambda x, y: x[1] < y[1]))


class Jogador:
    def __init__(self, cartas: list[str]) -> None:
        self.cartas = cartas


def main() -> None:
    ...


if __name__ == "__main__":
    main()
