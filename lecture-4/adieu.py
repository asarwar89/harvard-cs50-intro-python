def main():
  names = []

  while True:
    try:
      name = input("Name: ")
      names.append(name)

    except EOFError:
      print(process_str(names))
      break

def process_str(names):
  if not names:
    return ""

  return "Adieu, adieu, to " + ", ".join(names[:-1]) + f", and {names[-1]}"


if __name__ == "__main__":
  main()