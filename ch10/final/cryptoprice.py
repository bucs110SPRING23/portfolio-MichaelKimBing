import requests

class Cryptoprice:

    def __init__(self):
        """
        Initializes the api url of the API Cryptocurrency also known as CoinStats
        arguments: None
        return: API text
        """
        self.api_url = f"https://api.coinstats.app/public/v1/coins"

    def get(self):
        """
        Calls for the information of the name and the current price of one individual Bitcoin
        arguments: self
        return: 'name' and 'price' of Bitcoin
        """
        self.skip = 0
        self.limit = 1
        r = requests.get(f'{self.api_url}?{self.skip}&{self.limit}')
        response = r.json()
        bitcoin_dict = response
        return bitcoin_dict['coins'][0]['name'],bitcoin_dict['coins'][0]['price']

    def __str__(self):
        """
        Returns the object in a string representation
        arguments: self
        return: string value
        """
        name,price = self.get()
        return f'Name ID: {name}\nCurrent Value Per Bitcoin(USD): {price}'

