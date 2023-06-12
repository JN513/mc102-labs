from lab06 import soma_vetores


def test_soma_vetores_mesmo_tamanho() -> None:
    assert soma_vetores([1, 2], [2, 3]) == [3, 5]
    assert soma_vetores([11, -4, -2], [-2, -3, 10]) == [9, -7, 8]
    assert soma_vetores([23, 11, 123, 0, 2], [-123, -23, 2, -55, 0]) == [
        -100,
        -12,
        125,
        -55,
        2,
    ]
    assert soma_vetores([], []) == []


def test_soma_vetores_tamanhos_diferentes() -> None:
    assert soma_vetores([1], [2, 3]) == [3, 3]
    assert soma_vetores([2, 3], [1]) == [3, 3]
    assert soma_vetores([], [1, 2, 3]) == [1, 2, 3]
    assert soma_vetores([1, 2, 3], []) == [1, 2, 3]
