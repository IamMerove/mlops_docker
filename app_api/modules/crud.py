from sqlalchemy.orm import Session
from models.models import Calculation


def create_calculation(db: Session, operation: str, val: float, res: float):
    db_calc = Calculation(operation=operation, input_value=val, result=res)
    db.add(db_calc)
    db.commit()
    db.refresh(db_calc)
    return db_calc


def get_all_calculations(db: Session):
    return db.query(Calculation).all()
