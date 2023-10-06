from typing import Dict
from app.dto.trader import Trader


class Queue:

    def __init__(self, max_size: int):
        self._queue = []
        self._max_size = max_size
        self._size = 0

    @property
    def max_size(self):
        return self._max_size

    @property
    def queue(self):
        return self._queue

    @property
    def size(self):
        return self._size

    @max_size.setter
    def max_size(self, value: int):
        raise NotImplementedError("Cannot change queue size")

    @queue.setter
    def queue(self, value):
        raise NotImplementedError("Cannot change the queue")

    @size.setter
    def size(self, value):
        raise NotImplementedError("Cannot set the size")

    def enqueue(self, item: Trader):
        if not isinstance(item, Trader):
            raise ValueError("item should be type of Trader")
        queue_len = len(self._queue)
        if queue_len >= self._max_size:
            raise OverflowError("Queue is overflow")
        self._queue = [item, *self._queue]
        self._size += 1
        return

    def dequeue(self):
        self._size -= 1
        return self._queue.pop()

    def __iter__(self):
        while self._size > 0:
            yield self.dequeue()


if __name__ == "__main__":
    traders = [
        {
            "name": "herath",
            "transaction_type": "sell",
            "asset_type": "TRY",
            "asset_value": 300.45,
            "quantity": 500
        },
        {
            "name": "nimal",
            "transaction_type": "sell",
            "asset_type": "TRY",
            "asset_value": 300.45,
            "quantity": 1000
        },
        {
            "name": "pathum",
            "transaction_type": "buy",
            "asset_type": "ASD",
            "asset_value": 45678.45,
            "quantity": 1000
        },
        {
            "name": "kamal",
            "transaction_type": "buy",
            "asset_type": "RDG",
            "asset_value": 456.34,
            "quantity": 2000
        },
        {
            "name": "amila",
            "transaction_type": "buy",
            "asset_type": "EDT",
            "asset_value": 190.45,
            "quantity": 30000
        },
        {
            "name": "pushpa",
            "transaction_type": "buy",
            "asset_type": "EDT",
            "asset_value": 190.45,
            "quantity": 20000
        },
        {
            "name": "keerthi",
            "transaction_type": "buy",
            "asset_type": "EDT",
            "asset_value": 190.45,
            "quantity": 10000
        }
    ]

    queue = Queue(7)

    for trader in traders:
        print(trader)
        t = Trader(**trader)
        queue.enqueue(t)
        print(queue.size)

    print("-----------------")

    for item in queue:
        print(item)
        print(queue.size)





