from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from config.database import Session
from app.models.models import Comment as CommentModel
from fastapi.encoders import jsonable_encoder
from app.services.CommentService import CommentService
from schemas.user_schemas import Comment

comment_router = APIRouter()

# Get records from the comments table
@comment_router.get('/comments', tags=['comments'], response_model=List[Comment], status_code=200)
def get_comments() -> List[Comment]:
    db = Session()
    result = CommentService(db).get_comments(1)
    if not result:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))