from sqlalchemy import Table, Column, BigInteger, ForeignKey
from app.db.base_class import Base


teachers_programs = Table(
    "teachers_programs",
    Base.metadata,
    Column("teacher_id", BigInteger, ForeignKey("users.id")),
    Column("program_id", BigInteger, ForeignKey("programs.id")),
)