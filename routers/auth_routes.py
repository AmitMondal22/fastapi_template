from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse
import json
from typing import Optional, List
from fastapi.encoders import jsonable_encoder


from app.controllers.auth import UserAuthController

from app.models import UserModel

from library.responce import successResponse,errorResponse
from library.ObjectEncoder import ObjectEncoder

auth_routes = APIRouter()

@auth_routes.post('/login', tags=['login'])
async def login(user:UserModel.Login):
    try:
        data= await UserAuthController.login(user)
        resdata = successResponse(data, message="Login Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except ValueError as ve:
        errordata = errorResponse(message="Validation Error",data=ve)
        raise JSONResponse(status_code=400, content=errordata)
    except Exception as e:
        raise JSONResponse(status_code=500, content="Internal server error")
    
@auth_routes.post('/register', tags=['register'])
async def register(user:UserModel.Register):
    try:
        data= await UserAuthController.register(user)
        return  successResponse(data, message="Register Success")
    except ValueError as ve:
        errordata = errorResponse(message="Validation Error",data=ve)
        raise HTTPException(status_code=400, detail=json.dumps(errordata))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")