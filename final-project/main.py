from company_symbols import StockSymbols
from stock_price import StockPrice


symbols = StockSymbols().get_symbols()
number_of_stocks = int(input("Number of stocks to fetch (default 5): ") or 5)
count = 0
for symbol in symbols:
    if count == number_of_stocks:
        break
    stock = StockPrice(symbol)
    price = stock.get_price_data()
    print(f"=========================Start - {symbol}============================")
    for entry in price:
      print(f"Date: {entry['date']}, Price: {entry['price']}")
    count += 1
    print(f"=========================End - {symbol}============================")