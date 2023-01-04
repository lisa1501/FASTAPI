"""add content column to posts table

Revision ID: daf6e8aec6f3
Revises: 1168fecd2af8
Create Date: 2023-01-03 18:51:59.278190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daf6e8aec6f3'
down_revision = '1168fecd2af8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
