from calculator import square

def main():
    test_square()

# def test_square():
#   if (square(2) != 4):
#     print("2 square is not 4")
#   if (square(3) != 9):
#     print("3 square is not 9")
#   if (square(4) != 16):
#     print("4 square is not 16")

def test_square():
  try:
    assert square(2) == 4
  except AssertionError:
     print("2 square is not 4")

  try:
    assert square(3) == 9
  except AssertionError:
     print("3 square is not 9")

  try:
    assert square(4) == 16
  except AssertionError:
     print("4 square is not 16")

  try:
    assert square(-3) == 9
  except AssertionError:
     print("-3 square is not 9")

  try:
    assert square(-4) == 16
  except AssertionError:
     print("-4 square is not 16")

  try:
    assert square(0) == 0
  except AssertionError:
     print("0 square is not 0")

if __name__ == "__main__":
  main()