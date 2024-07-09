from fastapi import HTTPException
from sqlalchemy.orm import Session
from config.database import Session

from app.models import UserModel
from library.date_time_format import get_current_datetime
from library.has_password import get_password_hash

db = Session()
@staticmethod
async def login(user:UserModel.Login):
    try:
        return user.email
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@staticmethod
async def register(register_data:UserModel.Register):
    try:
         # Create SQLAlchemy model instance
        db_user = UserModel.User(
            first_name=register_data.first_name,
            last_name=register_data.last_name,
            user_name=register_data.user_name,
            mobile_no=register_data.mobile_no,
            user_email=register_data.email,
            email_verified_at=get_current_datetime(),
            user_role=register_data.user_role,
            password=get_password_hash(register_data.password)
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")