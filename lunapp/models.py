from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    amount = Column(Float)
    category = Column(String)
    date = Column(String)
    description = Column(String)

# También puedes agregar Budget, FixedPayment...
