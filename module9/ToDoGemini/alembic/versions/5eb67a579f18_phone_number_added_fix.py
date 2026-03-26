"""phone number added fix

Revision ID: 5eb67a579f18
Revises: 18e968a9b8c0
Create Date: 2026-03-24 23:10:51.961991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5eb67a579f18'
down_revision: Union[str, None] = '18e968a9b8c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))


def downgrade() -> None:
    pass
