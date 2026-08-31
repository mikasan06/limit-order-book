from order import Order, Side
from orderbook import OrderBook


def process(book: OrderBook, order: Order):
    """Process an incoming order: match it against the book, rest any remainder.
    Returns the list of trades that happened."""
    trades = []

    while order.quantity > 0:
        if order.side == Side.BUY:
            this_book = book.asks
            best = book.best_ask()
            crosses = best is not None and order.price >= best
        else:
            this_book = book.bids
            best = book.best_bid()
            crosses = best is not None and order.price <= best

        if not crosses:
            break

        level = this_book[best]
        resting = level[0]

        trade_qty = min(order.quantity, resting.quantity)
        trades.append((best, trade_qty, resting.id, order.id))

        order.quantity -= trade_qty
        resting.quantity -= trade_qty

        if resting.quantity == 0:
            level.remove(resting)
            del book._orders[resting.id]
            if not level:
                del this_book[best]

    if order.quantity > 0:
        book.add(order)

    return trades