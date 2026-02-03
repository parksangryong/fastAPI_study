"""에러 코드 정의 및 매핑"""

from typing import Dict, Tuple

# code_name -> (status_code, default_detail_message)
ERROR_CODES: Dict[str, Tuple[int, str]] = {
    # 사용자 관련 에러 (4xx)
    "USER_NOT_FOUND": (404, "사용자를 찾을 수 없습니다."),
    "USER_ALREADY_EXISTS": (422, "이미 존재하는 사용자입니다."),
    "USER_EMAIL_DUPLICATE": (422, "이미 사용 중인 이메일입니다."),
    "USER_INVALID_CREDENTIALS": (401, "잘못된 인증 정보입니다."),
    
    # 인증/인가 관련 에러 (4xx)
    "UNAUTHORIZED": (401, "인증이 필요합니다."),
    "FORBIDDEN": (403, "접근 권한이 없습니다."),
    
    # 리소스 관련 에러 (4xx)
    "RESOURCE_NOT_FOUND": (404, "요청한 리소스를 찾을 수 없습니다."),
    "RESOURCE_CONFLICT": (409, "리소스 충돌이 발생했습니다."),
    
    # 서버 에러 (5xx)
    "INTERNAL_SERVER_ERROR": (500, "서버 내부 오류가 발생했습니다."),
    "DATABASE_ERROR": (500, "데이터베이스 오류가 발생했습니다."),
}


def get_error_info(code_name: str) -> Tuple[int, str]:
    """code_name에 해당하는 status_code와 detail 메시지를 반환"""
    if code_name in ERROR_CODES:
        return ERROR_CODES[code_name]
    # 정의되지 않은 code_name인 경우 기본값 반환
    return (500, f"알 수 없는 에러 코드: {code_name}")

