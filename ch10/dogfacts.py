import requests

class DogfactsAPI:

    def __init__(self):
        self.api_url = "http://dog-api.kinduff.com/api/facts"

    def get(self):
        url = self.api_url + self.amount
        response = requests.get(url)
        data = response.json()
        self.data = data

    def __str__(self):
        return self.data