import requests

class CatfactsAPI:

    def __init__(self):
        self.url = "https://meowfacts.herokuapp.com/?"
        self.amount = "count=1"

    def __str__(self):
        url = self.url + self.amount
        response = requests.get(url)
        data = response.json()
        return data
