from sqlalchemy import String, BigInteger, Column, ForeignKey, and_
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.association import teachers_programs
from app.models.user import User, UserRole

class Program(Base):
    __tablename__ = "programs"
    id = Column(BigInteger, primary_key=True, index=True)
    name_program = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    spelled_title = Column(String, nullable=True)

    # Un programa tiene muchos semestres
    semesters = relationship("Semester", back_populates="program")

    # Un programa tiene muchos estudiantes
    students = relationship(
        "User",
        back_populates="program_student",
        primaryjoin=and_(
        User.program_id == id,
        User.role == UserRole.student
    )
    ) 

    # Muchos a muchos con profesores
    teachers = relationship("User", secondary=teachers_programs, back_populates="programs_teacher")
