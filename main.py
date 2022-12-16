import requests


def kurs(amount, currency, date):
    response = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/c/{currency}/{date}/?format=json')
    if response.status_code == 200:
        ask = response.json()['rates'][0]['ask']
        return amount * ask
    else:
        return response.text


if __name__ == '__main__':
    print(kurs(1, 'usd', '2022-10-05'))
