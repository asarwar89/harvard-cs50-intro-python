import sys

if (len(sys.argv) < 2):
    print("Too few command-line arguments")
    sys.exit()

if (len(sys.argv) > 2):
    print("Too many command-line arguments")
    sys.exit()

if (sys.argv[1].endswith('.py') == False):
    print("Not a Python file")
    sys.exit()

count = 0
with open(sys.argv[1]) as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if (line.startswith("# ") == False and line != "" and line != "#"):
          print(line)
          count += 1
    print(count)