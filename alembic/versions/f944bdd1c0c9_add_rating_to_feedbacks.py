"""add rating to feedbacks

Revision ID: f944bdd1c0c9
Revises: f99628a8c1f9
Create Date: 2026-09-24 16:44:31.192362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f944bdd1c0c9"
down_revision: Union[str, Sequence[str], None] = "f99628a8c1f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "feedbacks",
        sa.Column("rating", sa.Integer(), nullable=False, server_default="1"),
    )


def downgrade() -> None:
    op.drop_column("feedbacks", "rating")
