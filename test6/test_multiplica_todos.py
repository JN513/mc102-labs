from lab06 import multiplica_todos


def test_multiplica_todos_mesmo_tamanho() -> None:
    assert multiplica_todos([1, 2], [2, 3]) == [5, 10]
    assert multiplica_todos([11, -4, -2], [-2, -3, 10]) == [55, -20, -10]
    assert multiplica_todos([23, 11, -12, 0, 2], [-123, -23, 2, -55, 0]) == [
        -4577,
        -2189,
        2388,
        0,
        -398,
    ]
    assert multiplica_todos([], []) == []


def test_multiplica_todos_tamanhos_diferentes() -> None:
    assert multiplica_todos([1], [2, 3]) == [5]
    assert multiplica_todos([2, 3], [1]) == [2, 3]
    assert multiplica_todos([], [1, 2, 3]) == []
    assert multiplica_todos([1, 2, 3], []) == [0, 0, 0]
