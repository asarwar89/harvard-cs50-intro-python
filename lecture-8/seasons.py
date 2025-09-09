from datetime import date
import re
import sys
import inflect

def main():
    dob = input("Date of Birth: ")
    
    # initiate regex
    if (re.match(r"^[1-2][0-9]{3}-((0[0-9])|(1[0-2]))-(([0-2][0-9])|(3[0-1]))$", dob)):
        dob = date.fromisoformat(dob)
        today = date.today()
        today = date.fromisoformat('2000-01-01')  # For testing purposes
        duration = duration_minutes_words(dob, today)
        print(f"{duration} minutes")
    else:
        sys.exit("Invalid date")

def duration_minutes_words(dob, today):
    duration = today - dob
    minutes = duration.total_seconds() / 60
    return inflect.engine().number_to_words(int(minutes))


if __name__ == "__main__":
    main()