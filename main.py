
from lesson_12.aval_parser import RaiffeisenBankAval
from lesson_12.private_bank import PrivateBank

banks = [
    RaiffeisenBankAval(),
    PrivateBank()
]


for bank in banks:
    rates = bank.get_currency_rate()

    for rate in rates['rate']:
        print('currency name: {cn}\tpurchase: {p}\tsale: {s}'.format(
            cn=rate['currency'],
            p=rate['purchase_rate'],
            s=rate['sale_rate']
        ))

    print('-' * 50)
    print()