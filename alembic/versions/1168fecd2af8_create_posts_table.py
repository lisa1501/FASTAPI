"""create posts table

Revision ID: 1168fecd2af8
Revises: 
Create Date: 2023-01-03 18:42:39.065038

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1168fecd2af8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
