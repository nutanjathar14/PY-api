from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate, ProductUpdate

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def get_product(db: Session, pid: int):
    return db.query(Product).filter(Product.id == pid).first()

def create_product(db: Session, product: ProductCreate):
    new_product = Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(db: Session, pid: int, product: ProductUpdate):
    existing_product = db.query(Product).filter(Product.id == pid).first()
    if existing_product:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(existing_product, key, value)
        db.commit()
        db.refresh(existing_product)
    return existing_product