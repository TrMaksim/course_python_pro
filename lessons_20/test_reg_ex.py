from reg_ex import match_passport_number, match_ipn, match_car_numbers


def test_match_passport_number():
    text = "Паспорти: АВ123456, БК654321, УК987654."
    matches = match_passport_number(text)
    assert matches == ["АВ123456", "БК654321", "УК987654"]


def test_match_ipn():
    text = "ІПН: 1234567890, 9876543210, 5555555555."
    matches = match_ipn(text)
    assert matches == ["1234567890", "9876543210", "5555555555"]


def test_match_car_numbers():
    text = "Номери: АВ1234А, ЕК5678М, СТ9876У."
    matches = match_car_numbers(text)
    assert matches == ["АВ1234А", "ЕК5678М", "СТ9876У"]