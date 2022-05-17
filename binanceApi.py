from binance.client import Client

apiKey = *
secretKey = *

client = Client(api_key=apiKey,api_secret=secretKey)

def wallet():
    balance = client.get_asset_balance("TRY")
    print("Coin Adi: ",balance["asset"],"\n",
        "Deger: ",balance["free"])


def buyMarketPrice(cryptoName):
    balance = client.get_asset_balance("TRY")
    order = client.create_order(
    symbol=cryptoName,
    side=client.SIDE_BUY,
    type=client.ORDER_TYPE_MARKET,
    quantity=10)
    print("Complated!")

def sellMarketPrice(cryptoName):
    balance = client.get_asset_balance("TRY")
    order = client.create_order(
    symbol=cryptoName,
    side=client.SIDE_SELL,
    type=client.ORDER_TYPE_MARKET,
    quantity=10)
    print("Complated!")

    

