from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_index('idx_users_email', 'users', ['email'], unique=True)
    op.create_index('idx_users_created', 'users', ['created_at'])
    op.create_foreign_key(
        'fk_trades_user_id',
        'trades',
        'users',
        ['user_id'],
        ['id']
    )

def downgrade():
    op.drop_index('idx_users_email', 'users')
    op.drop_index('idx_users_created', 'users')
    op.drop_constraint('fk_trades_user_id', 'trades', type_='foreignkey') 