"""empty message

Revision ID: bbf223ee1b22
Revises: 3f9b152cec25
Create Date: 2019-03-19 18:35:58.415370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbf223ee1b22'
down_revision = '3f9b152cec25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projectlist', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('projectlist', 'create_time')
    # ### end Alembic commands ###
