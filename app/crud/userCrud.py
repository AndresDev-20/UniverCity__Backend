from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.userSchema import UserSchema, addUser
from app.core.security import hash_password, verify_password



def get_user(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, data: addUser):
    hashed_password = hash_password(data.password)
    add_user = User(firstNames = data.firstNames, surNames = data.surNames, email = data.email, password = hashed_password, role = data.role)
    db.add(add_user)
    db.commit()
    db.refresh(add_user)
    return add_user


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