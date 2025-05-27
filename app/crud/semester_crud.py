from sqlalchemy.orm import Session
from app.models.semesters import Semester
from app.schemas.semester_schema import SemesterSchema, addSemester


def get_semesters(db: Session):
    return db.query(Semester).all()

def get_semester_by_id(db: Session, semester_id: int):
    return db.query(Semester).filter(Semester.id == semester_id).first()    


def create_semester(db: Session, data: addSemester):
    new_semester = Semester(**data.dict())
    db.add(new_semester)
    db.commit()
    db.refresh(new_semester)
    return new_semester


def update_semester(db: Session, data: addSemester, semester_id: int):
    search_semester = db.query(Semester).filter(Semester.id == semester_id).first()
    if not search_semester:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(search_semester, field, value)
    db.commit()
    db.refresh(search_semester)
    return search_semester


def delete_semester(db: Session, semester_id: int):
    search_semester = db.query(Semester).filter(Semester.id == semester_id).first()
    if not search_semester:
        return None
    db.delete(search_semester)
    db.commit()
    return {"message": "El semestre ha sido eliminado"}