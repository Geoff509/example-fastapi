"""add last few columns to posts table"

Revision ID: e83134ef063e
Revises: 2f52a0ecc877
Create Date: 2022-01-16 02:23:17.154985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e83134ef063e'
down_revision = '2f52a0ecc877'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade():
    op.add_column('posts', 'published'),
    op.add_column('posts', 'created')
    pass
