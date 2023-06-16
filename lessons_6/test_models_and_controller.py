import pytest
import uuid
from lessons_6.card_models import Card
from lessons_6.table_controll import execute_query
from lessons_6.card_controller import CardInteraction


@pytest.fixture
def db_path(tmpdir):
    return str(tmpdir.join('cards.db'))


@pytest.fixture
def card_interaction(db_path):
    interaction = CardInteraction(db_path)
    interaction.create_table()
    return interaction


def test_card_activate():
    card = Card(
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="новая"
    )
    assert card.activate() == "активная"


def test_card_activate_blocked():
    card = Card(
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="заблокирована"
    )
    assert card.activate() == "Заблокированная карта, не может активироваться"


def test_card_block():
    card = Card(
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="активная"
    )
    assert card.block() == "заблокирована"


def test_card_secure_data():
    card = Card(
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="активная"
    )
    assert card.secure_data() == "Secure Number: XXXXXXXXXXXX2704, CVV: XXX"


def test_card_interaction_get_nonexistent_card(card_interaction):
    card = card_interaction.get("1234567812345678")
    assert card is None


def test_card_interaction_show(card_interaction, capsys):
    card = Card(
        number_card="6100297465002704",
        expiry_date="07/25",
        cvv="378",
        issue_date="2023-11-09",
        owner_id=uuid.uuid4(),
        status_card="активная"
    )
    card_interaction.save(card)
    card_interaction.show()
    captured = capsys.readouterr()
    assert "6100297465002704" in captured.out


def test_card_interaction_create_table(db_path):
    interaction = CardInteraction(db_path)
    interaction.create_table()
    assert execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name='cards'") is not None


