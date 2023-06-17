import pytest
import uuid
from lessons_6.card_models import Card
from lessons_6.table_controll import execute_query
from lessons_6.card_repository import CardRepository


@pytest.fixture
def db_path(tmpdir):
    return str(tmpdir.join('cards.db'))


@pytest.fixture
def card_interaction(db_path):
    interaction = CardRepository(db_path)
    interaction.create_table()
    return interaction


def test_card_activate():
    card = Card(
        card_id="1",
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="new"
    )
    assert card.activate() == "activate"


def test_card_activate_blocked():
    card = Card(
        card_id="1",
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="blocked"
    )
    assert card.activate() == "Blocked card, can not be activated"


def test_card_block():
    card = Card(
        card_id="1",
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="activate"
    )
    assert card.block() == "blocked"


def test_card_interaction_get_nonexistent_card(card_interaction):
    card = card_interaction.get("99999")
    assert card is None


def test_card_interaction_show(card_interaction, capsys):
    card = Card(
        card_id="1",
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="activate"
    )
    card_interaction.save(card)
    card_interaction.show()
    captured = capsys.readouterr()
    assert "XXXXXXXXXXXX2704" in captured.out


def test_card_interaction_create_table(db_path):
    interaction = CardRepository(db_path)
    interaction.create_table()
    assert execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name='cards'") is not None
