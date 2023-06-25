import pytest
import os
from lessons_8.card_repository import CardRepository
from lessons_8.card_models import Card


@pytest.fixture
def db_params():
    return {
        "host": "localhost",
        "port": 5432,
        "dbname": "cards_db",
        "user": "maksym",
        "password": os.environ.get("DB_PASSWORD", "123456")
    }


@pytest.fixture
def card_repo(db_params):
    return CardRepository(db_params)


def test_card_activate():
    card = Card(
        card_id=1,
        number_card="7006670334173992",
        expiry_date="03/25",
        cvv="485",
        issue_date="2023-06-24",
        owner_id="1234",
        status_card="new"
    )
    assert card.activate() == "activate"


def test_card_activate_blocked():
    card = Card(
        card_id=1,
        number_card="7006670334173992",
        expiry_date="03/25",
        cvv="485",
        issue_date="2023-06-24",
        owner_id="1234",
        status_card="blocked"
    )
    assert card.activate() == "Blocked card, can not be activated"


def test_card_block():
    card = Card(
        card_id=1,
        number_card="7006670334173992",
        expiry_date="03/25",
        cvv="485",
        issue_date="2023-06-24",
        owner_id="1234",
        status_card="activate"
    )
    assert card.block() == "blocked"


def test_card_repository_get_nonexistent_card(card_repo):
    card = card_repo.get_card_by_id(999)
    assert card is None


def test_card_repository_show(card_repo, capsys):
    card1 = Card(
        card_id=1,
        number_card="7006670334173992",
        expiry_date="03/25",
        cvv="485",
        issue_date="2023-06-24",
        owner_id="1234",
        status_card="new"
    )
    card_repo.save(card1)

    cards = card_repo.show()
    card_numbers = [card.number_card for card in cards]

    assert "7006670334173992" in card_numbers
