import re


def match_passport_number(text):
    pattern = r'\b[А-Я]{2}\d{6}\b'
    matches = re.findall(pattern, text)
    return matches


def match_ipn(text):
    pattern = r'\b\d{10}\b'
    matches = re.findall(pattern, text)
    return matches


def match_car_numbers(text):
    pattern = r'\b[АЕХ]{2}\d{4}(?<!0{4})[АВЕКМНОРСТУХ]{2}\b'
    matches = re.findall(pattern, text)
    return matches


input_text = """
    Паспорти: АВ123456, БК654321, УК987654.
    ІПН: 1234567890, 9876543210, 5555555555.
    Номери: АВ1234А, ЕК5678М, АХ1234ЕР.
"""

passport_numbers = match_passport_number(input_text)
print("Паспортні номери:", passport_numbers)

ipn_numbers = match_ipn(input_text)
print("ІПН:", ipn_numbers)

car_numbers = match_car_numbers(input_text)
print("Номери авто:", car_numbers)
