from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  
from app.schemas.grade_schema import GradeSchema, addGrade
from app.crud.grade_crud import (
    get_grades, 
    get_grade_by_id, 
    create_grade, 
    update_grade, 
    delete_grade
)

from app.api.desp import get_db
from app.auth.dependencies import get_teacher_user, get_current_user


router = APIRouter()
@router.get("/", response_model=list[GradeSchema])
async def read_grades(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return get_grades(db)


@router.get("/{grade_id}", response_model=GradeSchema)
async def read_grade(grade_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    grade = get_grade_by_id(db, grade_id)
    if not grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return grade


@router.post("/create", response_model=GradeSchema)
async def create_new_grade(grade: addGrade, db: Session = Depends(get_db), current_user = Depends(get_teacher_user)):
    return create_grade(db, grade)


@router.put("/update/{grade_id}", response_model=GradeSchema)
async def update_existing_grade(grade_id: int, grade: addGrade, db: Session = Depends(get_db), current_user = Depends(get_teacher_user)):
    updated_grade = update_grade(db, grade, grade_id)
    if not updated_grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return updated_grade


@router.delete("/delete/{grade_id}")
async def delete_existing_grade(grade_id: int, db: Session = Depends(get_db), current_user = Depends(get_teacher_user)):
    result = delete_grade(db, grade_id)
    if not result:
        raise HTTPException(status_code=404, detail="Grade not found")
    return result