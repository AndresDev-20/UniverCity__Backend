from fastapi import FastAPI
from app.api.routers import user_router
from app.api.routers import program_router
from app.api.routers import semester_router
from app.api.routers import grade_router


app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["Etiqueta(users con roles)"])
app.include_router(program_router.router, prefix="/programs", tags=["Etiqueta(programs)"])
app.include_router(semester_router.router, prefix="/semesters", tags=["Etiqueta(semesters)"])
app.include_router(grade_router.router, prefix="/grades", tags=["Etiqueta(grades)"])

@app.get("/")
def welcome():
    return {"Message": "Welcome to FastAPI"}