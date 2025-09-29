from sqlalchemy import Column, Integer, String, Boolean
from src.db.session import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    hashed_password = Column(String(512), nullable=False)
    firstname = Column(String(10), nullable=False)
    lastname = Column(String(10), nullable=False)
    age = Column(Integer, nullable=True)
    contact_number = Column(String(15), nullable=True)
    is_active = Column(Boolean, default=True)