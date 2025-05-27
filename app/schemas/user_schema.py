from pydantic import BaseModel
from enum import Enum
from app.schemas.program_schema import ProgramSchema as Program
from app.schemas.grade_schema import GradeSchema as Grade
from typing import List, Optional



class UserRole(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"

class UserSchema(BaseModel):
    firstNames: str
    surNames: str
    email: str
    role: UserRole


    class Config:
        from_attributes: True



class UserWhitId(UserSchema):
    id: int


# Para crear el administrador
class addUserAdmin(UserSchema):
    role: UserRole = UserRole.admin
    password: str



# Para los estudiantes
class UserStudents(UserWhitId):
    program_student: Optional[Program] 
    grades: List[Grade] = [] 

class addUserStudent(UserSchema):
    role: UserRole = UserRole.student
    program_id: int
    password: str




# Para los profesores
class UserTeachers(UserWhitId):
    programs: List[Program] = [] 

class addTeacher(UserSchema):
    role: UserRole = UserRole.teacher
    password: str





