def main():
  percentage = get_percentage("Fraction: ")
  print(percentage)

def get_percentage(prompt):
  while True:
    try:
      fraction = input(prompt)
      num, denom = fraction.split("/")
      percentage = round(int(num) / int(denom) * 100) 

      if (percentage <= 1):
        return "E"
      elif (percentage >= 99):
        return "F"

      return f"{percentage}%"
    except (ValueError, ZeroDivisionError):
      pass

main()
