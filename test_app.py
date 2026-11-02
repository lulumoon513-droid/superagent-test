from app import divide, average


def test_divide():
    assert divide(10, 2) == 5


def test_average():
    assert average([1, 2, 3]) == 2
