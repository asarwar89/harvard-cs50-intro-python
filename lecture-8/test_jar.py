from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    try:
        Jar(-1)
        assert False, "Expected ValueError for negative capacity"
    except ValueError:
        pass
    
def test_str():
  jar = Jar(20)

  assert str(jar) == "0 / 20"

  jar.deposit(5)
  jar.deposit(5)

  assert str(jar) == "10 / 20"

  jar.deposit(2)
  assert str(jar) == "12 / 20"

  jar.withdraw(7)
  assert str(jar) == "5 / 20"

  try:
      jar.deposit(20)
      assert False, "Expected ValueError for exceeding capacity"
  except ValueError:
      pass
    
  assert str(jar) == "5 / 20"


def test_deposit():
  jar = Jar(10)
  jar.deposit(3)
  assert jar.size == 3

  jar.deposit(7)
  assert jar.size == 10

  try:
      jar.deposit(1)
      assert False, "Expected ValueError for exceeding capacity"
  except ValueError:
      pass

  assert jar.size == 10

def test_withdraw():
  jar = Jar(10)
  jar.deposit(10)

  jar.withdraw(4)
  assert jar.size == 6

  jar.withdraw(6)
  assert jar.size == 0

  try:
      jar.withdraw(1)
      assert False, "Expected ValueError for withdrawing from empty jar"
  except ValueError:
      pass

  assert jar.size == 0