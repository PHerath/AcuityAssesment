# AcuityAssesment

## steps to run the application in local

### 1. create virtual environment
#### ```virtualenv -p python3.10 venv```
### 3. activate the virtual env
#### ```source venv/bin/activate```
### 2. install the libraries
#### ```pip3 install -r requirements.txt```
### 3. run the application
#### ```uvicorn app.main:app --reload```


### curl request for the API
```commandline
curl --location 'http://localhost:8000/transactions' \
--header 'Content-Type: application/json' \
--data '[
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
]'
```

### sample json request for the API

```json
[
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
```

