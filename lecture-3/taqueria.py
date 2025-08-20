def main():
  items = {
    "baja_taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super_burrito": 8.50,
    "super_quesadilla": 9.50,
    "taco": 3.00,
    "tortilla_salad": 8.00
  }

  total = 0

  while True:
    try:
      item = input("Item: ").lower().replace(" ", "_")

      price = items.get(item)
      if (price is not None):
        total += price
        print(f"Total: ${total:.2f}")
    except EOFError:
      print("\n")
      break

main()