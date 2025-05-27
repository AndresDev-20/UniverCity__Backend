from sqlalchemy.orm import Session
from app.models.grade import Grade
from app.schemas.grade_schema import GradeSchema, addGrade


def get_grades(db: Session):
    return db.query(Grade).all()    


def get_grade_by_id(db: Session, grade_id: int):
    return db.query(Grade).filter(Grade.id == grade_id).first()


def create_grade(db: Session, data: addGrade):
    new_grade = Grade(**data.dict())
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade


def update_grade(db: Session, data: addGrade, grade_id: int):
    search_grade = db.query(Grade).filter(Grade.id == grade_id).first()
    if not search_grade:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(search_grade, field, value)
    db.commit()
    db.refresh(search_grade)
    return search_grade


def delete_grade(db: Session, grade_id: int):
    search_grade = db.query(Grade).filter(Grade.id == grade_id).first()
    if not search_grade:
        return None
    db.delete(search_grade)
    db.commit()
    return {"message": "La calificación ha sido eliminada"}