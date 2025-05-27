from sqlalchemy.orm import Session
from app.models.program import Program
from app.schemas.program_schema import ProgramSchema, addProgram


def get_programs(db: Session):
    return db.query(Program).all()


def get_program_by_id(db: Session, program_id: int):
    return db.query(Program).filter(Program.id == program_id).first()


def create_program(db: Session, data: addProgram):
    new_program = Program(**data.dict())
    db.add(new_program)
    db.commit()
    db.refresh(new_program)
    return new_program

def update_program(db: Session, data: addProgram, program_id: int):
    search_program = db.query(Program).filter(Program.id == program_id).first()
    if not search_program:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(search_program, field, value)
    db.commit()
    db.refresh(search_program)
    return search_program

def delete_program(db: Session, program_id: int):
    search_program = db.query(Program).filter(Program.id == program_id).first()
    if not search_program:
        return None
    db.delete(search_program)
    db.commit()
    return {"message": "El programa se ha sido eliminado"}