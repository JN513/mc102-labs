from lab06 import multiplicacao_escalar


def test_multiplicacao_escalar() -> None:
    assert multiplicacao_escalar([1, 2, 3], 4) == [4, 8, 12]
    assert multiplicacao_escalar([-1, 2, -3], 4) == [-4, 8, -12]
    assert multiplicacao_escalar([1, 2, 3], -2) == [-2, -4, -6]
    assert multiplicacao_escalar([-1, 2, -3], -2) == [2, -4, 6]
    assert multiplicacao_escalar([], 2) == []
    assert multiplicacao_escalar([1, -1], 0) == [0, 0]
