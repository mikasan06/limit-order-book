from order import Order, Side


class OrderBook:
    def __init__(self):
        self.bids = {}
        self.asks = {}
        self._orders = {} # id -> order

    def add(self, order: Order):
        if order.side == Side.BUY:
            self.bids.setdefault(order.price, []).append(order)
        else:
            self.asks.setdefault(order.price, []).append(order)
        self._orders[order.id] = order

    def cancel(self, order_id: int):
        order = self._orders[order_id]
        price = order.price
        side = order.side

        book = self.bids if side == Side.BUY else self.asks
        book[price].remove(order)
        if not book[price]:
            del book[price]

        del self._orders[order_id]
            
    def best_bid(self):
        if not self.bids:
            return None
        return max(self.bids)

    def best_ask(self):
        if not self.asks:
            return None
        return min(self.asks)