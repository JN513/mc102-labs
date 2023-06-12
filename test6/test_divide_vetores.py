from lab06 import divide_vetores


def test_divide_vetores_mesmo_tamanho() -> None:
    assert divide_vetores([1, 2], [2, 3]) == [0, 0]
    assert divide_vetores([11, -4, -2], [-2, -3, 10]) == [-6, 1, -1]
    assert divide_vetores([23, 11, 123, 0, 2], [-123, -23, 2, -55, 1]) == [
        -1,
        -1,
        61,
        0,
        2,
    ]
    assert divide_vetores([], []) == []


def test_divide_vetores_tamanhos_diferentes() -> None:
    assert divide_vetores([10], [2, 3]) == [5, 0]
    assert divide_vetores([2, 3], [1]) == [2, 3]
    assert divide_vetores([], [10, 2, 3]) == [0, 0, 0]
    assert divide_vetores([10, 2, 3], []) == [10, 2, 3]
