
x = input("What's x? ")
y = input("What's y? ")

number = round(float(x) + float(y))

print(f"{number:,}")

z = float(x) / float(y)
print(f"{z:.2f}")

def main():
  x = int(input("What's x? "))
  print("x squired is", square(x))

def square(n):
  return n * n

main();