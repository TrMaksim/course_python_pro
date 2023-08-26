"""create_books_table

Revision ID: 001
Revises:
Create Date: 2023-08-25

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text

revision = '001'
down_revision = None


def upgrade():
    conn = op.get_bind()

    if not conn.dialect.has_table(conn, 'Books'):
        conn.execute(
            '''
            CREATE TABLE Books (
                id UUID PRIMARY KEY,
                name VARCHAR(200) NOT NULL,
                author VARCHAR(150) NOT NULL,
                date_of_release DATE NOT NULL,
                description VARCHAR(250) NOT NULL,
                genre VARCHAR(100) NOT NULL
            )
            '''
        )


def downgrade():
    conn = op.get_bind()
    conn.execute('DROP TABLE Books')
