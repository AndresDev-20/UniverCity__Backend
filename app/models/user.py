from sqlalchemy import Column, BigInteger, String, Enum, ForeignKey, and_
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.models.association import teachers_programs
from app.models.grade import Grade
import enum


class UserRole(enum.Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class User(Base):
    __tablename__= "users"
    id = Column(BigInteger, primary_key=True, index=True)
    firstNames = Column(String)
    surNames = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(UserRole), nullable=False)

    # Para los estudiantes
    program_id = Column(BigInteger, ForeignKey("programs.id"), nullable=True)
    program_student = relationship("Program", back_populates="students") 

    # Relación de uno a muchos con las notas
    grades = relationship(
        "Grade", 
        back_populates="student", 
        primaryjoin=and_(
        id == Grade.student_id,
        role == UserRole.student
    )
    )

    # Para los profesores (muchos a muchos)
    programs_teacher = relationship("Program", secondary=teachers_programs, back_populates="teachers")
