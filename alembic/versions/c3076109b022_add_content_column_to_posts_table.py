"""add content column to posts table

Revision ID: c3076109b022
Revises: b4690a443ef1
Create Date: 2022-01-16 01:48:57.121080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3076109b022'
down_revision = 'b4690a443ef1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
