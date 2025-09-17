import requests
import re

class StockPrice:
    def __init__(self, stock, duration=24):
        self.stock = stock
        self.price_data = self.get_html_data(stock, duration)

    def get_html_data(self, stock, duration=24):
        url = f"https://www.dsebd.org/php_graph/monthly_graph.php?inst={stock}&duration={duration}&type=price"
        response = requests.get(url)

        matches = re.findall(r'\"((\d{4}-\d{2}-\d{2}),(\d*.\d*))\\n', response.text)

        price_data = []
        for match in matches:
            date, price = match[1], float(match[2])
            price_data.append({"date": date, "price": price})
        
        return price_data
    
    def get_price_data(self):
        return self.price_data

    def __repr__(self):
        return f"StockPrice(stock={self.stock}, price_data={self.price_data})"