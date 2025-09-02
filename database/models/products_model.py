from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base

class product_model (Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    article = Column(String, nullable=False)
    name = Column(String, nullable=False)
    min_cost = Column(Float, nullable=False)
    fk_type = Column(Integer, ForeignKey('product_type.id'), nullable=False)
