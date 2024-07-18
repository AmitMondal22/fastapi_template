from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.sql import func
from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date
from config.database import Base
import enum
import re

    
class User(Base):
    __tablename__ = 'md_client'

    client_id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    client_mobile = Column(String)
    client_email = Column(String)
    client_cities_id = Column(Integer)
    client_state_id = Column(Integer)
    client_countri_id = Column(Integer)
    create_by = Column(Integer, default=None, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
