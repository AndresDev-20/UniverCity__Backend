from sqlalchemy.orm import Session
from sqlalchemy import insert
from app.models.user import User
from app.models.association import teachers_programs
from app.models.program import Program
from app.schemas.user_schema import UserSchema, addUserStudent, addTeacher, addUserAdmin
from app.schemas.association_schema import AssociationSchema
from app.core.security import hash_password, verify_password
from typing import List



def get_user(db: Session):
    return db.query(User).all()


def get_user_rol(db: Session, role):
    user = db.query(User).filter(User.role == role).all()
    return user


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_admin(db: Session, data: addUserAdmin):
    hashed_password = hash_password(data.password)
    add_admin = User(firstNames = data.firstNames, surNames = data.surNames, email = data.email, password = hashed_password, role = data.role)
    db.add(add_admin)
    db.commit()
    db.refresh(add_admin)
    return add_admin


def create_student(db: Session, data: addUserStudent):
    hashed_password = hash_password(data.password)
    add_student = User(firstNames = data.firstNames, surNames = data.surNames, email = data.email, password = hashed_password, role = data.role, program_id = data.program_id)
    db.add(add_student)
    db.commit()
    db.refresh(add_student)
    return add_student


def create_teacher(db: Session, data: addTeacher):
    hashed_password = hash_password(data.password)
    add_teacher = User(firstNames = data.firstNames, surNames = data.surNames, email = data.email, password = hashed_password, role = data.role)
    db.add(add_teacher)
    db.commit()
    db.refresh(add_teacher)
    return add_teacher


def add_association(db: Session, data: AssociationSchema):
    teacher = db.query(User).filter(User.id == data.teacher_id).first()
    program = db.query(Program).filter(Program.id == data.program_id).first()
    if not teacher or not program:
        return None
    stmt = insert(teachers_programs).values(teacher_id=teacher.id, program_id=program.id)
    db.execute(stmt)
    db.commit()
    return {"teacher_id": teacher.id, "program_id": program.id}


def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def update_user(db: Session, data: UserSchema, user_id: int):
    search_user = db.query(User).filter(User.id == user_id).first()
    if not search_user:
        return None
    for index, dates in data.dict().items():
        setattr(search_user, index, dates)
    db.commit()
    db.refresh(search_user)
    return search_user


def delete_user(db: Session, user_id: int):
    search_user = db.query(User).filter(User.id == user_id).first()
    if not search_user:
        return None
    db.delete(search_user)
    db.commit()
    return {"message": "El usuario ha sido eliminado"}