import uuid


class Card:

    def __init__(self, number_card: str, expiry_date: str, cvv: str,
                 issue_date: str, owner_id: uuid.UUID, status_card: str):
        self.number_card = number_card
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.issue_date = issue_date
        self.owner_id = owner_id
        self.status_card = status_card

    def activate(self) -> str:
        if self.status_card == "новая":
            self.status_card = "активная"
            return "активная"
        elif self.status_card == "заблокирована":
            return "Заблокированная карта, не может активироваться"

    def block(self) -> str:
        if self.status_card == "активная":
            self.status_card = "заблокирована"
            return "заблокирована"

    def secure_data(self) -> str:
        secure_number_card = "X" * 12 + self.number_card[-4:]
        secure_cvv = "X" * len(self.cvv)
        return f"Secure Number: {secure_number_card}, CVV: {secure_cvv}"
