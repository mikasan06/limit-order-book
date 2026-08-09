import pytest

from order import Order, Side
from orderbook import OrderBook


def test_best_bid_and_ask_are_none_when_empty():
    book = OrderBook()
    assert book.best_bid() is None
    assert book.best_ask() is None


def test_best_bid_is_highest_price():
    book = OrderBook()
    book.add(Order(Side.BUY, 100.0, 10))
    book.add(Order(Side.BUY, 101.0, 5))
    book.add(Order(Side.BUY, 99.0, 5))
    assert book.best_bid() == 101.0


def test_best_ask_is_lowest_price():
    book = OrderBook()
    book.add(Order(Side.SELL, 105.0, 10))
    book.add(Order(Side.SELL, 103.0, 5))
    book.add(Order(Side.SELL, 106.0, 5))
    assert book.best_ask() == 103.0


def test_orders_at_same_price_keep_arrival_order():
    book = OrderBook()
    first = Order(Side.BUY, 100.0, 10)
    second = Order(Side.BUY, 100.0, 5)
    book.add(first)
    book.add(second)
    assert book.bids[100.0] == [first, second]


def test_cancel_removes_order_from_book():
    book = OrderBook()
    order = Order(Side.BUY, 100.0, 10)
    book.add(order)
    book.cancel(order.id)
    assert order.id not in book._orders
    assert order not in book.bids.get(100.0, [])


def test_cancel_removes_empty_price_level():
    book = OrderBook()
    order = Order(Side.BUY, 100.0, 10)
    book.add(order)
    book.cancel(order.id)
    assert 100.0 not in book.bids


def test_cancel_leaves_other_orders_at_same_level():
    book = OrderBook()
    first = Order(Side.BUY, 100.0, 10)
    second = Order(Side.BUY, 100.0, 5)
    book.add(first)
    book.add(second)
    book.cancel(first.id)
    assert book.bids[100.0] == [second]


def test_cancel_unknown_id_raises_key_error():
    book = OrderBook()
    with pytest.raises(KeyError):
        book.cancel(12345)


def test_best_bid_updates_after_cancel():
    book = OrderBook()
    lower = Order(Side.BUY, 100.0, 10)
    higher = Order(Side.BUY, 101.0, 5)
    book.add(lower)
    book.add(higher)
    book.cancel(higher.id)
    assert book.best_bid() == 100.0