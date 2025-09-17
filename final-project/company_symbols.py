import requests
import re

class StockSymbols:
    def __init__(self):
        self.symbols = self.fetch_symbols()
        

    def fetch_symbols(self):
        url = "https://www.dsebd.org/latest_share_price_scroll_by_value.php"
        response = requests.get(url)
        matches = re.findall(r'displayCompany.php\?name=([A-Z]*)\"', response.text)

        return matches
    
    def get_symbols(self):
        return self.symbols

    def __str__(self):
        return f"StockSymbols(symbols={self.symbols})"
