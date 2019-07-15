"""empty message

Revision ID: 1bc439737530
Revises: 760d615570c2
Create Date: 2019-07-13 09:01:12.724143

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1bc439737530'
down_revision = '760d615570c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('booksname', table_name='tbl_authors')
    op.drop_column('tbl_authors', 'booksname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('booksname', mysql.VARCHAR(length=32), nullable=True))
    op.create_index('booksname', 'tbl_authors', ['booksname'], unique=True)
    # ### end Alembic commands ###