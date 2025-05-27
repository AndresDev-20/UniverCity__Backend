from pydantic import BaseModel
from typing import Optional
from app.schemas.semester_schema import SemesterSchema as semester_schema


class addGrade(BaseModel):
    grade: float
    student_id: int
    semester_id: int

    class Config:
        from_attributes = True

class GradeSchema(addGrade):
    semester: Optional[semester_schema] = None
    id: int