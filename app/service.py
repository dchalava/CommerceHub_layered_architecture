from fastapi import HTTPException, status

from app.models import (
    Item,
    ItemCreate,
    OrderItem,
    OrderRequest,
    OrderResponse,
)
from app.repository import (
    ItemRepository,
    OrderRepository,
    item_repository,
    order_repository,
)


class ItemService:
    def __init__(self, repository: ItemRepository) -> None:
        self._repository = repository

    def list_items(self) -> list[Item]:
        return self._repository.list()

    def create_item(self, item_data: ItemCreate) -> Item:
        if self._repository.get_by_name(item_data.name):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An item with this name already exists",
            )

        return self._repository.create(item_data.name, item_data.price)


item_service = ItemService(item_repository)


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def create_order(self, order: OrderRequest) -> OrderResponse:
        saved_order = self._repository.save(order)
        return self._to_response(saved_order)

    def list_orders(self) -> list[OrderResponse]:
        return [self._to_response(order) for order in self._repository.list_all()]

    def _to_response(self, order: dict) -> OrderResponse:
        items = [OrderItem.model_validate(item) for item in order["items"]]
        total = round(
            sum(item.quantity * item.unit_price for item in items),
            2,
        )
        return OrderResponse(
            order_id=order["order_id"],
            customer_name=order["customer_name"],
            items=items,
            total=total,
        )


order_service = OrderService(order_repository)
