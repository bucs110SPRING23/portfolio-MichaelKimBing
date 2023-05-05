import requests

class DogfactsAPI:

    def __init__(self):
        self.url = "http://dog-api.kinduff.com/api/facts"

    def get(self):
        url = self.url
        response = requests.get(url)
        data = response.json()
        return data