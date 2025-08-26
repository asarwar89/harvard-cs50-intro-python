import csv
students = []

# with open("students.csv") as file:
#   for line in file:
#     name, house = line.rstrip().split(",")
#     students.append({"name": name, "house": house})
#     # students.append([name, house])

# # for student in sorted(students, key=lambda s: s['house'], reverse=True):
# #     print(f"{student['name']} is in {student['house']}")

# def get_house(student):
#     return student['house']

# for student in sorted(students, key=get_house, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# with open("students.csv") as file:
#   # reader = csv.reader(file)
#   # for row in reader:
#   #   students.append({"name": row[0], "home": row[2]})
  
#   reader = csv.DictReader(file)
#   for row in reader:
#     students.append({"name": row["name"], "address": row["address"]})

# for student in sorted(students, key=lambda s: s['name']):
#     print(f"{student['name']} is from {student['address']}")

name = input("Name: ")
home = input("House: ")

with open("students.csv", "a") as file:
  # writer = csv.writer(file)
  writer = csv.DictWriter(file, fieldnames=["name", "address"])
  writer.writerow({"name": name, "address": home})