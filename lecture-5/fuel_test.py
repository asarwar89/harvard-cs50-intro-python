from fuel import convert, gauge
import pytest

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75

    if pytest.raises(ValueError):
        convert("1/1")
        convert("0/1")
        

def test_convert_invalid():
    assert convert("1/0") == None
    assert convert("1/2/3") == None
    assert convert("three/four") == None

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
