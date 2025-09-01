from numb3rs import validate

def test_valid_ips():
  assert validate("192.168.1.1") == True
  assert validate("255.255.255.255") == True
  assert validate("0.0.0.0") == True

def test_invalid_ips():
    assert validate("256.256.256.256") == False
    assert validate("192.168.1.256") == False
    assert validate("192.168.1.1.1") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("125.125.125.abc") == False
    assert validate("125.125.125.001") == False