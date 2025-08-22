# import json
import requests
import sys

if (len(sys.argv) != 2):
  sys.exit("Missing command-line argument")

try:
  number = float(sys.argv[1])
except (ValueError, IndexError):
  sys.exit("Command-line argument is not a number")


try:
  response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0a09391b6b996ce41e2196e4c1f11dc3b6674d842ed06cca5b4b21df25af229c")
  
  o = response.json()
  price_USD = float(o["data"]["priceUsd"])
  total_price = price_USD * number
  print(f"${total_price:,.4f}")

except requests.RequestException: 
  print("Error")