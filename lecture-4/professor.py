import random


def main():
  level = get_level()
  count = 10
  correct_count = 0

  while count > 0:
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    answer = num1 + num2

    try_count = 3
    while try_count > 0:
      try:
          response = int(input(f"{num1} + {num2} = "))
          if response == answer:
            print("Correct!")
            count -= 1
            correct_count += 1
            break
          else:
            print("EEE")
            try_count -= 1
            if try_count == 0:
                count -= 1
      except ValueError:
        print("EEE")
        try_count -= 1
        if try_count == 0:
                count -= 1

  print(f"Score: {correct_count}")


def get_level():
  while True:
    try:
       level = int(input("Enter difficulty level (0-3): "))
       if 0 <= level <= 3:
           return level
       else:
           continue
    except ValueError:
       pass


def generate_integer(level):
    num = ''
    if level > 2:
      num = str(random.randint(0, 9))
    
    if level > 1:
      num = str(random.randint(0, 9)) + num
    
    if level > 0:
      num = str(random.randint(1, 9)) + num

    return int(num)


if __name__ == "__main__":
    main()