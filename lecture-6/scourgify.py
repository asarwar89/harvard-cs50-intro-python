import csv
import sys

if (len(sys.argv) != 3):
  sys.exit()



try:
  students = []

  with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
      last_name, first_name = row["name"].split(", ")
      students.append({"first": first_name, "last": last_name, "house": row["house"]})

except FileNotFoundError:
  sys.exit("File does not exist")

try:
  with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    
    for student in sorted(students, key=lambda s: s['first']):
      writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
except FileNotFoundError:
  sys.exit("File does not exist")