from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Semester(Base):
    __tablename__ = "semesters"
    id = Column(BigInteger, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=True)

    # Muchos semestres pertenecen a un programa
    program_id = Column(BigInteger, ForeignKey("programs.id"), nullable=False)
    program = relationship("Program", back_populates="semesters")

    # Un semestre tiene muchas notas
    grades = relationship("Grade", back_populates="semester")
