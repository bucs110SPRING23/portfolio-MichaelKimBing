import requests

class Cryptoprice:

    def __init__(self):
        self.api_url = f"https://api.coinstats.app/public/v1/coins"

    def get(self):
        self.skip = 0
        self.limit = 1
        r = requests.get(f'{self.api_url}?{self.skip}&{self.limit}')
        response = r.json()
        bitcoin_dict = response
        return bitcoin_dict['coins'][0]['name'],bitcoin_dict['coins'][0]['price']

    def __str__(self):
        name,price = self.get()
        return f'Name ID: {name}\nCurrent Value Per Bitcoin(USD): {price}'

