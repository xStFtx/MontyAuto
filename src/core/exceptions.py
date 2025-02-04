from fastapi import HTTPException, status
from starlette.requests import Request
from starlette.responses import JSONResponse

class AutomationException(Exception):
    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message

async def automation_exception_handler(request: Request, exc: AutomationException):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )

class InvalidAPIKeyError(AutomationException):
    def __init__(self):
        super().__init__(
            code="invalid_api_key",
            message="Invalid or missing API key"
        )

class RateLimitExceededError(AutomationException):
    def __init__(self):
        super().__init__(
            code="rate_limit_exceeded",
            message="Too many requests"
        ) 