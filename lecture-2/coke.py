owe = 50

while (owe > 0):
  print("Amount dew", owe)
  coin = int(input("Insert coin: "))
  if coin > 0 and coin <= owe:
    owe -= int(coin)
  else:
    break

print("Change owed:", owe)