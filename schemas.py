from pydantic import BaseModel, HttpUrl, constr
from datetime import datetime

class ProductBase(BaseModel):
    name: constr(max_length=100)
    category: str
    description: constr(max_length=250) = None
    product_image: HttpUrl
    sku: constr(max_length=100)
    unit_of_measure: str
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        from_attributes = True
