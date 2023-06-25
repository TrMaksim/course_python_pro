from typing import Optional
from lessons_8.card_serializer import CardSerialiser
from lessons_8.card_models import Card
from psycopg2.pool import SimpleConnectionPool


class CardRepository:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = self.connection_to_db()

    def connection_to_db(self):
        connection_pool = SimpleConnectionPool(1, 10, **self.db_params)
        connection = connection_pool.getconn()
        return connection

    def create_table(self):
        query_sql = '''
        CREATE TABLE public.cards(
        card_id SERIAL PRIMARY KEY NOT NULL,
        card_number varchar(100) NOT NULL,
        expiry_date varchar(100) NOT NULL,
        cvv varchar(100) NOT NULL,
        issue_date varchar(100) NOT NULL,
        owner_id varchar(100) NOT NULL,
        status varchar(100) NOT NULL);
        '''
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(query_sql)

    def save(self, card: Card):
        query_sql = '''
                   INSERT INTO public.cards (card_number, expiry_date, cvv, issue_date, owner_id, status)
                   VALUES (%s, %s, %s, %s, %s, %s)
                   RETURNING card_id;
               '''

        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(query_sql, (
                    card.number_card,
                    card.expiry_date,
                    card.cvv,
                    card.issue_date,
                    str(card.owner_id),
                    card.status_card
                ))
                card_id = cursor.fetchone()[0]
                return card_id

    def get_card_by_id(self, card_id: int) -> Optional[Card]:
        query_sql = "SELECT * FROM public.cards WHERE card_id = %s;"

        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(query_sql, (card_id,))
                result = cursor.fetchone()

        if result:
            card = Card(
                card_id=result[0],
                number_card=result[1],
                expiry_date=result[2],
                cvv=result[3],
                issue_date=result[4],
                owner_id=result[5],
                status_card=result[6]
            )
            return CardSerialiser.to_json(card)

    def show(self) -> list[Card]:
        query_sql = "SELECT * FROM cards;"
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(query_sql)
                result = cursor.fetchall()

        cards = []
        for row in result:
            card = Card(
                card_id=row[0],
                number_card=row[1],
                expiry_date=row[2],
                cvv=row[3],
                issue_date=row[4],
                owner_id=row[5],
                status_card=row[6]
            )
            cards.append(card)

        return cards
