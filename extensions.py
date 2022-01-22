import json
import requests
from dopoln import exchanger

class APIException(Exception):
    pass
class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) !=3:
            raise APIException("Неверное количество параметров")

        quote, base, amount = values
        if quote == base:
            raise APIException(f"одинаковые валюты {base}")

        try:
            quote_form = exchanger[quote]
        except ValueError:
            raise APIException(f"Не удалось обработать {quote}")

        try:
            base_form = exchanger[base]
        except KeyError:
            raise APIException(f"Не удалось обработать {base}")

        try:
            amount =float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}")

        r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=f536d25e10b86b0aaeaf46b961304cba&rates={quote_form}&symbols={base_form}')
        result = float(json.loads(r.content)['rates'][base_form])* amount

        return round(result, 3)







