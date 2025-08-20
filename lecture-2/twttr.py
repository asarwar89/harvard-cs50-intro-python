word = input("Input: ")

for char in word:
    if char in "aeiouAEIOU":
        continue
    print(char, end="")
print()