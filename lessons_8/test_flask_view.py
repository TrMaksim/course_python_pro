import os


from flask import Flask, jsonify
import pytest
from lessons_8.card_generate import GenerateCard
from lessons_8.card_repository import CardRepository
from lessons_8.card_models import Card


@pytest.fixture
def app():
    app = Flask(__name__)

    db_params = {
        "host": "localhost",
        "port": 5432,
        "dbname": "cards_db",
        "user": "maksym",
        "password": os.environ.get("DB_PASSWORD", "123456")
    }

    card_repo = CardRepository(db_params)
    card_generator = GenerateCard()

    @app.route('/card/save/<user_id>', methods=['GET'])
    def save_card(user_id):
        card_number = card_generator.generate_number_card()
        expiry_date = card_generator.generate_expiry_date()
        cvv = card_generator.generate_cvv()
        issue_date = card_generator.generate_issue_date()
        status_card = card_generator.generate_status_card()

        card = Card(
            number_card=card_number,
            expiry_date=expiry_date,
            cvv=cvv,
            issue_date=issue_date,
            owner_id=user_id,
            status_card=status_card
        )

        card_id = card_repo.save(card)

        if card_id:
            return jsonify({"card_id": user_id}), 200
        else:
            return jsonify({"error": "Failed to save the card."}), 500

    @app.route('/card/<int:card_id>')
    def get_card(card_id):
        card = card_repo.get_card_by_id(card_id)
        if card:
            return jsonify(card)
        return jsonify({"error": "Card not found"})

    @app.route('/cards')
    def get_all_cards():
        cards = card_repo.show()

        response_data = []
        for card in cards:
            card_data = {
                "card_id": card.card_id,
                "number_card": card.number_card,
                "expiry_date": card.expiry_date,
                "cvv": card.cvv,
                "issue_date": card.issue_date,
                "owner_id": str(card.owner_id) if card.owner_id else None,
                "status_card": card.status_card
            }
            response_data.append(card_data)

        return jsonify(response_data)

    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_save_card(client):
    response = client.get('/card/save/1234')
    assert response.status_code == 200
    data = response.get_json()
    assert data["card_id"] == "1234"


def test_get_card(client):
    card_data = {
        "number_card": "9779640847830906",
        "expiry_date": "04/24",
        "cvv": "754",
        "issue_date": "2023-06-24",
        "owner_id": "1234",
        "status_card": "new"
    }
    response = client.get('/card/88')
    assert response.status_code == 200
    data = response.get_json()

    assert data["number_card"] == card_data["number_card"]
    assert data["expiry_date"] == card_data["expiry_date"]
    assert data["cvv"] == card_data["cvv"]
    assert data["issue_date"] == card_data["issue_date"]
    assert data["owner_id"] == card_data["owner_id"]
    assert data["status_card"] == card_data["status_card"]


def test_get_all_cards(client):
    response = client.get('/cards')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0

    card_data = data[0]
    assert card_data["card_id"] == 1
    assert card_data["number_card"] == "7006670334173992"
    assert card_data["expiry_date"] == "03/25"
    assert card_data["cvv"] == "485"
    assert card_data["issue_date"] == "2023-06-24"
    assert card_data["owner_id"] == "1234"
    assert card_data["status_card"] == "new"
