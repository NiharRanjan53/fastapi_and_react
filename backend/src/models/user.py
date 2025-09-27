from sqlalchemy import Column, Integer, String, Boolean
from src.db.session import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    contact_number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)