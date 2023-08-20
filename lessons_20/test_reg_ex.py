from reg_ex import *
import pytest


@pytest.fixture
def input_text():
    return """
        Паспорти: АВ123456, БК654321, УК987654.
        ІПН: 1234567890, 9876543210, 5555555555.
        Номери: АВ1234А, ЕК5678М, АХ1234ЕР.
    """


def test_match_passport_number(input_text):
    matches = match_passport_number(input_text)
    assert matches == ["АВ123456", "БК654321", "УК987654"]


def test_match_ipn(input_text):
    matches = match_ipn(input_text)
    assert matches == ["1234567890", "9876543210", "5555555555"]


def test_match_car_numbers(input_text):
    matches = match_car_numbers(input_text)
    assert matches == ["АХ1234ЕР"]
