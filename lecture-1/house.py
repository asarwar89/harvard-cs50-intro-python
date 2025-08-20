def main():
  name = input("Enter your name: ")

  match name:
    case "Harry" | "Hermione" | "Ron":
      print("Griffindor!")
    case "Draco":
      print("Slytherin!")
    case _:
      print("Unknown")

  # if (name == "Harry" or name == "Hermione" or name == "Ron"):
  #   print("Griffindor!")
  # elif (name == "Draco"):
  #   print("Slytherin!")
  # else:
  #   print("Unknown")

main()