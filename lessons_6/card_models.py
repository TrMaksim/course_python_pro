import uuid


class Card:

    def __init__(self, card_id: int, number_card: str, expiry_date: str, cvv: str,
                 issue_date: str, owner_id: uuid.UUID, status_card: str):
        self.card_id = card_id
        self.number_card = number_card
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.issue_date = issue_date
        self.owner_id = owner_id
        self.status_card = status_card

    def activate(self) -> str:
        if self.status_card == "new":
            self.status_card = "activate"
            return "activate"
        elif self.status_card == "blocked":
            return "Blocked card, can not be activated"

    def block(self) -> str:
        if self.status_card == "activate":
            self.status_card = "blocked"
            return "blocked"
