from sqlalchemy import Column, BigInteger, String, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
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
