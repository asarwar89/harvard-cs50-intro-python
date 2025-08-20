students = ["Harry", "Hermione", "Ron"]

for student in students:
  print(student)

for i in range(len(students)):
  print(students[i])

students = {
  "Harry": "Griffindor",
  "Hermione": "Griffindor",
  "Ron": "Griffindor",
  "Draco": "Slytherin"
}

for student in students:
  print(student, students[student], sep=": ")

print('\n')

students = [
  {"name": "Harry", "house": "Griffindor", "patronous": "Stag"},
  {"name": "Hermione", "house": "Griffindor", "patronous": "Otter"},
  {"name": "Ron", "house": "Griffindor", "patronous": "Jack Russell Terrier"},
  {"name": "Draco", "house": "Slytherin", "patronous": None}
]

for student in students:
  for key in student:
    print(key, student[key], sep=": ")