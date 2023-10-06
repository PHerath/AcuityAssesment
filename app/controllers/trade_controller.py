from ..dto.trader import Trader
from fastapi import APIRouter
from typing import List
from app.helpers import Queue
from config import MAX_SIZE_OF_QUEUE
from app.impl.data_analyzer import data_analyzer
transaction_router = APIRouter()


@transaction_router.post("/transactions", tags=["transactions"])
def register_transaction(transactions: List[Trader]):
    try:
        queue = Queue(MAX_SIZE_OF_QUEUE)
        for transaction in transactions:
            queue.enqueue(transaction)

        traders = [trader.model_dump() for trader in queue]

        return data_analyzer(traders)
    except Exception as e:
        raise Exception(e)

    