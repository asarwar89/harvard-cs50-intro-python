from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50") == "CS50"
    assert shorten("aeiou") == ""

def test_shorten_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("WORLD") == "WRLD"
    assert shorten("PYTHON") == "PYTHN"

def test_shorten_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("world") == "wrld"
    assert shorten("python") == "pythn"