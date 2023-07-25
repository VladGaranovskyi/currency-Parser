from lesson_12.bank import Bank
from lesson_12.curency import currency

import requests


class PrivateBank(Bank):
    def __init__(self):
        self.__url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

    def __get_json(self):
        response = requests.get(self.__url)
        return response.json()

    def get_currency_rate(self):
        currency_rate = {
            'rate': []
        }

        json = self.__get_json()
        for line in json:
            if line['ccy'].strip().lower() in currency.keys():
                currency_rate['rate'].append(
                    {
                        'currency': currency.get(line['ccy'].strip().lower()),
                        'purchase_rate': str(round(float(line['buy']), 2)),
                        'sale_rate': str(round(float(line['sale']), 2))
                    }
                )

        return currency_rate


if __name__ == '__main__':
    from pprint import pprint
    bank = PrivateBank()
    pprint(bank.get_currency_rate())
