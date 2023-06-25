import os
from lessons_8.card_generate import GenerateCard
from lessons_8.card_repository import CardRepository
from flask import Flask, jsonify
from lessons_8.card_models import Card

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


if __name__ == '__main__':
    app.run()
