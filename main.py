from tradingview_ta import *
from tkinter import *
from tkinter import ttk

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
    stok_degeri = data1["Stoch.K"]
    macd_degeri1 = data1["MACD.macd"]
    macd_degeri2 = data1["MACD.signal"]
    high = data1["high"]
    #low = data1["low"]

    rsi = False
    stokastik = False
    macd = False

    print("-"*15)
    print("###",coinname,"###")
    print("RSI değeri: ",rsi_degeri)
    print("STOKASTIK değeri : ",stok_degeri)
    print("MACD değerleri : ",macd_degeri1,macd_degeri2)
    
    macd_diff = macd_degeri1-macd_degeri2
    
    if rsi_degeri <= 35:
        rsi = True

        if stok_degeri <= 25:
            stokastik = True

            if macd_degeri1 <= 70 and macd_degeri2 <= 70 and macd_diff <=10 and macd_diff >= -100:
                macd = True
      
    print("RSİ:",rsi,"\nStokastik: ",stokastik,"\nMACD: ",macd)

    try:
        profit = (high * int(textbox1.get()))/100
        sellTime = high + profit
    except ValueError:
        print("Boş yerleri doldurun")

    #stop_loss_percent =(low * 5)/100
    #stop_loss = low - stop_loss_percent

    if rsi == True and stokastik == True and macd == True:
        print("SİNYAL : AL") 
        print("Coini şu fiyatta satabilirsiniz : ",sellTime)
        #print("STOP-LOSS : ",stop_loss)
        print("-"*15)

    else:
        print("SİNYAL : BEKLEMEDE KAL!")

    print("Hareketli ortalama önerisi : ",signal["RECOMMENDATION"])
    print("-"*15)

#coins(coinname="ETHUSDT")

#### UYGULAMA ARAYÜZ BÖLÜMÜ ####

window = Tk()
window.geometry("400x400")

btcButton = Button(window,text="BTCUSDT")
ethButton = Button(window)
solButton = Button(window)

times = ["5 DAKİKA","15 DAKİKA","30 DAKİKA","1 SAAT","4 SAAT","1 GÜN","1 HAFTA"]

chooseTime = ttk.Combobox(window,values=times)
chooseTime.set("Bir zaman aralığı seçin!")

def saatsec(buttonCoinName):

    if chooseTime.get() == "5 DAKİKA":
        print("INTERVAL_5_MINUTES")
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_5_MINUTES)
    if chooseTime.get() == "15 DAKİKA":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_15_MINUTES)
        print("15 DAKİKA")
    if chooseTime.get() == "30 DAKİKA":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_30_MINUTES)
        print("30 DAKİKA")
    if chooseTime.get() == "1 SAAT":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_1_HOUR)
        print("1 SAAT")
    if chooseTime.get() == "4 SAAT":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_4_HOURS)
        print("4 SAAT")
    if chooseTime.get() == "1 GÜN":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_1_DAY)
        print("1 GÜN")
    if chooseTime.get() == "1 HAFTA":
        coins(coinname=buttonCoinName, newTime=Interval.INTERVAL_1_WEEK)
        print("1 HAFTA")
    else:
        print("Zaman Seçili Değil!")
    

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
                command=lambda:[saatsec(buttonCoinName="BTCUSDT"),int(textbox1.get())]
                )

btcButton.place(x=40,
                y=100)

ethButton.config(text="ETHEREUM",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="ETHUSDT"),int(textbox1.get())]
                )

ethButton.place(x=40,
                y=150)

solButton.config(text="SOLANA",
                bg="white",
                fg="black",
                command=lambda:[saatsec(buttonCoinName="SOLUSDT"),int(textbox1.get())]
                )

solButton.place(x=40,
                y=200)

mainloop()
