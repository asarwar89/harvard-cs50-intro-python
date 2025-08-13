def main():
  name = input("What's your name? ")

  # name = name.strip().capitalize()
  name = name.strip().title()

  first, last = name.split(" ")

  print("Hello,", first )
  print("Hello,", end=" ")
  print(first)
  print(f"Hello, {first}")

  hello(first)
  hello()

def hello(to="world"):
  print("Hello,", to)

main()