from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class TransactionCreate(BaseModel):
    email: str
    amount: float
    category: str
    date: str
    description: str
