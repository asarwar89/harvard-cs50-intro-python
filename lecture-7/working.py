import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
  if matches := re.findall(r"(\d{1,2}(?:\:\d{2})? (?:AM|PM))", s):
     for match in matches:
        matches_time = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM)$", match)
        if matches_time:
            hour = int(matches_time.group(1))
            minute = int(matches_time.group(2) or 0)
            period = matches_time.group(3)

            if (hour > 12 or minute > 59):
                raise ValueError("Invalid time format")

            if period == "AM":
                if hour == 12:
                    hour = 0
            else:
                if hour != 12:
                    hour += 12
            time = (f"{hour:02}:{minute:02}")
            s = s.replace(match, time)
  return s
if __name__ == "__main__":
    main()