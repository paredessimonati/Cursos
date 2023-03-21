from plates import is_valid


def test_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("38") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("ZZ") == True
    assert is_valid("Z") == False