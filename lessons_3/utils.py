import requests
from datetime import datetime
from urllib import parse


def get_currency_iso_code(currency: str) -> int:
    '''
    Функція повертає ISO код валюти
    :param currency: назва валюти
    :return: код валюти
    '''
    currency_dict = {
        'UAH': 980,
        'USD': 840,
        'EUR': 978,
        'GBP': 826,
        'AZN': 944,
        'CAD': 124,
        'PLN': 985,
    }
    try:
        return currency_dict[currency]
    except:
        raise KeyError('Currency not found! Update currencies information')


def get_currency_exchange_rate(currency_a: str,
                               currency_b: str) -> str:
    currency_code_a = get_currency_iso_code(currency_a)
    currency_code_b = get_currency_iso_code(currency_b)

    response = requests.get('https://api.monobank.ua/bank/currency')
    json = response.json()

    if response.status_code == 200:
        for i in range(len(json)):
            if json[i].get('currencyCodeA') == currency_code_a and json[i].get('currencyCodeB') == currency_code_b:
                date = datetime.fromtimestamp(
                    int(json[i].get('date'))
                ).strftime('%Y-%m-%d %H:%M:%S')
                rate_buy = json[i].get('rateBuy')
                rate_sell = json[i].get('rateSell')
                return f'exchange rate {currency_a} to {currency_b} for {date}: \n rate buy - {rate_buy} \n rate sell - {rate_sell}'
            return f'Not found: exchange rate {currency_a} to {currency_b}'
    else:
        return f"Api error {response.status_code}: {json.get('errorDescription')}"
# print(get_currency_exchange_rate('USD', 'UAH'))


def validate_rate_date(rate_date: str) -> str | None:
    formats = ["%Y-%m-%d", "%d-%m-%Y", "%d.%m.%Y", "%m.%d.%Y", "%Y.%m.%d"]

    for date_format in formats:
        try:
            date = datetime.strptime(rate_date, date_format)
            formatted_date = date.strftime("%d.%m.%Y")
            return formatted_date
        except ValueError:
            continue


def validate_input_bank(bank: str) -> str | None:
    formats = {
        'NBU': {'nbu', 'NB', 'NationalBank', 'nationalbank', 'Nb', 'NBU'},
        'PB': {'pb', 'Pb', 'privatbank', 'PrivatBank', 'pB', 'PRIVATBANK', 'PB'},
    }

    for bank_name, bank_formats in formats.items():
        if bank in bank_formats:
            return bank_name


def get_pb_exchange_rate(convert_currency: str,
                         bank: str,
                         rate_date: str) -> str:
    validate_data = validate_rate_date(rate_date)
    if not validate_data:
        return "Enter a different date format"
    params = {
        'json': '',
        'date': validate_data,  # TODO додати функцію валідації формату дати
    }

    query = parse.urlencode(params)
    api_url = 'https://api.privatbank.ua/p24api/exchange_rates?'
    response = requests.get(api_url+query)
    json = response.json()

    if response.status_code == 200:
        rates = json['exchangeRate']
        for rate in rates:
            if rate['currency'] == convert_currency:
                valid_bank = validate_input_bank(bank)
                if not valid_bank:
                    return 'Rates for this bank is not supported'
                if valid_bank == 'NBU':
                    try:
                        sale_rate = rate['saleRateNB']
                        purchase_rate = rate['purchaseRateNB']
                        return f'Exchange rate UAH to {convert_currency} for {validate_data} at {valid_bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate NBU for {convert_currency}'
                elif valid_bank == 'PB':
                    try:
                        sale_rate = rate['saleRate']
                        purchase_rate = rate['purchaseRate']
                        return f'Exchange rate UAH to {convert_currency} for {validate_data} at {valid_bank}: sale={sale_rate}, purchase={purchase_rate}'
                    except:
                        return f'There is no exchange rate PrivatBank for {convert_currency}'
    else:
        return f'error {response.status_code}'


result_for_date = get_pb_exchange_rate('USD', 'privatbank', '01.11.2022')
result_for_PB = get_pb_exchange_rate('USD', 'privatbank', '01.11.2022')
result_for_NBU = get_pb_exchange_rate('USD', 'NBU', '01.11.2022')
print(result_for_date)
print(result_for_PB)
print(result_for_NBU)
