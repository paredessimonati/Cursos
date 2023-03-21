from bank import value


def test_bank_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0


def test_bank_20():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("HIIII") == 20


def test_bank_100():
    assert value("sup") == 100
    assert value("WADDUP") == 100
    assert value("MIAU") == 100
    assert value("2092384") == 100
    assert value("") == 100
    assert value(".hello") == 100
