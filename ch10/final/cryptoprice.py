import requests

class Cryptoprice:

    def __init__(self,skip = 0,limit = 1):
        self.api_url = f"https://api.coinstats.app/public/v1/coins?skip={skip}&limit={limit}"

    def get(self):
        r = requests.get(self.api_url)
        response = r.json()
        bitcoin_dict = response
        return bitcoin_dict['coins'][0]['name'],bitcoin_dict['coins'][0]['price']

    def __str__(self):
        name,price = self.get()
        return f'Name ID: {name}\nCurrent Value Per Bitcoin(USD): {price}'

