from binance.client import Client

apiKey = *
secretKey = *

client = Client(api_key=apiKey,api_secret=secretKey)

def wallet():
    balance = client.get_asset_balance("TRX")
    print(balance,type(balance))

def buyMarketPrice(cryptoname):
    client.order_market_buy(cryptoname)

def sellMarketPrice(cryptoname):
    client.order_market_sell(cryptoname)
    


