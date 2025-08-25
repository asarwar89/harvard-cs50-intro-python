from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS50P") == True
    assert is_valid("CS50P123") == False
    assert is_valid("C") == False
    assert is_valid("CS50P!") == False
    assert is_valid("CS50P0") == False

def test_is_not_valid():
    assert is_valid("CS50P!") == False
    assert is_valid("C") == False
    assert is_valid("CS50P123") == False
    assert is_valid("C0P123") == False