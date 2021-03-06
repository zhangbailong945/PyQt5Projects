"""empty message

Revision ID: 119e3ac2e1cf
Revises: 554f5d3ea258
Create Date: 2021-04-07 17:36:14.855174

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '119e3ac2e1cf'
down_revision = '554f5d3ea258'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('a_name', sa.String(length=32), nullable=True),
    sa.Column('d_legs', sa.Integer(), nullable=True),
    sa.Column('c_eat', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('a_name')
    )
    op.add_column('users', sa.Column('gender', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=22), nullable=True))
    op.drop_index('u_name', table_name='users')
    op.drop_column('users', 'u_name')
    op.drop_column('users', 'u_des')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('u_des', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('users', sa.Column('u_name', mysql.VARCHAR(length=22), nullable=True))
    op.create_index('u_name', 'users', ['u_name'], unique=True)
    op.drop_column('users', 'name')
    op.drop_column('users', 'gender')
    op.drop_table('animals')
    # ### end Alembic commands ###
