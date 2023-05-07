import requests

class Exchangerate:

    def __init__(self):
        self.api_url = f"https://api.exchangerate.host/latest?base=USD"

    def get(self, amount):
        r = requests.get(f'{self.api_url}&{amount}')
        response = r.json()
        exchange_dict = response
        return exchange_dict['rates']['EUR'],exchange_dict['rates']['CAD'],exchange_dict['rates']['KRW'], exchange_dict['rates']['CUP'],exchange_dict['rates']['CNY']

    def __str__(self):
        eur_currency,canada_currency,korean_currency,cuban_currency,china_currency = self.get()
        return f'"Your Net Worth in"\n Europe: €{eur_currency} \n Canada: ${canada_currency}\n Korea: ₩{korean_currency}\n Cuba: ₱{cuban_currency}\n China: ¥{china_currency}\n Thank You For Using Bitcoin Services.  Goodbye!'
