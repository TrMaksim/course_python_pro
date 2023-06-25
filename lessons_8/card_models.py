class Card:
    def __init__(self, card_id=None, number_card=None, expiry_date=None,
                 cvv=None, issue_date=None, owner_id=None, status_card=None):
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
