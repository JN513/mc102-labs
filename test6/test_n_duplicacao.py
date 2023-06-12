from lab06 import n_duplicacao


def test_n_duplicacao() -> None:
    assert n_duplicacao([1], 4) == [1, 1, 1, 1]
    assert n_duplicacao([1, -2], 3) == [1, -2, 1, -2, 1, -2]
    assert n_duplicacao([1, 2], 0) == []
    assert n_duplicacao([], 2) == []
    assert n_duplicacao([1, -1], 3) == [1, -1, 1, -1, 1, -1]
