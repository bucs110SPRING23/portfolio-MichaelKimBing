import requests
import random

class TrviaProxyAPI:
    def __init__(self):
        self.url = "https://opentdb.com/api.php?"
        self.varstr = "amount=2&category=10"
    
    def get(self):
        url = self.url + self.varstr
        response = requests.get(url)
        data = 

def main():


main()