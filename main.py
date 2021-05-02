# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





import pyupbit
import pandas as pd
import statistics
ticker = "KRW-IOST"





bitcoinMarketConditions = pyupbit.get_ohlcv(ticker = ticker , interval= "day",count = 21)

pd.set_option('display.max_columns', None)
bitcoinMarketConditionsChart = pd.DataFrame(bitcoinMarketConditions)

bitcoinMarketConditionsChart = bitcoinMarketConditionsChart.apply(pd.to_numeric)

print(bitcoinMarketConditionsChart)

TRList = []



for i in range(0,20):
    day1TR1 = abs(bitcoinMarketConditionsChart.iloc[20-i][1]-bitcoinMarketConditionsChart.iloc[20-i][2]) #오늘의 고가와 저가 차이(TR1)
    day1TR2 = abs(bitcoinMarketConditionsChart.iloc[20-1-i][3]-bitcoinMarketConditionsChart.iloc[20-i][1]) #어제의 종가와 오늘의 고가 차이(TR2)
    day1TR3 = abs(bitcoinMarketConditionsChart.iloc[20-1-i][3]-bitcoinMarketConditionsChart.iloc[20-i][2])#어제의 종가와 오늘의 저가 차이(TR3)
    TR = max(day1TR1,day1TR2,day1TR3)

    TRList.append(TR)

print(TRList)


print(len(TRList))

sum = 0
sum += TRList[0]*2
for i in range(1,19):
    sum += TRList[i]
print(sum/20)


N = statistics.mean(TRList)
print(N)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
#
# print(day1TR1)
#
access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"


def totalMoney():

    totalMoney = 0.0


    access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
    secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
    upbit = pyupbit.Upbit(access_key, secrets_key)
    pd.set_option('display.max_columns', None)
    myBalance = upbit.get_balances()

    df = pd.DataFrame(myBalance)

    df[['balance', 'avg_buy_price']] = df[['balance', 'avg_buy_price']].apply(pd.to_numeric)

    df = df.astype({'currency': 'str'})


    upbit = pyupbit.Upbit(access_key, secrets_key)

    myBalance = upbit.get_balances()

    df = pd.DataFrame(myBalance)


    df[['balance', 'avg_buy_price','locked']] = df[['balance', 'avg_buy_price','locked']].apply(pd.to_numeric)

    df = df.astype({'currency': 'str'})



    totalMoney = df.iloc[0][1]+df.iloc[0][2]

    print(df)

    for i in range(1,len(df)):
        totalMoney += df.iloc[i][1]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])


    return totalMoney


print(totalMoney())
unit = 0.02*totalMoney()
print(unit)



# while True:
#
#
#     buyBitcoinPrize = 0
#
#     if pyupbit.get_current_price(ticker) >= buyBitcoinPrize + N:
#         buyBitcoinPrize = pyupbit.get_current_price(ticker)
#         upbitBuy = pyupbit.Upbit(access_key, secrets_key)
#         upbitBuy.buy_market_order(ticker,totalMoney()*0.02)
#
#     elif pyupbit.get_current_price(ticker) < buyBitcoinPrize - 2*N:
#         buyBitcoinPrize = pyupbit.get_current_price(ticker)




#
# sum = 40+45+35+35+55+30+60+45+40+35+35+40+85+10+75+40+25+50+55
# print(sum)
# sum += 55*2
#
# sum = sum / 21