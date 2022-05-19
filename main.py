from tradingview_ta import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import binanceApi
from binanceApi import wallet

#macd özellikleri -70 in altında olmaları ve aralarındaki farkın 10 dan az olması
#rsi özellikleri 35 in altında olması
#stokastik rsi özelllikleri 20 nin altında olması

"""
INTERVAL_5_MINUTES
INTERVAL_15_MINUTES
INTERVAL_30_MINUTES
INTERVAL_1_HOUR
INTERVAL_4_HOUR
INTERVAL_1_DAY
INTERVAL_1_WEEK
"""

def coins(coinname,newTime):
    #coinin verileri için tradingviewa erişildi

    coin = TA_Handler(
    symbol=coinname,
    exchange="BINANCE",
    screener="crypto",
    interval=newTime
    )

    #verileri çektik
    data1 = coin.get_analysis().indicators
    #print(data1)

    signal = coin.get_analysis().moving_averages
    
    #coinin indikatör değerleri
    rsi_degeri = data1["RSI"]
    stok_degeri = data1["Stoch.RSI.K"]
    macd_degeri1 = data1["MACD.macd"]
    macd_degeri2 = data1["MACD.signal"]
    high = data1["high"]
    low = data1["low"]

    rsi = False
    stokastik = False
    macd = False
    order_status = False

    print("-"*15)
    print("###",coinname,"###")
    print("RSI degeri: ",rsi_degeri)
    print("STOKASTIK degeri : ",stok_degeri)
    print("MACD degerleri : ",macd_degeri1,macd_degeri2)
    
    macd_diff = macd_degeri1-macd_degeri2
    
    if rsi_degeri <= 35:
        rsi = True

    if stok_degeri <= 25:
        stokastik = True

    if macd_degeri1 <= 70 and macd_degeri2 <= 70 and macd_diff <=10 and macd_diff >= -200:
        macd = True
      
    print("RSI:",rsi,"\nStokastik: ",stokastik,"\nMACD: ",macd)

    try:
        profit = (high * int(textbox1.get()))/100
        sellTime = high + profit
    except ValueError:
        print("Bos yerleri doldurun")

    stop_loss_percent =(low * 5)/100
    stop_loss = low - stop_loss_percent

    if rsi == True and stokastik == True and macd == True:
        print("SINYAL : AL") 
        order_status = True
        print("Coini şu fiyatta satabilirsiniz : ",sellTime)
        print("STOP-LOSS : ",stop_loss)
        print("-"*15)

    else:
        print("SİNYAL : BEKLEMEDE KAL!")

    print("Hareketli ortalama önerisi : ",signal["RECOMMENDATION"])
    print("-"*15)

#coins(coinname="ETHUSDT")
def process(kriptoPara):
    if order_status == True:
        choice = input("İşlem Yapılsın Mı? (y/n)")
        if choice == "y":
            print("Mevcut Bakiye : ",binanceApi.wallet())
            tutar = int(input("Ne kadarlık alım yapılsın ? "))
            if tutar >= 10:
                binanceApi.buyMarketPrice(cryptoName=kriptoPara,tutar=tutar)
            else:
                print("Tutar 10'dan küçük olamaz! ")
        if choice == "n":
            print("Process has been cancelled!")
#### UYGULAMA ARAYÜZ BÖLÜMÜ ####

window = Tk()
window.title('Cyrpto Currency Signal Bot')
window.geometry("400x400")
window.resizable(width=False, height=False)

btcButton = Button(window)
ethButton = Button(window)
solButton = Button(window)
xrpButton = Button(window)
xmrButton = Button(window)
walletButton = Button(window)

times = ["5 DAKİKA","15 DAKİKA","30 DAKİKA","1 SAAT","4 SAAT","1 GÜN","1 HAFTA"]

chooseTime = ttk.Combobox(window,values=times)
chooseTime.set("Bir zaman aralığı seçin!")

def saatsec(buttonCoinName):

    if chooseTime.get() == "5 DAKİKA":
        print("INTERVAL_5_MINUTES")
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_5_MINUTES)
    if chooseTime.get() == "15 DAKİKA":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_15_MINUTES)
        print("15 DAKİKA")
    if chooseTime.get() == "30 DAKİKA":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_30_MINUTES)
        print("30 DAKİKA")
    if chooseTime.get() == "1 SAAT":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_1_HOUR)
        print("1 SAAT")
    if chooseTime.get() == "4 SAAT":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_4_HOURS)
        print("4 SAAT")
    if chooseTime.get() == "1 GÜN":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_1_DAY)
        print("1 GÜN")
    if chooseTime.get() == "1 HAFTA":
        coins(coinname=buttonCoinName, 
            newTime=Interval.INTERVAL_1_WEEK)
        print("1 HAFTA")
    else:
        print("Zaman Seçili Değil!")

assetName = binanceApi.client.get_asset_balance("TRY")["asset"]
assetValue = binanceApi.client.get_asset_balance("TRY")["free"]

def showWalletBalance():
    messagebox.showinfo(title="Cüzdan Bakiyesi (Wallet Balance)",
                        message=[assetName,assetValue])

textbox1 = Entry(window
            )

label1 = Label(window,
                text="Kar Alınacak Yüzde Oranı (%)")

label1.pack()
textbox1.pack()
chooseTime.pack(padx=10,
                pady=10)

#BUTONLAR
btcButton.config(text="BITCOIN",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="BTCTRY"),int(textbox1.get())]
                )

btcButton.place(x=40,
                y=100)

ethButton.config(text="ETHEREUM",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="ETHTRY"),int(textbox1.get())]
                )

ethButton.place(x=40,
                y=150)

solButton.config(text="SOLANA",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="SOLTRY"),int(textbox1.get()),binanceApi.wallet]
                )

solButton.place(x=40,
                y=200)

xrpButton.config(text="RIPLLE",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="XRPTRY"),int(textbox1.get()),binanceApi.wallet]
                )

xrpButton.place(x=40,
                y=250)

xmrButton.config(text="MONERO",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="XMRTRY"),int(textbox1.get()),binanceApi.wallet]
                )

xmrButton.place(x=40,
                y=300)

walletButton.config(text="Cüzdanı Görüntüle",
                bg="white",
                fg="black",
                command=showWalletBalance
                )

walletButton.place(x=250,
                y=350)

licence = Label(window,
                text="Owner & Creator : CAN ŞAHİN",
                font=("Arial",7))

licence.pack()
licence.place(x=10,
            y=375)
mainloop()
