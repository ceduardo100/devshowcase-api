"""add project rating and upvotes

Revision ID: f99628a8c1f9
Revises: fix_project_tech_feedback
Create Date: 2026-09-24 16:36:51.370390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f99628a8c1f9"
down_revision: Union[str, Sequence[str], None] = "fix_project_tech_feedback"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "projects",
        sa.Column("upvotes", sa.Integer(), nullable=False, server_default="0"),
    )

    op.add_column(
        "projects",
        sa.Column("average_rating", sa.Float(), nullable=False, server_default="0"),
    )


def downgrade() -> None:
    op.drop_column("projects", "average_rating")
    op.drop_column("projects", "upvotes")
