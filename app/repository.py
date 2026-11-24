from app.models import Item, OrderRequest


class ItemRepository:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id = 1

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get_by_name(self, name: str) -> Item | None:
        return next(
            (item for item in self._items.values() if item.name.lower() == name.lower()),
            None,
        )

    def create(self, name: str, price: float) -> Item:
        item = Item(id=self._next_id, name=name, price=price)
        self._items[item.id] = item
        self._next_id += 1
        return item


item_repository = ItemRepository()


class OrderRepository:
    def __init__(self) -> None:
        self._orders: list[dict] = []
        self._next_order_id = 1

    def save(self, order: OrderRequest) -> dict:
        saved_order = {
            "order_id": self._next_order_id,
            **order.model_dump(),
        }
        self._orders.append(saved_order)
        self._next_order_id += 1
        return saved_order

    def list_all(self) -> list[dict]:
        return list(self._orders)


order_repository = OrderRepository()
