from order import Order, Side
from orderbook import OrderBook


def process(book: OrderBook, order: Order):
    """
    An incoming order arrives. Does it cross the book and trade,
    or rest? Return the trades that happened (a list).
    """
    trades = []

    # 1. Which side of the book do we match AGAINST?
    #    A buy matches against asks; a sell against bids. (opposite side)

    if order.side == Side.BUY:
        best = book.best_ask()  
        #    buy crosses if its price >= best ask
        crosses = best is not None and order.price >= best  
    else:
        best = book.best_bid()
        #    sell crosses if its price <= best bid
        crosses = best is not None and order.price <= best  
    
    if not crosses:
        book.add(order)
        return
    #    If nothing to cross (empty side, or no price overlap) -> rest it, done.

    # 3. While it still crosses AND has quantity left:
    #      - take the best opposite price level
    #      - match against the FRONT of that level's queue (oldest first)
    #      - a trade happens for min(incoming qty, resting qty)
    #      - reduce both; if the resting order hits zero, remove it
    #        (from the level AND the id-index — your invariant)
    #      - record the trade
    #      - if the level empties, move to the next best price

    # 4. If the incoming order still has quantity after all crossing
    #    is exhausted -> rest the remainder in the book.

    return trades