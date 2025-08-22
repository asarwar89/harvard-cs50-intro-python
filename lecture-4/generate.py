# import random
from random import choice, randint, shuffle

# choice = random.choice(["heads", "tails"])
choice = choice(["heads", "tails"])
num = randint(1, 100)
print(choice)
print(num)

cards = ["jack", "queen", "king"]
shuffle(cards)

for card in cards:
  print(card)