i = 3

while i != 0:
  print('meow')
  i -= 1

i = 0

for i in [0,1,2]:
  print('meow for')

for _ in range(5):
  print('meow for range')

global n
n = 0

while n <= 0:
  n = int(input("How many times should I meow? "))

print('meow times\n' * n, end='')

def main():
  n = get_number()
  meow(n)

def get_number():
  while True:
    number = int(input("How many times should I meow? "))
    if number > 0:
      return number

def meow(n):
  for _ in range(n):
    print('meow')

main()