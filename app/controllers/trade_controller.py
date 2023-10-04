from ..dto.trader import Trader
from fastapi import APIRouter
from pydantic import model_serializer
from typing import List, Deque
from queue import Queue

transaction_router = APIRouter()


@transaction_router.post("/transactions", tags=["transactions"])
def register_transaction(transactions: List[Trader]):
    try:
        queue = Queue()
        traders = [trader.model_dump() for trader in transactions]
        # for transaction in transactions:
        #     queue.put(transaction)
        highest_total_asset_value = find_highest_total_asset_value_v2(traders)
        print(next(highest_total_asset_value))
        # print(next(highest_total_asset_value))
        # print(next(highest_total_asset_value))
        # print(next(highest_total_asset_value))
        # highest_total_asset_value = find_lowest_total_asset_value_v2(traders)
        return highest_total_asset_value
    except Exception as e:
        raise Exception(e)


def find_highest_total_asset_value_v1(traders: list):
    try:
        sorted_traders = sorted(traders, key=lambda d: d['asset_value']*d['quantity'], reverse=True)
        yield sorted_traders[0]
    except Exception as e:
        raise Exception(e)


def find_highest_total_asset_value_v2(traders: list):
    try:
        highest_trader = traders[0]
        current_total_asset_value = highest_trader['asset_value']*highest_trader['quantity']
        number_of_transactions = len(traders)
        for i in range(1, number_of_transactions):
            if traders[i]['asset_value'] * traders[i]['quantity'] > current_total_asset_value:
                highest_trader = traders[i]
        yield highest_trader
    except Exception as e:
        raise Exception(e)


def find_lowest_total_asset_value_v1(traders: list):
    try:
        sorted_traders = sorted(traders, key=lambda d: d['asset_value']*d['quantity'], reverse=False)
        yield sorted_traders[0]
    except Exception as e:
        raise Exception(e)


def find_lowest_total_asset_value_v2(traders: list):
    try:
        lowest_trader = traders[0]
        current_total_asset_value = lowest_trader['asset_value'] * lowest_trader['quantity']
        number_of_transactions = len(traders)
        for i in range(1, number_of_transactions):
            if traders[i]['asset_value'] * traders[i]['quantity'] < current_total_asset_value:
                lowest_trader = traders[i]
        yield lowest_trader
    except Exception as e:
        raise Exception(e)