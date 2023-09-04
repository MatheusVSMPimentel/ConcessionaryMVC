"""empty message

Revision ID: 7bf1b32b6527
Revises: f2c1072d4394
Create Date: 2023-09-04 16:13:03.809925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bf1b32b6527'
down_revision = 'f2c1072d4394'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Veiculos',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('Tipo', sa.Integer(), nullable=True),
    sa.Column('Cor', sa.String(length=70), nullable=True),
    sa.Column('Marca', sa.String(length=70), nullable=True),
    sa.Column('Modelo', sa.String(length=70), nullable=True),
    sa.Column('AnoFabricacao', sa.String(length=20), nullable=True),
    sa.Column('Novo', sa.Boolean(), nullable=True),
    sa.Column('KmRodados', sa.Integer(), nullable=True),
    sa.Column('Leilao', sa.Boolean(), nullable=True),
    sa.Column('Parcela', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Veiculos')
    # ### end Alembic commands ###
