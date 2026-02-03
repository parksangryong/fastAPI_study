from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from pydantic import ValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """요청 검증 에러 처리 (422)"""
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "status_code": 400}
    )

async def http_exception_handler(request: Request, exc: HTTPException | StarletteHTTPException):
    """HTTPException 처리 (FastAPI 및 Starlette HTTP 예외)"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "status_code": exc.status_code}
    )

async def general_exception_handler(request: Request, exc: Exception):
    """일반 예외 처리 (500)"""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "status_code": 500}
    )


def register_exception_handlers(app):
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)