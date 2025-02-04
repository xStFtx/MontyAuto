from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' cdn.example.com; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "frame-src 'none'; "
            "object-src 'none'"
        )

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        response.headers.update({
            "Content-Security-Policy": self.csp,
            "Permissions-Policy": "geolocation=(), microphone=()",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            "Feature-Policy": "geolocation 'none'; microphone 'none'"
        })
        return response 