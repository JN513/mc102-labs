from lab06 import soma_elementos


def test_soma_elementos() -> None:
    assert soma_elementos([2]) == 2
    assert soma_elementos([1, -2, 3, 10]) == 12
    assert soma_elementos([1, -1]) == 0
    assert soma_elementos([]) == 0
    assert soma_elementos([1, -1, 1, -1, 1, -1]) == 0
