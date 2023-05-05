import requests

class CatfactsAPI:

    def __init__(self):
        self.api_url = "https://meowfacts.herokuapp.com/?"
        self.amount = "count=1"

    def get(self):
        url = self.api_url + self.amount
        response = requests.get(url)
        data = response.json()
        self.data = data

    def __str__(self):
        return self.data