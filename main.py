# main.py 생성
from fastapi import FastAPI
from user.interface.user_controller import router as user_router
from common.exception_handler import register_exception_handlers

app = FastAPI()

app.include_router(user_router)
register_exception_handlers(app)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}