import unittest
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Book
from testing.postgresql import Postgresql


class TestBooksModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.postgresql = Postgresql()
        database_url = f"postgresql+psycopg2://maksym:123456@localhost/max_database"
        cls.engine = create_engine(database_url)
        Book.metadata.create_all(cls.engine)

    @classmethod
    def tearDownClass(cls):
        cls.engine.dispose()
        cls.postgresql.stop()

    def setUp(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_create_and_read_books(self):
        book = Book(
            name="Sample Book",
            author="John Doe",
            date_of_release="2023-08-25",
            description="A sample book",
            genre="Fiction"
        )

        self.session.add(book)
        self.session.commit()

        retrieved_book = self.session.query(Book).filter_by(name="Sample Book").first()

        self.assertEqual(retrieved_book.name, "Sample Book")
        self.assertEqual(retrieved_book.author, "John Doe")
        self.assertEqual(retrieved_book.date_of_release, datetime.strptime("2023-08-25", "%Y-%m-%d").date())
        self.assertEqual(retrieved_book.description, "A sample book")
        self.assertEqual(retrieved_book.genre, "Fiction")


if __name__ == '__main__':
    unittest.main()
