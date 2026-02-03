from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from common.exception.exceptions import BusinessException
from common.exception.error_codes import get_error_info


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """요청 검증 에러 처리 (422)"""
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors(), "error_code": "VALIDATION_ERROR"}
    )

async def business_exception_handler(request: Request, exc: BusinessException):
    """비즈니스 로직 예외 처리"""
    status_code, default_detail = get_error_info(exc.error_code)
    detail_message = exc.detail if exc.detail else default_detail
    
    return JSONResponse(
        status_code=status_code,
        content={
            "detail": detail_message,
            "error_code": exc.error_code
        }
    )

async def http_exception_handler(request: Request, exc: HTTPException | StarletteHTTPException):
    """HTTPException 처리 (FastAPI 및 Starlette HTTP 예외)"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "error_code": "HTTP_ERROR"}
    )

async def general_exception_handler(request: Request, exc: Exception):
    """일반 예외 처리 (500)"""
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error_code": "SERVER_ERROR"}
    )

def register_exception_handlers(app):
    # 비즈니스 예외 
    app.add_exception_handler(BusinessException, business_exception_handler)
    # 라우팅 에러
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    # 검증 에러
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    # HTTPException
    app.add_exception_handler(HTTPException, http_exception_handler)
    # 일반 예외
    app.add_exception_handler(Exception, general_exception_handler)