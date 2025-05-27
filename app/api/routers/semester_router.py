from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.semester_schema import SemesterSchema, addSemester
from app.crud.semester_crud import (
    get_semesters,
    get_semester_by_id,
    create_semester,
    update_semester,
    delete_semester
)
from app.api.desp import get_db
from app.auth.dependencies import get_admin_user

router = APIRouter()
@router.get("/", response_model=list[SemesterSchema])
async def read_semesters(db: Session = Depends(get_db)):
    semesters = get_semesters(db)
    return semesters


@router.get("/{semester_id}", response_model=SemesterSchema)
async def read_semester(semester_id: int, db: Session = Depends(get_db)):
    semester = get_semester_by_id(db, semester_id)
    if not semester:
        raise HTTPException(status_code=404, detail="Semester not found")
    return semester


@router.post("/create", response_model=SemesterSchema)
async def create_new_semester(semester: addSemester, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    return create_semester(db, semester)


@router.put("/update/{semester_id}", response_model=SemesterSchema)
async def update_existing_semester(semester_id: int, semester: addSemester, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    updated_semester = update_semester(db, semester, semester_id)
    if not updated_semester:
        raise HTTPException(status_code=404, detail="Semester not found")
    return updated_semester


@router.delete("/delete/{semester_id}")
async def delete_existing_semester(semester_id: int, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    result = delete_semester(db, semester_id)
    if not result:
        raise HTTPException(status_code=404, detail="Semester not found")
    return result