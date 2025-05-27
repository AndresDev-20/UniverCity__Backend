from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  
from app.schemas.program_schema import ProgramSchema, addProgram
from app.crud.program_crud import get_programs, get_program_by_id, create_program, update_program, delete_program
from app.api.desp import get_db
from app.auth.dependencies import get_admin_user, get_admin_or_teacher_user, get_current_user

router = APIRouter()

@router.get("/", response_model=list[ProgramSchema])
async def read_programs(db: Session = Depends(get_db)):
    return get_programs(db)

@router.get("/{program_id}", response_model=addProgram)
async def read_program(program_id: int, db: Session = Depends(get_db)):
    program = get_program_by_id(db, program_id)
    if not program:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return program

@router.post("/create", response_model=addProgram) 
async def create_new_program(program: addProgram, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    return create_program(db, program)

@router.put("/update/{program_id}", response_model=addProgram)
async def update_existing_program(program_id: int, program: addProgram, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    updated_program = update_program(db, program, program_id)
    if not updated_program:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return updated_program

@router.delete("/delete/{program_id}")
async def delete_existing_program(program_id: int, db: Session = Depends(get_db), current_user = Depends(get_admin_user)):
    result = delete_program(db, program_id)
    if not result:
        raise HTTPException(status_code=404, detail="Programa no encontrado")
    return result