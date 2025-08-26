# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

with open("names.txt", "r") as file:
    # lines = file.readlines()
    # for line in lines:
    #     names.append(line.rstrip())
    # for name in names:
    #     print(f"Hello, {name}")

    # for line in file:
    #     print("Hello,", line.rstrip())
    
    names = []

    with open("names.txt") as file:
        for line in file:
            names.append(line.rstrip())

    for name in sorted(names):
        print(f"Hello, {name}")
