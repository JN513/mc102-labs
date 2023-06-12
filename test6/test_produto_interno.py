from lab06 import produto_interno


def test_produto_interno_mesmo_tamanho() -> None:
    assert produto_interno([1, 2], [2, 3]) == 8
    assert produto_interno([11, -4, -2], [-2, -3, 10]) == -30
    assert produto_interno([23, 11, 123, 0, 2],
                           [-123, -23, 2, -55, 0]) == -2836
    assert produto_interno([], []) == 0


def test_produto_interno_tamanhos_diferentes() -> None:
    assert produto_interno([1], [2, 3]) == 5
    assert produto_interno([2, 3], [1]) == 5
    assert produto_interno([], [1, 2, 3]) == 6
    assert produto_interno([1, 2, 3], []) == 6
