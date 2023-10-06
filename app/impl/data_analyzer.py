from typing import List
import itertools
import operator
from collections import Counter


def find_highest_total_asset_value_v1(traders: List):
    try:
        sorted_traders = sorted(traders, key=lambda d: d['asset_value']*d['quantity'], reverse=True)
        return sorted_traders[0]
    except Exception as e:
        raise Exception(e)


def find_highest_total_asset_value_v2(traders: List):
    try:
        highest_trader = traders[0]
        number_of_transactions = len(traders)
        for i in range(1, number_of_transactions):
            current_highest_asset_value = highest_trader['asset_value'] * highest_trader['quantity']
            if traders[i]['asset_value'] * traders[i]['quantity'] > current_highest_asset_value:
                highest_trader = traders[i]
            continue
        yield highest_trader
        # return highest_trader
    except Exception as e:
        raise Exception(e)


def find_lowest_total_asset_value_v1(traders: List):
    try:
        sorted_traders = sorted(traders, key=lambda d: d['asset_value']*d['quantity'], reverse=False)
        return sorted_traders[0]
    except Exception as e:
        raise Exception(e)


def find_lowest_total_asset_value_v2(traders: List):
    try:
        lowest_trader = traders[0]
        number_of_transactions = len(traders)
        for i in range(1, number_of_transactions):
            current_lowest_asset_value = lowest_trader['asset_value'] * lowest_trader['quantity']
            if traders[i]['asset_value'] * traders[i]['quantity'] < current_lowest_asset_value:
                lowest_trader = traders[i]
            continue
        yield lowest_trader
        # return lowest_trader
    except Exception as e:
        raise Exception(e)


def find_most_frequent_asset(traders: List):
    # groups = itertools.groupby(traders, key=lambda d: d['asset_type'])
    counter = Counter([trader['asset_type'] for trader in traders])
    yield counter.most_common(1)[0][0]


def data_analyzer(items: List):
    try:
        if not isinstance(items, List):
            raise ValueError("input should be a list")
        highest_total_asset_value = find_highest_total_asset_value_v2(items)
        lowest_total_asset_value = find_lowest_total_asset_value_v2(items)
        most_frequent_asset = find_most_frequent_asset(items)
        return dict(
            highest_total_asset_value=highest_total_asset_value,
            lowest_total_asset_value=lowest_total_asset_value,
            most_frequent_asset=most_frequent_asset
        )
    except Exception as e:
        raise Exception(e)


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
        "quantity": 100
    }
]

    highest_total_asset_value_v2 = find_highest_total_asset_value_v2(traders)
    print(highest_total_asset_value_v2)
    print(next(highest_total_asset_value_v2))
    lowest_total_trader = find_lowest_total_asset_value_v2(traders)
    print(lowest_total_trader)
    print(next(lowest_total_trader))


    print('-----------------')
    print(find_highest_total_asset_value_v1(traders))
    print(find_lowest_total_asset_value_v1(traders))
