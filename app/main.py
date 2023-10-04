import re
from fastapi import FastAPI
# from dto.trader import Trader
from .controllers.trade_controller import transaction_router
from queue import Queue

app = FastAPI()

trade_queue = Queue(maxsize=10)

app.include_router(transaction_router)


if __name__ == "__main__":

    # trader = Trader(
    #     name="pathum",
    #     transaction_type="buy",
    #     assert_type="AZE",
    #     assert_value=56.78,
    #     quantity=20
    # )
    ...



