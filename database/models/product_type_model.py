from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base

class product_type_model (Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    koef = Column(Float, nullable=False)

