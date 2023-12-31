"""Deleted Book(author_name) column

Revision ID: 15e386ab1823
Revises: a7a355b92ac2
Create Date: 2023-07-28 20:08:50.608582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e386ab1823'
down_revision = 'a7a355b92ac2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'author_name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('author_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
