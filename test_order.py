from order import Order, Side


def test_construction_sets_fields():
    order = Order(Side.BUY, 100.0, 10)
    assert order.side == Side.BUY
    assert order.price == 100.0
    assert order.quantity == 10


def test_ids_are_unique_per_instance():
    first = Order(Side.BUY, 100.0, 10)
    second = Order(Side.SELL, 101.0, 5)
    assert first.id != second.id


def test_explicit_id_is_respected():
    order = Order(Side.BUY, 100.0, 10, id=999)
    assert order.id == 999


def test_repr_contains_key_fields():
    order = Order(Side.BUY, 100.0, 10, id=1)
    text = repr(order)
    assert "BUY" in text
    assert "100" in text
    assert "10" in text