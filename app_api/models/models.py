from sqlalchemy import Column, Integer, String, Float
from modules.connect import Base



class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    input_value = Column(Float)
    result = Column(Float)

