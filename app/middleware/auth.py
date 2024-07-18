from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from config.JWT_config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from library.jwt_token import verify_token


class JWTMiddleware(BaseHTTPMiddleware):
    async def superAdminMW(self, request: Request, call_next):
        if "authorization" not in request.headers:
            raise HTTPException(status_code=403, detail="Authorization header missing")

        token = request.headers["authorization"].split("Bearer ")[1]
        if not token:
            raise HTTPException(status_code=403, detail="Token missing")
        
        decoded_token = verify_token(token)
        print(decoded_token.encode)
        if not decoded_token:
            raise HTTPException(status_code=403, detail="Invalid token")
        
        request.state.user = decoded_token
        response = await call_next(request)
        return response