import sqlite3
import uuid
from typing import Optional
from lessons_6.card_models import Card
from lessons_6.table_controll import execute_query, unwrapper


class CardInteraction:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            id TEXT,
            card_number TEXT,
            expiry_date TEXT,
            cvv TEXT,
            issue_date TEXT,
            owner_id TEXT,
            status TEXT
        )
        ''')

        conn.commit()
        conn.close()

    def save(self, card: Card):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO cards(id, card_number, expiry_date, cvv, issue_date, owner_id, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(uuid.uuid4()),
            card.number_card,
            card.expiry_date,
            card.cvv,
            card.issue_date,
            str(card.owner_id),
            card.status_card
        ))

        conn.commit()
        conn.close()

    def get(self, card_number: str) -> Optional[Card]:
        query_sql = f'''SELECT * FROM cards WHERE card_number = {card_number}'''
        result = execute_query(query_sql)

        if result:
            card = Card(
                number_card=result[0][1],
                expiry_date=result[0][2],
                cvv=result[0][3],
                issue_date=result[0][4],
                owner_id=uuid.UUID(result[0][5]) if result[0][5] else None,
                status_card=result[0][6]
            )

            return card
        return None

    def show(self) -> None:
        query_sql = '''
        SELECT * FROM cards
        '''

        all_cards = execute_query(query_sql)
        unwrapper(all_cards)


def main():
    card_interaction = CardInteraction('cards.db')
    card_1 = Card(number_card="6100297465002704", expiry_date="07/25", cvv="378",
                  issue_date="2023-11-09", owner_id=uuid.uuid4(), status_card="заблокирована")

    # card_interaction.save(card_1)
    card_interaction.show()
    print(card_1.activate())
    print(card_1.block())
    card = card_interaction.get("6100297465002704")
    print(card.secure_data())


if __name__ == '__main__':
    main()
