def main():
  time = input("What time is it? ")

  timeInHours = convert(time)
  
  if (timeInHours >= 7 and timeInHours <= 8):
      print("breakfast time")
  elif (timeInHours >= 12 and timeInHours <= 13):
      print("lunch time")
  elif (timeInHours >= 18 and timeInHours <= 19):
      print("dinner time")


def convert(time):
  if (time.endswith("a.m.")):
    time = time.split(" ")[0]
    hour, minute = time.split(":")
  elif (time.endswith("p.m.")):
    hour, minute = time.split(" ")[0].split(":")
    if (int(hour) != 12 ):
      hour = int(hour) + 12  
  else:
    hour, minute = time.split(":")

  minute = int(minute) / 60

  return int(hour) + minute


if __name__ == "__main__":
    main()