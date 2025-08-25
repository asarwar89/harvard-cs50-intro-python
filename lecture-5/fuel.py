def main():
  while True:
    try:
      fraction = input("Fraction: ")
      fraction = convert(fraction)
      percentage = gauge(fraction)
      
      if percentage:
        print(percentage)
        break
    except (ValueError, ZeroDivisionError):
      pass

def convert(fraction):
  try:
    num, denom = fraction.split("/")

    if denom == "0":
      raise ZeroDivisionError
    
    percentage = round(int(num) / int(denom) * 100) 

    if (percentage <= 0 or percentage >= 100):
      raise ValueError

    return percentage
  except (ValueError, ZeroDivisionError):
    pass
  
def gauge(percentage):
  if (percentage <= 1):
    return "E"
  elif (percentage >= 99):
    return "F"
  return f"{percentage}%"

if __name__ == "__main__":
  main()
