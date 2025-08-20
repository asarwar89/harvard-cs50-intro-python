variable_name = input()

for char in variable_name:
  if char.isupper():
    print("_" + char.lower(), end="")
  else:
    print(char, end="")
print()