from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# creacion de bd
from database import Base, engine
import models
# Crear tablas
Base.metadata.create_all(bind=engine)



app = FastAPI()

# Permitir peticiones desde React Native
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulación de base de datos
users_db = {}
transactions_db = {}
budgets_db = {}
fixed_payments_db = {}

# Modelos
class User(BaseModel):
    email: str
    password: str

class Transaction(BaseModel):
    id: int
    email: str
    amount: float
    category: str
    date: str
    description: str

class Budget(BaseModel):
    email: str
    category: str
    limit: float

class FixedPayment(BaseModel):
    id: int
    email: str
    name: str
    amount: float
    day: int  # día del mes

# -------------------
# Endpoints básicos
# -------------------
@app.get("/")
def read_root():
    return {"message": "API de LanaApp funcionando!"}

# Registro
@app.post("/register")
def register(user: User):
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Usuario ya existe")
    users_db[user.email] = user.password
    return {"message": "Usuario registrado correctamente"}

# Login
@app.post("/login")
def login(user: User):
    if user.email not in users_db:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    if users_db[user.email] != user.password:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    return {"access_token": "fake_token_for_" + user.email}

# -------------------
# CRUD Transacciones
# -------------------
@app.post("/transactions/")
def create_transaction(tx: Transaction):
    transactions_db[tx.id] = tx
    return {"message": "Transacción creada"}

@app.get("/transactions/{email}", response_model=List[Transaction])
def get_transactions(email: str):
    return [tx for tx in transactions_db.values() if tx.email == email]

@app.put("/transactions/{tx_id}")
def update_transaction(tx_id: int, tx: Transaction):
    if tx_id not in transactions_db:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    transactions_db[tx_id] = tx
    return {"message": "Transacción actualizada"}

@app.delete("/transactions/{tx_id}")
def delete_transaction(tx_id: int):
    if tx_id not in transactions_db:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    del transactions_db[tx_id]
    return {"message": "Transacción eliminada"}

# -------------------
# CRUD Presupuestos
# -------------------
@app.post("/budgets/")
def create_budget(budget: Budget):
    key = (budget.email, budget.category)
    budgets_db[key] = budget.limit
    return {"message": "Presupuesto creado"}

@app.get("/budgets/{email}")
def get_budgets(email: str):
    return [
        {"category": cat, "limit": limit}
        for (e, cat), limit in budgets_db.items()
        if e == email
    ]

@app.put("/budgets/")
def update_budget(budget: Budget):
    key = (budget.email, budget.category)
    if key not in budgets_db:
        raise HTTPException(status_code=404, detail="Presupuesto no encontrado")
    budgets_db[key] = budget.limit
    return {"message": "Presupuesto actualizado"}

@app.delete("/budgets/")
def delete_budget(budget: Budget):
    key = (budget.email, budget.category)
    if key not in budgets_db:
        raise HTTPException(status_code=404, detail="Presupuesto no encontrado")
    del budgets_db[key]
    return {"message": "Presupuesto eliminado"}

# -------------------
# CRUD Pagos Fijos
# -------------------
@app.post("/fixed_payments/")
def create_fixed_payment(fp: FixedPayment):
    fixed_payments_db[fp.id] = fp
    return {"message": "Pago fijo creado"}

@app.get("/fixed_payments/{email}", response_model=List[FixedPayment])
def get_fixed_payments(email: str):
    return [fp for fp in fixed_payments_db.values() if fp.email == email]

@app.put("/fixed_payments/{fp_id}")
def update_fixed_payment(fp_id: int, fp: FixedPayment):
    if fp_id not in fixed_payments_db:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    fixed_payments_db[fp_id] = fp
    return {"message": "Pago fijo actualizado"}

@app.delete("/fixed_payments/{fp_id}")
def delete_fixed_payment(fp_id: int):
    if fp_id not in fixed_payments_db:
        raise HTTPException(status_code=404, detail="Pago fijo no encontrado")
    del fixed_payments_db[fp_id]
    return {"message": "Pago fijo eliminado"}

# -------------------
# Datos para gráficas (simulado)
# -------------------
@app.get("/charts/{email}")
def get_charts(email: str):
    # Simulamos datos
    return {
        "income_by_category": {"salario": 1000, "extra": 500},
        "expenses_by_category": {"comida": 400, "transporte": 200},
        "income_vs_expenses": {"income": 1500, "expenses": 600}
    }
