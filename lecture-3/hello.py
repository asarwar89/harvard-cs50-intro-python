def main():
  x = get_int("Enter a number: ")
  print(f"x is {x}")

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      # print("That's not a valid number!")
      pass
  
main()

