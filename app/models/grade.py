from sqlalchemy import Column, BigInteger, String, ForeignKey, Double
from sqlalchemy.orm import relationship
from app.db.base_class import Base



class Grade(Base):
    __tablename__ = "grades"
    id = Column(BigInteger, primary_key=True, index=True)
    grade = Column(Double, nullable=False)

    # Relacion de muchos a uno con los semsestres
    semester_id = Column(BigInteger, ForeignKey("semesters.id"), nullable=False)
    semester = relationship("Semester", back_populates="grades")

    # Relacion de muchos a uno con los estudiantes
    student_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    student = relationship("User", back_populates="grades")