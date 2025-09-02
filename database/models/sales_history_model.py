from sqlalchemy import Column, Integer, Date, String, Float, ForeignKey
from database.connection import Base

class sales_history_model (Base):
    __tablename__ = "sales_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    count = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    fk_partners_id = Column(Integer, ForeignKey("partners.id"), nullable=False)
    fk_products_id = Column(Integer, ForeignKey("products.id"), nullable=False)


