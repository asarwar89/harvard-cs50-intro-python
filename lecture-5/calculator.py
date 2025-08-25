def main():
  number = input("Number: ")
  print(f"Square: {square(int(number))}")

def square(n):
  return n * n

if __name__ == "__main__":
  main()