"""make device nullable

Revision ID: 242b78fe1705
Revises: 
Create Date: 2023-11-23 09:56:50.279886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '242b78fe1705'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('device',
               existing_type=sa.VARCHAR(length=200),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('device',
               existing_type=sa.VARCHAR(length=200),
               nullable=False)

    # ### end Alembic commands ###
