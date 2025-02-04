"""Initial migration

Revision ID: 0001
Revises: 
Create Date: 2023-01-01 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'jobs',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('status', sa.String(20), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, onupdate=sa.func.now())
    )

def downgrade():
    op.drop_table('jobs') 