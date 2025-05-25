from fastapi import FastAPI
from app.api.routers import userRouter


app = FastAPI()

app.include_router(userRouter.router, prefix="/users", tags=["Etiqueta(users)"])

@app.get("/")
def welcome():
    return {"Message": "Welcome to FastAPI"}