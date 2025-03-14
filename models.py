from sqlalchemy import Column, Integer, String, Enum, Text, TIMESTAMP
from datetime import datetime
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum("finished", "semi-finished", "raw", name="category_enum"), nullable=False)
    description = Column(String(250))
    product_image = Column(Text)
    sku = Column(String(100), nullable=False)
    unit_of_measure = Column(Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack", name="uom_enum"), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    updated_date = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

Base.metadata.create_all(bind=engine)
