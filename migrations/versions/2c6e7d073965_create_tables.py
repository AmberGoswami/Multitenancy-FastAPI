"""Create tables

Revision ID: 2c6e7d073965
Revises: 
Create Date: 2023-07-19 13:24:20.402907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6e7d073965'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tenants',
    sa.Column('Id', sa.UUID(), nullable=False),
    sa.Column('Name', sa.String(), nullable=True),
    sa.Column('Email', sa.String(), nullable=True),
    sa.Column('Password', sa.String(), nullable=True),
    sa.Column('Created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('Id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tenants', schema='public')
    # ### end Alembic commands ###
