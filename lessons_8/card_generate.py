import random
from datetime import date, datetime, timedelta


class GenerateCard:
    def __init__(self):
        pass

    def generate_number_card(self) -> int:
        card_number = ''.join(str(random.randint(0, 9)) for _ in range(16))
        return int(card_number)

    def generate_expiry_date(self) -> str:
        current_date = datetime.now()
        expiry_date = current_date + timedelta(days=random.randint(30, 365 * 2))
        expiry_date_str = expiry_date.strftime("%m/%y")
        return expiry_date_str

    def generate_cvv(self) -> str:
        cvv = ''.join(str(random.randint(0, 9)) for _ in range(3))
        return cvv

    def generate_issue_date(self) -> str:
        issue_date = date.today().strftime("%Y-%m-%d")
        return issue_date

    def generate_status_card(self) -> str:
        # Generate a random status for the card
        statuses = ["new", "active"]
        status_card = random.choice(statuses)
        return status_card