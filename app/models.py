from pydantic import BaseModel, Field


class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)


class Item(ItemCreate):
    id: int


class OrderItem(BaseModel):
    name: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(ge=0)


class OrderRequest(BaseModel):
    customer_name: str = Field(min_length=1)
    items: list[OrderItem] = Field(min_length=1)


class OrderResponse(BaseModel):
    order_id: int
    customer_name: str
    items: list[OrderItem]
    total: float
