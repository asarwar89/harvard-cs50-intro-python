from bank import value

def test_value():
  assert value("hello") == '$0'
  assert value("HELLO") == '$0'
  assert value("Hi") == '$20'
  assert value("hI") == '$20'
  assert value("hey") == '$20'
  assert value("random") == '$100'