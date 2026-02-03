"""에러 코드 정의 및 매핑"""

from typing import Dict, Tuple

# code_name -> (status_code, default_detail_message)
ERROR_CODES: Dict[str, Tuple[int, str]] = {
    # 사용자 관련 에러 (4xx)
    "USER-001": (404, "사용자를 찾을 수 없습니다."),
    "USER-002": (422, "이미 존재하는 사용자입니다."),
    "USER-003": (422, "이미 사용 중인 이메일입니다."),
    "USER-004": (401, "잘못된 인증 정보입니다."),
    
    # 인증/인가 관련 에러 (4xx)
    "JWT-001": (401, "인증이 필요합니다."),
    "JWT-002": (403, "접근 권한이 없습니다."),
    
}


def get_error_info(error_code: str) -> Tuple[int, str]:
    """code_name에 해당하는 status_code와 detail 메시지를 반환"""
    if error_code in ERROR_CODES:
        return ERROR_CODES[error_code]
    # 정의되지 않은 code_name인 경우 기본값 반환
    return (500, f"알 수 없는 에러 코드: {error_code}")

