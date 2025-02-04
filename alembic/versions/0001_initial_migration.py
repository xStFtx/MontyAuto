"""Initial migration

Revision ID: 0001
Revises: 
Create Date: 2023-01-01 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('created_at', sa.DateTime, default=sa.func.now())
    )

def downgrade():
    op.drop_table('users') 