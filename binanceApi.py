from binance.client import Client

apiKey = *
secretKey = *

client = Client(api_key=apiKey,api_secret=secretKey)

def wallet():
    balance = client.get_asset_balance("TRY")
    print("Varlık Adi: ",balance["asset"],"\n",
        "Deger: ",balance["free"])


def buyMarketPrice(tutar):
    balance = client.get_asset_balance("TRY")
    order = client.create_order(
    symbol="TRXTRY",
    side=client.SIDE_BUY,
    type=client.ORDER_TYPE_MARKET,
    quantity=tutar)
    print("Complated!")

def sellMarketPrice(cryptoName):
    order = client.create_order(
    symbol=cryptoName,
    side=client.SIDE_SELL,
    type=client.ORDER_TYPE_MARKET, 
    quantity=11)
    print("Complated!")

def sellLimitOrder(cryptoName,satis,sellTimeApi):
    order = client.create_order(
        symbol = cryptoName,
        side = client.SIDE_SELL,
        type = client.ORDER_TYPE_LIMIT,
        timeInForce = client.TIME_IN_FORCE_GTC,
        quantity = satis-1,
        price = sellTimeApi,  
    )

def stopLoss(cryptoName,price,stopPrice):
    order = client.create_order(
        symbol=cryptoName,
        side = client.SIDE_SELL,
        type = client.ORDER_TYPE_STOP_LOSS_LIMIT,
        timeInForce = client.TIME_IN_FORCE_GTC,
        quantity = 100,
        price = price,
        stopPrice = stopPrice
    )

