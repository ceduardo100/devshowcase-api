"""create feedbacks table

Revision ID: a6d72d252ab3
Revises: 0586cfbf41c4
Create Date: 2026-09-23 16:28:03.844568

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a6d72d252ab3"
down_revision: Union[str, Sequence[str], None] = "0586cfbf41c4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "feedbacks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("profile_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        op.f("ix_feedbacks_id"),
        "feedbacks",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        op.f("ix_feedbacks_id"),
        table_name="feedbacks",
    )

    op.drop_table("feedbacks")
