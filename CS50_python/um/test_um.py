from um import count
import pytest

def test_strings():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("UM, Um uM.. ") == 3
    assert count("cat") == 0
    assert count("Um, thanks for the album.") == 1

def test_other():
    assert count("1337 H4X0R") == 0
    assert count("") == 0