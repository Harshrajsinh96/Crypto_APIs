# Crypto_APIs

Created REST APIs for a blockchain crypto-currency where Wallet and Transactions entities were handled using SQLAlchemy mapper in Flask framework and the data was persisted in SQLite DB. Individual account with balance which can transfer/receive value from other wallets was in a hold with the main wallet. All the transactions details were saved in Transaction entity, with appropriate error messages if user encounters bad request. Whole setup with GET/POST/DELETE request was tested on Postman.


> Change the path of DB as per your system directory in "REST_API.py" - Line 6

### 1. Create Wallet

POST /wallets

```js
{   
    "id" : "1233445665353", 
    "balance": 5,
    "coin_symbol": "FOO_COIN"
}
```

### 2. Get Wallet

GET /wallets/1233445665353

```js
{   
    "id" : "1233445665353", 
    "balance": 5,
    "coin_symbol": "FOO_COIN"
}
```

### 3. Delete Wallet

DELETE /wallets/1233445665353


### 4. Transfer Asset

POST /txns

```js
{
    "from_wallet": "2342452454", 
    "to_wallet": "1233445665353", 
    "amount": 10, 
    "time_stamp": "2018-12-13 14:46:33.942971", 
    "txn_hash": "5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4"
}
```

### 5. Get Txn

GET /txns/5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4

```js
{
    "status": "pending",
    "from_wallet": "2342452454", 
    "to_wallet": "1233445665353", 
    "amount": 10, 
    "time_stamp": "2018-12-13 14:46:33.942971", 
    "txn_hash": "5e0e3bd986d1ab40725cb9cae4c7a071eef71195074a4bcd240b37b862ace3f4"
}
```
