from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database.connection import Base

class partners_model (Base):
    __tablename__ = "partners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    director = Column(String, nullable=False)
    email = Column (String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    inn = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)


