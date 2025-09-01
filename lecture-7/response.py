import validators

def main():
  is_valid_email = validators.email(input("What's your email address? "))
  if is_valid_email:
      print("Valid")
  else:
      print("Invalid")

if __name__ == "__main__":
    main()
