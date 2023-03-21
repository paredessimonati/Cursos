from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == round((3 / 4) * 100)
    assert convert("1/1") == round((1 / 1) * 100)
    assert convert("2/5") == round((2 / 5) * 100)
    assert convert("6/15") == round((6 / 15) * 100)


def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert("cat")
        convert("dog/50")
        convert("-1")
        convert("cat/dog")
        convert("0.5/1")


def test_convert_divideby0():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")
        convert("3/0")
        convert("-1/0")


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(30) == "30%"


def test_ve():
    with pytest.raises(ValueError):
        convert("fd")
        convert("s/50")
        convert("x/t")
    with pytest.raises(ValueError):
        convert("-5/10")
        convert("5/-3")
    with pytest.raises(ValueError):
        convert("1.5/3")
        convert("5/3")
