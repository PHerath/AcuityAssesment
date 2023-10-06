import re

import uvicorn
from fastapi import FastAPI
# from dto.trader import Trader
from app.controllers.trade_controller import transaction_router
from queue import Queue

app = FastAPI()

trade_queue = Queue(maxsize=10)

app.include_router(transaction_router)


if __name__ == "__main__":
    uvicorn.run(app=app , port=8000)



