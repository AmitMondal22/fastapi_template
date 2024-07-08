from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session, engine, Base

from app.routers.auth_routers import comment_router

app = FastAPI()
app.title = "Medium Tutorial FastAPI"
app.version = "0.0.1"

app.include_router(comment_router)

Base.metadata.create_all(bind=engine)