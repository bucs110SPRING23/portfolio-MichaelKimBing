import requests

class Exchangerate:

    def __init__(self):
        """
        Initializes the api url of the API Exchange Rate or Exchangerate.host
        arguments: None
        return: API text
        """
        self.api_url = f"https://api.exchangerate.host/latest?base=USD"

    def get(self, amount):
        """
        Calls for the information of the current exchange rate from several different types of currencies, such as Euros, Canadian Dollar, Korean Won, Cuban Pesos, and Chinese Yuan
        arguments: self, amount
        return: 'rates' of 'EUR', 'CAD', 'KRW', 'CUP', and 'CNY'
        """
        self.amount = amount
        r = requests.get(f'{self.api_url}&{amount}')
        response = r.json()
        exchange_dict = response
        return exchange_dict['rates']['EUR'],exchange_dict['rates']['CAD'],exchange_dict['rates']['KRW'], exchange_dict['rates']['CUP'],exchange_dict['rates']['CNY']

    def __str__(self):
        """
        Returns the object in a string representation
        arguments: self
        return: string value
        """
        eur_currency,canada_currency,korean_currency,cuban_currency,china_currency = self.get(self.amount)
        return f'"Your Net Worth in"\n Europe: €{eur_currency} \n Canada: ${canada_currency}\n Korea: ₩{korean_currency}\n Cuba: ₱{cuban_currency}\n China: ¥{china_currency}\n Thank You For Using Bitcoin Services.  Goodbye!'
