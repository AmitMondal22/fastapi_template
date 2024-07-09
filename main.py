from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from json import JSONEncoder
from decimal import Decimal
from datetime import date, datetime, timedelta
import uvicorn
from config.database import Session, engine, Base

from routers.comment_routes import comment_router
from routers.auth_routes import auth_routes

app = FastAPI()
app.title = "Fastapi Template"
app.version = "0.0.1"
origins = [
    "http://127.0.0.1:8001",
    "http://localhost:8001",
    "*"
]
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Custom JSON encoder
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return flobjat(obj)
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, timedelta):
            return str(obj)
        elif isinstance(obj, set):
            return list(obj)
        elif isinstance(obj, dict):
            return {key: self.default(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [self.default(element) for element in obj]
        elif isinstance(obj, tuple):
            return tuple(self.default(element) for element in obj)
        return super().default(obj)

# Set the custom JSON encoder for FastAPI
app.json_encoder = CustomJSONEncoder



app.include_router(comment_router)
app.include_router(auth_routes, prefix="/api/v1/auth", tags=["authorization"])

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)