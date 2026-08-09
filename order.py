from enum import Enum, auto
from dataclasses import dataclass, field
from itertools import count


class Side(Enum):
    BUY = auto()
    SELL = auto()


_order_ids = count(1)


@dataclass
class Order:
    side: Side
    price: float
    quantity: int
    id: int = field(default_factory=lambda: next(_order_ids))

    def __repr__(self):
        return f"Order(#{self.id} {self.side.name} {self.quantity}@{self.price})"