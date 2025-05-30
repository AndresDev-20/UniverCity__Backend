"""Tercera migración

Revision ID: 229a34b7f8d6
Revises: ab81de94556d
Create Date: 2025-05-26 10:55:36.658635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '229a34b7f8d6'
down_revision: Union[str, None] = 'ab81de94556d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('programs',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name_program', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('spelled_title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_programs_id'), 'programs', ['id'], unique=False)
    op.create_table('semesters',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('program_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_semesters_id'), 'semesters', ['id'], unique=False)
    op.create_table('grades',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('grade', sa.Double(), nullable=False),
    sa.Column('semester_id', sa.BigInteger(), nullable=False),
    sa.Column('student_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['semester_id'], ['semesters.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grades_id'), 'grades', ['id'], unique=False)
    op.create_table('teachers_programs',
    sa.Column('teacher_id', sa.BigInteger(), nullable=True),
    sa.Column('program_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['program_id'], ['programs.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], )
    )
    op.add_column('users', sa.Column('program_id', sa.BigInteger(), nullable=True))
    op.create_foreign_key(None, 'users', 'programs', ['program_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'program_id')
    op.drop_table('teachers_programs')
    op.drop_index(op.f('ix_grades_id'), table_name='grades')
    op.drop_table('grades')
    op.drop_index(op.f('ix_semesters_id'), table_name='semesters')
    op.drop_table('semesters')
    op.drop_index(op.f('ix_programs_id'), table_name='programs')
    op.drop_table('programs')
    # ### end Alembic commands ###
