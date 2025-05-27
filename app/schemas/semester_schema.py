from pydantic import BaseModel


class addSemester(BaseModel):
    title: str
    description: str
    program_id: int

    class Config:
        from_attributes = True

class SemesterSchema(addSemester):
    id: int 
