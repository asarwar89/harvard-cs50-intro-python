def main():
  while True:
    date = get_date(input("Date: "))
    if date:
      print(date)
      break

def get_date(date_str):
  date_str = date_str.strip()
  months = {
    "January": '01',
    "February": '02',
    "March": '03',
    "April": '04',
    "May": '05',
    "June": '06',
    "July": '07',
    "August": '08',
    "September": '09',
    "October": '10',
    "November": '11',
    "December": '12'
  }
  
  try:
    if ('/' in date_str):
      month, day, year = date_str.split("/")
      month = month.zfill(2)
      day = day.zfill(2)
      return f"{year}-{month}-{day}"
    elif (',' in date_str):
      date_str = date_str.replace(',', '')
      month, day, year = date_str.split(" ")
      month = months[month]
      return f"{year}-{month}-{day.zfill(2)}"
    else:
      return None
  except KeyError:
    return None

main()