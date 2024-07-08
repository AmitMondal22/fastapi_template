from config.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key = True)
    company_id = Column(Integer)
    date = Column(DateTime)
    stars = Column(Integer)
    comment = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)