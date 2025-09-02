from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base

class material_type_model (Base):
    __tablename__ = "material_type"

    id = Column(Integer, primary_key=True, autoincrement=True)
    material_type = Column(String, nullable=False)
    defect = Column(Float, nullable=False)

