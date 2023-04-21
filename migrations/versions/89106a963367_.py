"""empty message

Revision ID: 89106a963367
Revises: 257450bdb1fd
Create Date: 2023-04-21 00:09:24.852378

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89106a963367'
down_revision = '257450bdb1fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('categoryID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('categoryID'),
    sa.UniqueConstraint('name')
    )
    op.create_table('customers',
    sa.Column('customerID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phonenumber', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=50), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('customerID'),
    sa.UniqueConstraint('name')
    )
    op.create_table('characters',
    sa.Column('characterID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('birthYear', sa.String(length=50), nullable=True),
    sa.Column('height', sa.String(length=50), nullable=True),
    sa.Column('mass', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.String(length=50), nullable=True),
    sa.Column('hairColor', sa.String(length=50), nullable=True),
    sa.Column('skinColor', sa.String(length=50), nullable=True),
    sa.Column('homeworld', sa.String(length=50), nullable=True),
    sa.Column('categoryID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryID'], ['category.categoryID'], ),
    sa.PrimaryKeyConstraint('characterID'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planets',
    sa.Column('planetID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('population', sa.String(length=50), nullable=True),
    sa.Column('rotationPeriod', sa.String(length=50), nullable=True),
    sa.Column('orbitalPeriod', sa.String(length=50), nullable=True),
    sa.Column('diameter', sa.String(length=50), nullable=True),
    sa.Column('gravity', sa.String(length=50), nullable=True),
    sa.Column('terrainGlasslands', sa.String(length=50), nullable=True),
    sa.Column('surfaceWater', sa.String(length=50), nullable=True),
    sa.Column('climate', sa.String(length=50), nullable=True),
    sa.Column('categoryID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryID'], ['category.categoryID'], ),
    sa.PrimaryKeyConstraint('planetID'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favoritos',
    sa.Column('favoritoID', sa.Integer(), nullable=False),
    sa.Column('customer_ID', sa.Integer(), nullable=True),
    sa.Column('characterID', sa.Integer(), nullable=True),
    sa.Column('planetID', sa.Integer(), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['characterID'], ['characters.characterID'], ),
    sa.ForeignKeyConstraint(['customer_ID'], ['customers.customerID'], ),
    sa.ForeignKeyConstraint(['planetID'], ['planets.planetID'], ),
    sa.PrimaryKeyConstraint('favoritoID')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favoritos')
    op.drop_table('planets')
    op.drop_table('characters')
    op.drop_table('customers')
    op.drop_table('category')
    # ### end Alembic commands ###
