from lab06 import correlacao_cruzada


def test_correlacao_cruzada() -> None:
    assert correlacao_cruzada([], [1]) == []
    assert correlacao_cruzada([2], [1]) == [2]
    assert correlacao_cruzada([2], [-1]) == [-2]
    assert correlacao_cruzada([1, 2, 3], [-1, 1]) == [1, 1]
    assert correlacao_cruzada([3, 2, 1], [-1, 1]) == [-1, -1]
    assert correlacao_cruzada([3, 2, 1], [-1, -1]) == [-5, -3]
    assert correlacao_cruzada([3, 2, 3], [-1, 4, -1]) == [2]
    assert correlacao_cruzada([3, -2, 3, -10, 8], [-1, 2, -1]) == [-10, 18, -31]
    assert correlacao_cruzada([3, -2, 3, -10, 8], [-1, 2]) == [-7, 8, -23, 26]
