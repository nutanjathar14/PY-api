from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import get_products, get_product, create_product, update_product
from schemas import ProductCreate, ProductUpdate, ProductResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/product/list", response_model=list[ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    return get_products(db, skip=(page - 1) * 10, limit=10)

@router.get("/product/{pid}/info", response_model=ProductResponse)
def retrieve_product(pid: int, db: Session = Depends(get_db)):
    product = get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.put("/product/{pid}/update", response_model=ProductResponse)
def modify_product(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    updated_product = update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
