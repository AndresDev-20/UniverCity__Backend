from pydantic import BaseModel
from enum import Enum



class UserRole(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"

class UserSchema(BaseModel):
    firstNames: str
    surNames: str
    email: str
    role: UserRole

class UserWhitId(UserSchema):
    id: int

class addUser(UserSchema):
    password: str