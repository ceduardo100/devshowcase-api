"""create profile technologies relationship

Revision ID: 97de7e49590c
Revises: e21d83823f52
Create Date: 2026-09-23 15:21:06.075336

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97de7e49590c'
down_revision: Union[str, Sequence[str], None] = 'e21d83823f52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "profile_technologies",
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.Column("technology_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["technology_id"],
            ["technologies.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("profile_id", "technology_id"),
    )


def downgrade() -> None:
    op.drop_table("profile_technologies")
