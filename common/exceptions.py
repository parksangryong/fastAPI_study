"""커스텀 예외 클래스 정의"""


class BusinessException(Exception):
    """비즈니스 로직 예외
    
    code_name을 통해 status_code와 detail 메시지를 매핑합니다.
    """
    def __init__(self, code_name: str, detail: str | None = None):
        self.code_name = code_name
        self.detail = detail
        super().__init__(self.detail or code_name)

