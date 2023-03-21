import twttr

def test_twttr():
    assert twttr.shorten("Hola")== "Hl"
    assert twttr.shorten("HOLA")== "HL"
    assert twttr.shorten("H0l4")== "H0l4"
    assert twttr.shorten("Hola..")== "Hl.."