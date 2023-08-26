"""create_index_for_genre

Revision ID: 002
Revises: 001
Create Date: 2023-08-25

"""

from alembic import op

revision = '002'
down_revision = '001'


def upgrade():
    op.create_index('idx_genre', 'Books', ['genre'])


def downgrade():
    op.drop_index('idx_genre', table_name='Books')
