"""create projects table

Revision ID: 0586cfbf41c4
Revises: 97de7e49590c
Create Date: 2026-09-23 16:18:58.817662

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0586cfbf41c4"
down_revision: Union[str, Sequence[str], None] = "97de7e49590c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("github_url", sa.String(length=255), nullable=True),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_projects_id"),
        "projects",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_projects_id"),
        table_name="projects",
    )

    op.drop_table("projects")
