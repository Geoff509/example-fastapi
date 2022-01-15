"""add user table

Revision ID: 29413d5c5c5b
Revises: c3076109b022
Create Date: 2022-01-16 01:58:12.634822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29413d5c5c5b'
down_revision = 'c3076109b022'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False), 
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
