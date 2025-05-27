from pydantic import BaseModel
from app.schemas.semester_schema import SemesterSchema as Semester


class addProgram(BaseModel):
    name_program: str
    description: str
    duration: str  # in months
    spelled_title: str

    class Config:
        from_attributes = True

class ProgramSchema(addProgram):
    id: int
    semesters: list[Semester] = []
