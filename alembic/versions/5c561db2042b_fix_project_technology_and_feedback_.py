"""fix project technology and feedback relationships"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fix_project_tech_feedback"
down_revision = "a6d72d252ab3"
branch_labels = None
depends_on = None


def upgrade():
    # Remove a antiga relação Profile N:N Technology
    op.drop_table("profile_technologies")

    # Cria a relação correta Project N:N Technology
    op.create_table(
        "project_technologies",
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("technology_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["technology_id"],
            ["technologies.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("project_id", "technology_id"),
    )

    # Adiciona project_id aos feedbacks
    op.add_column(
        "feedbacks",
        sa.Column("project_id", sa.Integer(), nullable=True),
    )

    op.create_foreign_key(
        "fk_feedbacks_project_id_projects",
        "feedbacks",
        "projects",
        ["project_id"],
        ["id"],
        ondelete="CASCADE",
    )

    # Aproveita os feedbacks existentes e associa ao primeiro projeto
    op.execute(
        """
        UPDATE feedbacks
        SET project_id = (
            SELECT id
            FROM projects
            ORDER BY id
            LIMIT 1
        )
        WHERE project_id IS NULL
        """
    )

    # project_id passa a ser obrigatório
    op.alter_column(
        "feedbacks",
        "project_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    # Remove a antiga relação Feedback -> Profile
    op.drop_constraint(
        "feedbacks_profile_id_fkey",
        "feedbacks",
        type_="foreignkey",
    )

    op.drop_column("feedbacks", "profile_id")


def downgrade():
    # Restaura profile_id nos feedbacks
    op.add_column(
        "feedbacks",
        sa.Column("profile_id", sa.Integer(), nullable=True),
    )

    op.create_foreign_key(
        "fk_feedbacks_profile_id_profiles",
        "feedbacks",
        "profiles",
        ["profile_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.execute(
        """
        UPDATE feedbacks
        SET profile_id = (
            SELECT id
            FROM profiles
            ORDER BY id
            LIMIT 1
        )
        WHERE profile_id IS NULL
        """
    )

    op.alter_column(
        "feedbacks",
        "profile_id",
        existing_type=sa.Integer(),
        nullable=False,
    )

    op.drop_constraint(
        "fk_feedbacks_project_id_projects",
        "feedbacks",
        type_="foreignkey",
    )

    op.drop_column("feedbacks", "project_id")

    # Restaura Profile N:N Technology
    op.drop_table("project_technologies")

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
