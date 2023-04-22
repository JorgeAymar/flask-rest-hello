"""empty message

Revision ID: ea209528ad1f
Revises: 49a962478b64
Create Date: 2023-04-22 18:30:19.345594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea209528ad1f'
down_revision = '49a962478b64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favcharacters',
    sa.Column('favoritoID', sa.Integer(), nullable=False),
    sa.Column('customerID', sa.Integer(), nullable=True),
    sa.Column('characterID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characterID'], ['characters.characterID'], ),
    sa.ForeignKeyConstraint(['customerID'], ['customers.customerID'], ),
    sa.PrimaryKeyConstraint('favoritoID')
    )
    op.create_table('favplanets',
    sa.Column('favoritoID', sa.Integer(), nullable=False),
    sa.Column('customerID', sa.Integer(), nullable=True),
    sa.Column('planetID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customerID'], ['customers.customerID'], ),
    sa.ForeignKeyConstraint(['planetID'], ['planets.planetID'], ),
    sa.PrimaryKeyConstraint('favoritoID')
    )
    op.drop_table('favoritos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos',
    sa.Column('favoritoID', sa.INTEGER(), server_default=sa.text('nextval(\'"favoritos_favoritoID_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('characterID', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('planetID', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('isActive', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('customerID', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['characterID'], ['characters.characterID'], name='favoritos_characterID_fkey'),
    sa.ForeignKeyConstraint(['customerID'], ['customers.customerID'], name='favoritos_customerID_fkey'),
    sa.ForeignKeyConstraint(['planetID'], ['planets.planetID'], name='favoritos_planetID_fkey'),
    sa.PrimaryKeyConstraint('favoritoID', name='favoritos_pkey')
    )
    op.drop_table('favplanets')
    op.drop_table('favcharacters')
    # ### end Alembic commands ###
