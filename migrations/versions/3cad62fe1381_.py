"""empty message

Revision ID: 3cad62fe1381
Revises: None
Create Date: 2015-01-16 11:56:41.395932

"""

# revision identifiers, used by Alembic.
revision = '3cad62fe1381'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('company', sa.String(length=255), nullable=True),
    sa.Column('bus_type', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('company_id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('company_purchases',
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.Column('item', sa.Text(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.company_id'], ),
    sa.PrimaryKeyConstraint('purchase_id')
    )
    op.create_table('company_contact',
    sa.Column('company_contact_id', sa.Integer(), nullable=False),
    sa.Column('contact_name', sa.String(length=255), nullable=True),
    sa.Column('address_1', sa.String(length=255), nullable=True),
    sa.Column('address_2', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('fax_number', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('fin', sa.String(length=255), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.company_id'], ),
    sa.PrimaryKeyConstraint('company_contact_id')
    )
    op.create_table('contracts',
    sa.Column('contracts_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('contract_number', sa.String(length=255), nullable=True),
    sa.Column('county', sa.String(length=255), nullable=True),
    sa.Column('type_of_contract', sa.String(length=255), nullable=True),
    sa.Column('pa', sa.String(length=255), nullable=True),
    sa.Column('expiration', sa.DateTime(), nullable=True),
    sa.Column('spec_number', sa.String(length=255), nullable=True),
    sa.Column('controller_number', sa.Integer(), nullable=True),
    sa.Column('commcode', sa.Integer(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.company_id'], ),
    sa.PrimaryKeyConstraint('contracts_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contracts')
    op.drop_table('company_contact')
    op.drop_table('company_purchases')
    op.drop_table('roles')
    op.drop_table('users')
    op.drop_table('company')
    ### end Alembic commands ###
