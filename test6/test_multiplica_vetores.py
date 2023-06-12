from lab06 import multiplica_vetores


def test_multiplica_vetores_mesmo_tamanho() -> None:
    assert multiplica_vetores([1, 2], [2, 3]) == [2, 6]
    assert multiplica_vetores([11, -4, -2], [-2, -3, 10]) == [-22, 12, -20]
    assert multiplica_vetores([23, 11, 123, 0, 2], [-123, -23, 2, -55, 0]) == [
        -2829,
        -253,
        246,
        0,
        0,
    ]
    assert multiplica_vetores([], []) == []


def test_multiplica_vetores_tamanhos_diferentes() -> None:
    assert multiplica_vetores([1], [2, 3]) == [2, 3]
    assert multiplica_vetores([2, 3], [1]) == [2, 3]
    assert multiplica_vetores([], [1, 2, 3]) == [1, 2, 3]
    assert multiplica_vetores([1, 2, 3], []) == [1, 2, 3]
