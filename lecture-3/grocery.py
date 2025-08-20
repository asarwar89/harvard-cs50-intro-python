def main():
  items = dict(sorted(get_items().items()))

  for item in items:
    print(f"{items[item]} {item}")

def get_items():
  items = {}
  while True:
    try:
      item = input().strip().upper()
      items[item] = items.get(item, 0) + 1

    except EOFError:
      print()
      break
  return items

main()