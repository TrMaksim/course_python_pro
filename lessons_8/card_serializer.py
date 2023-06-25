import json
from lessons_8.card_models import Card


class CardSerialiser:

    @classmethod
    def to_json(cls, card: Card) -> str:
        return {
            "number_card": card.number_card,
            "expiry_date": card.expiry_date,
            "cvv": card.cvv,
            "issue_date": card.issue_date,
            "owner_id": str(card.owner_id),
            "status_card": card.status_card
        }
