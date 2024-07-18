async def add_client():
    try:
        data= ""
        resdata = successResponse(data, message="Register Success")
        return JSONResponse(status_code=200, content=jsonable_encoder(resdata))
    except HTTPException as he:
        return JSONResponse(status_code=he.status_code, content=jsonable_encoder(errorResponse(message=he.detail)))
    except Exception as e:
        # Handle any other unexpected exceptions
        return JSONResponse(status_code=500, content=jsonable_encoder(errorResponse(message="Internal server error")))