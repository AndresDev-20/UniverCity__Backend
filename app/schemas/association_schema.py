from pydantic import BaseModel


class AssociationSchema(BaseModel):
    teacher_id: int
    program_id: int

    class Config:
        from_attributes = True