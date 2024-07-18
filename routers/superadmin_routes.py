from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from library.responce import successResponse,errorResponse

from app.controllers.auper_admin import ClientController

from schemas.superadmin import ClientSchemas


superadmin_routes = APIRouter()



@superadmin_routes.post('/client/add', tags=['superadmin_client'])
async def add_client(params:ClientSchemas.AddSuperAdminClient):
    try:
        data= ClientController.add_client(params)
        resdata = successResponse(data, message="Register Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except HTTPException as he:
        return JSONResponse(status_code=he.status_code, content=jsonable_encoder(errorResponse(message=he.detail)))
    except Exception as e:
        # Handle any other unexpected exceptions
        return JSONResponse(status_code=500, content=jsonable_encoder(errorResponse(message="Internal server error")))