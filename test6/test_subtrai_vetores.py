from lab06 import subtrai_vetores


def test_subtrai_vetores_mesmo_tamanho() -> None:
    assert subtrai_vetores([1, 2], [2, 3]) == [-1, -1]
    assert subtrai_vetores([11, -4, -2], [-2, -3, 10]) == [13, -1, -12]
    assert subtrai_vetores([23, 11, 123, 0, 2], [-123, -23, 2, -55, 0]) == [
        146,
        34,
        121,
        55,
        2,
    ]
    assert subtrai_vetores([], []) == []


def test_subtrai_vetores_tamanhos_diferentes() -> None:
    assert subtrai_vetores([1], [2, 3]) == [-1, -3]
    assert subtrai_vetores([2, 3], [1]) == [1, 3]
    assert subtrai_vetores([], [1, 2, 3]) == [-1, -2, -3]
    assert subtrai_vetores([1, 2, 3], []) == [1, 2, 3]
