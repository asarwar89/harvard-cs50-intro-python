import random

while True:
  try:
    number = random.randint(1, int(input("Level: ")))
    if number > 0:
      break
  except ValueError:
    pass

while True:
  try:
    guess = int(input("Guess: "))

    if guess <= 0:
      continue

    if guess < number:
      print("Too small!")
    elif guess > number:
      print("Too large!")
    else:
      print("Just right!")
      break
  except ValueError:
    pass
