class Wizard:
  def __init__(self, name):
    if not name:
      raise ValueError("Name cannot be empty")
    self.name = name

class Student(Wizard):
  def __init__(self, name, house):
    super().__init__(name)
    self.house = house

class Professor(Wizard):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

wizard = Wizard("Karim")
student = Student("Alice", "Gryffindor")
professor = Professor("Snape", "Potions")

print(wizard.name)
print(student.name, student.house)
print(professor.name, professor.subject)
