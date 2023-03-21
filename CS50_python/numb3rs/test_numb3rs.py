from numb3rs import validate
import pytest

def test_validate():
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True
    assert validate("111.111.111.111") is True

def test_validate_letters():
    assert validate("a.a.a.a") is ValueError
    assert validate("a.24.a.24") is ValueError
    assert validate("24.a.24.a") is ValueError
    assert validate("a..24") is ValueError
    assert validate("24a...") is ValueError
    assert validate("cat") is ValueError

def test_validate_other():
    assert validate("-1.244.255.255") is False
    assert validate("-100") is False
    assert validate("256.256.256.256") is False
    assert validate("256.255.255.255") is False
    assert validate("255.256.255.255") is False
    assert validate("255.255.256.255") is False
    assert validate("255.255.255.256") is False