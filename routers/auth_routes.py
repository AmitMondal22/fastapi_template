from fastapi import APIRouter, HTTPException, Response
import json
from typing import Optional, List

from app.controllers.auth import UserAuthController

from app.models import UserModel

from library.responce import successResponse,errorResponse
from library.ObjectEncoder import ObjectEncoder

auth_routes = APIRouter()

# @auth_routes.post('/login', tags=['login'])
# # @auth_routes.post('/login', tags=['login'], response_model=List[Comment])
# # async def login(user:AuthModel.Login) -> List[Comment]:
# async def login(user:AuthModel.Login):
#     try:
#         data= await UserAuthController.login(user)
#         resdata = successResponse(data, message="Login Success")
#         return Response(content=json.dumps(resdata, cls=ObjectEncoder), media_type="application/json", status_code=200)
#     except ValueError as ve:
#         errordata = errorResponse(message="Validation Error",data=ve)
#         raise HTTPException(status_code=400, detail=json.dumps(errordata))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail="Internal server error")
    
@auth_routes.post('/login', tags=['login'])
async def login(user:UserModel.Login):
    try:
        data= await UserAuthController.login(user)
        resdata = successResponse(data, message="Login Success")
        return Response(content=json.dumps(resdata, cls=ObjectEncoder), media_type="application/json", status_code=200)
    except ValueError as ve:
        errordata = errorResponse(message="Validation Error",data=ve)
        raise HTTPException(status_code=400, detail=json.dumps(errordata))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
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