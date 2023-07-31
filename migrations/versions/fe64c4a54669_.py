"""empty message

Revision ID: fe64c4a54669
Revises: 
Create Date: 2023-07-31 14:33:04.623402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe64c4a54669'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('treatments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('treatment_name', sa.String(length=64), nullable=True),
    sa.Column('treatment_price', sa.Integer(), nullable=True),
    sa.Column('treatment_length', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('treatment_name', sa.String(length=64), nullable=True),
    sa.Column('treatment_date', sa.Integer(), nullable=True),
    sa.Column('treatment_time', sa.Integer(), nullable=True),
    sa.Column('treatment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['treatment_id'], ['treatments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('treatments')
    # ### end Alembic commands ###