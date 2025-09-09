class Student:
  def __init__(self, name, house, patronus):
    self.name = name
    self.house = house
    self.patronus = patronus

  def __str__(self):
    return f"{self.name} is from {self.house}."
  
  @property
  def house(self):
    return self._house
  
  @house.setter
  def house(self, house):
    if not house in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self._house = house

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name")
    self._name = name

  def charm(self):
    match self.patronus:
      case "Stag":
        return "Expecto Patronum!"
      case "Otter":
        return "You're a great friend!"
      case "Jack Russel Terrier":
        return "You're so loyal!"
      case _:
        return "I don't know that one."

def main():
  student = get_student()
  print(student.charm())

def get_student():
  name = input("Name: ")
  house = input("House: ")
  patronus = input("Patronus: ")
  return Student(name, house, patronus)

if __name__ == "__main__":
  main()