"""fix field

Revision ID: 15dbc2c73fd8
Revises: 04390adc6a64
Create Date: 2024-12-27 01:27:38.276864

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "15dbc2c73fd8"
down_revision: Union[str, None] = "04390adc6a64"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "wallet_request",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.Column("bandwith", sa.Float(), nullable=False),
        sa.Column("energy", sa.Float(), nullable=False),
        sa.Column("balance", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_wallet_request_address"),
        "wallet_request",
        ["address"],
        unique=True,
    )
    op.create_index(
        op.f("ix_wallet_request_id"), "wallet_request", ["id"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_wallet_request_id"), table_name="wallet_request")
    op.drop_index(
        op.f("ix_wallet_request_address"), table_name="wallet_request"
    )
    op.drop_table("wallet_request")
    # ### end Alembic commands ###
