# main.py 생성
from fastapi import FastAPI
from user.interface.user_controller import router as user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}