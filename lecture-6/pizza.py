import sys
from tabulate import tabulate

if (len(sys.argv) != 2 or sys.argv[1].endswith('.csv') == False):
  sys.exit()

pizza_list = []
try:
  with open(sys.argv[1], "r") as file:
      lines = file.readlines()
      for line in lines:
          pizza_list.append(line.rstrip().split(","))
except FileNotFoundError:
   sys.exit("File does not exist")



print(tabulate(pizza_list, headers="firstrow", tablefmt="grid"))
