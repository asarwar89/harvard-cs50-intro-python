def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s):
  num_started = False
  index = 0

  if (len(s) < 2 or len(s) > 6):
    return False

  while (index < len(s)):
    if not s[index].isalnum():
      return False
    elif index < 2:
      if s[index] in "0123456789":
        return False
    elif s[index].isalpha() and num_started == True:
      return False
    elif s[index] in "0123456789" and num_started == False:
      if s[index] == "0":
        return False
      num_started = True

    index += 1
  
  return True


    
  


main()