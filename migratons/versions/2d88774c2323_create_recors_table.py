"""create_recors_table

Revision ID: 2d88774c2323
Revises: 
Create Date: 2024-11-07 13:55:10.995037

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2d88774c2323"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "records",
        sa.Column("uid", sa.UUID(), nullable=False),
        sa.Column("idf", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("asc_org", sa.String(), nullable=False),
        sa.Column("general_data", sa.String(), nullable=False),
        sa.Column("activity_data", sa.String(), nullable=False),
        sa.Column("info_support_data", sa.String(), nullable=False),
        sa.Column("admin_service_data", sa.String(), nullable=False),
        sa.Column("resp_person_data", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("uid"),
        sa.UniqueConstraint("idf"),
    )


def downgrade() -> None:
    op.drop_table("employees")
