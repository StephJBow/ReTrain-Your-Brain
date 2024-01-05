"""empty message

Revision ID: 0ae07880e3a7
Revises: 41b0247a0f3b
Create Date: 2023-09-20 11:09:24.157022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ae07880e3a7'
down_revision = '41b0247a0f3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testimonials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reviewer_name', sa.String(length=64), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testimonials')
    # ### end Alembic commands ###