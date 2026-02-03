"""커스텀 예외 클래스 정의"""

class BusinessException(Exception):
    def __init__(self, error_code: str, detail: str | None = None):
        self.error_code = error_code
        self.detail = detail
        super().__init__(self.detail or error_code)

