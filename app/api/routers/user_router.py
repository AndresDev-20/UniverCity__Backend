from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.crud import user_crud as user_crud
from app.schemas import user_schema, association_schema
from app.api.desp import get_db
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.jwt import create_access_token
from app.auth.dependencies import get_admin_user, get_current_user
from app.core.config import settings
import datetime



router = APIRouter()


@router.get("/", response_model=List[user_schema.UserWhitId])
async def read_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_crud.get_user(db)


@router.get("/students", response_model=List[user_schema.UserStudents])
async def read_students(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_crud.get_user_rol(db, "student")

 
@router.get("/teachers", response_model=List[user_schema.UserTeachers])
async def read_teachers(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return user_crud.get_user_rol(db, "teacher")



@router.get("/{user_id}", response_model=user_schema.UserSchema)
async def get_user_id(user_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_user = user_crud.get_user_by_id(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_user


@router.post("/admin/create", response_model=user_schema.UserSchema)
async def create_admin(data: user_schema.addUserAdmin, db: Session = Depends(get_db)):
    return user_crud.create_admin(db=db, data=data)


@router.post("/student/create", response_model=user_schema.UserSchema)
async def create_student(data: user_schema.addUserStudent, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    return user_crud.create_student(db=db, data=data)



@router.post("/teacher/create", response_model=user_schema.UserSchema)
async def create_teacher(data: user_schema.addTeacher, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    return user_crud.create_teacher(db=db, data=data)


@router.post("/teacher/addprogram", response_model=association_schema.AssociationSchema)
async def add_program_teacher_by_id(data: association_schema.AssociationSchema, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    res = user_crud.add_association(db=db, data=data)
    if res is None:
        raise HTTPException(status_code=404, detail="Profesor o programa no encontrado")
    return res


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas"
        )
    access_token_expires = datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": str(user.id), "role": user.role.value}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}



@router.put("/update/{user_id}", response_model=user_schema.UserSchema)
async def user_update(data: user_crud.UserSchema, user_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    search_user = user_crud.update_user(db=db, data=data, user_id=user_id)
    if search_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return search_user



@router.delete("/delete/{user_id}")
async def user_delete(user_id: int, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    user_search = user_crud.delete_user(user_id=user_id, db=db)
    if user_search is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"Message": "El usuario ha sido eliminado"}