"""empty message

Revision ID: 1d3205518d40
Revises: 89106a963367
Create Date: 2023-04-21 17:30:43.696000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d3205518d40'
down_revision = '89106a963367'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.drop_column('phonenumber')
        batch_op.drop_column('address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('customers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('phonenumber', sa.VARCHAR(length=50), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
