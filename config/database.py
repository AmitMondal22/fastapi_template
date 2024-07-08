import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_username = 'root'
database_password = 'root'
database_ip       = 'localhost'  # Assuming your database is running locally
database_name     = 'fastapitest'
database_port     = 3306

# Use proper string formatting
engine = create_engine(f'mysql+mysqlconnector://{database_username}:{database_password}@{database_ip}:{database_port}/{database_name}')

Session = sessionmaker(bind=engine)
Base = declarative_base()
