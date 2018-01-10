"""create tables

Revision ID: 557dcf670064
Revises: 
Create Date: 2018-01-10 10:44:28.707863

"""
from alembic import op
import sqlalchemy as sa
import datetime



# revision identifiers, used by Alembic.
revision = '557dcf670064'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'dcon_lender_eligbl',
        sa.Column('eligbl_id', sa.Integer(), primary_key=True, autoincrement=True),
	    sa.Column('cp_id', sa.Integer(), nullable=False),
	    sa.Column('st_cd', sa.String(20)),
	    sa.Column('prod_type', sa.String(20), nullable=False),
	    sa.Column('app_type', sa.String(20), nullable=False, default='I'),
	    sa.Column('deal_type', sa.String(20), nullable=False),
	    sa.Column('dt_verification_in', sa.String(20), nullable=False),
	    sa.Column('incld_in', sa.String(20), nullable=False, default='Y'),
	    sa.Column('veh_typ_cd',sa.String(20)),
	    sa.Column('created_ts',sa.DateTime(), default=datetime.datetime.utcnow),
	    sa.Column('updtd_ts',sa.DateTime(), default=datetime.datetime.utcnow),
	    sa.Column('modified_by',sa.String(20)),
	    sa.Column('effective_ts',sa.DateTime()),
    )

def downgrade():
    op.drop_table('dcon_lender_eligbl')
