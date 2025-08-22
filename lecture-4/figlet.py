import sys
from pyfiglet import Figlet

if len(sys.argv) == 1:
  print(input("Input: "))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-font"):
  try:
    f = Figlet(font=sys.argv[2])
    print(f.renderText(input("Input: ")))
    sys.exit()
  except Exception:
    sys.exit("Invalid usage")
else:
  sys.exit("Invalid usage")
