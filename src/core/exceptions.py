from fastapi import HTTPException, status

class AutomationException(HTTPException):
    def __init__(self, code: str, message: str, status_code: int):
        super().__init__(
            status_code=status_code,
            detail={
                "code": code,
                "message": message
            }
        )

class InvalidAPIKeyError(AutomationException):
    def __init__(self):
        super().__init__(
            code="invalid_api_key",
            message="Invalid or missing API key",
            status_code=status.HTTP_403_FORBIDDEN
        )

class RateLimitExceededError(AutomationException):
    def __init__(self):
        super().__init__(
            code="rate_limit_exceeded",
            message="Too many requests",
            status_code=status.HTTP_429_TOO_MANY_REQUESTS
        ) 