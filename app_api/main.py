from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import models
from modules import connect, crud
from maths import mon_module
from modules.connect import engine  # Au lieu de modules.database
# On initialise les tables de la base de données au démarrage
models.Base.metadata.create_all(bind=engine)
connect.init_db()

app = FastAPI(title='MLOPS Project API')

# Fonction pour récuperer la session de BDD

def get_db():
    db =connect.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message":"API is running"}

# Route 1 : Faire un calcul et l'enregistrer

@app.post("/compute/{operation}")

def compute_and_save(operation: str, value: float, db :Session = Depends(get_db)):
    # On effectue le calcul
    if operation == "square":
        result = mon_module.square(value)
    elif operation == "add":
        result = mon_module.add(value, 1)
    elif operation == "sub":
        result = mon_module.sub(value, 1)
    else:
        raise HTTPException(status_code=400, detail="Opération non supportée")

    # On enregistre en BDD via CRUD
    new_entry = crud.create_calculation(db, operation, value, result)

    return {"status": "success", "data": new_entry}

# Route 2 : Récuperer tout l'historique

@app.get("/data")
def get_history(db:Session = Depends(get_db)):
    history = crud.get_all_calculations(db)
    return history
