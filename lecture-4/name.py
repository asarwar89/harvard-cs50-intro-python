import sys

if len(sys.argv) > 2:
  sys.exit("Too many arguments")
elif len(sys.argv) < 2:
  sys.exit("Too few arguments")
    
print("Hello, " + sys.argv[1])