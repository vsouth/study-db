"""Added Author table and relation

Revision ID: 8a98e5a11d0b
Revises: 75232a2bc3c5
Create Date: 2023-07-28 19:43:15.479493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a98e5a11d0b'
down_revision = '75232a2bc3c5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('books', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'books', 'authors', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'books', type_='foreignkey')
    op.drop_column('books', 'author_id')
    op.drop_table('authors')
    # ### end Alembic commands ###
