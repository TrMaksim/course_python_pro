from uuid import uuid4

from sqlalchemy import Column, UUID, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


engine = create_engine(f"postgresql+psycopg2://maksym:123456@localhost/max_database", echo=True)

Base = declarative_base()


class Book(Base):
    __tablename__ = "Books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(200), nullable=False)
    author = Column(String(150), nullable=False)
    date_of_release = Column(Date, nullable=False)
    description = Column(String(250), nullable=False)
    genre = Column(String(100), nullable=False)


Base.metadata.create_all(engine)
