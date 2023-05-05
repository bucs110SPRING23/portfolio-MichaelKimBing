import requests

class DogfactsAPI:

    def __init__(self):
        self.url = "http://dog-api.kinduff.com/api/facts"
    
    def __str__(self):
        url = self.url
        response = requests.get(url)
        data = response.json()
        return data
