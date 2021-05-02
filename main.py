# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





import pyupbit
import pandas as pd
import numpy as np
import statistics
ticker = "KRW-WAXP"




def calculateN(ticker):
    df = pyupbit.get_ohlcv(ticker = 'KRW-'+ticker)



    df.tail()

    df['pclose'] = df['close'].shift(1)
    df['diff1'] = abs(df['high'] - df['low'])
    df['diff2'] = abs(df['pclose'] - df['high'])
    df['diff3'] = abs(df['pclose'] - df['low'])
    df['TR'] = df[['diff1', 'diff2', 'diff3']].max(axis=1)
    # print(TRList)

    # print(len(TRList))

    import numpy as np

    data = np.array(df['TR'])  # no previous day's N
    # print(data)
    for i in range(1, len(df)):
        data[i] = (19 * data[i - 1] + df['TR'].iloc[i]) / 20

    df['N'] = data
    pd.set_option('display.max_columns', None)
    # print(df)

    return data[len(df)-1]
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
        totalMoney += df.iloc[i][1]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])+df.iloc[i][2]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])


    return totalMoney






def loadAmountOfTheCoin(ticker):


    access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
    secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
    upbit = pyupbit.Upbit(access_key, secrets_key)

    myBalance = upbit.get_balances()
    df = pd.DataFrame(myBalance)


    print(df.loc[df['currency'] == ticker , 'balance'].iloc[0])
    amountOfTheCoin = df.loc[df['currency'] == ticker , 'balance'].iloc[0]
    return amountOfTheCoin

ticker = 'WAXP'
loadAmountOfTheCoin(ticker)

access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
upbit = pyupbit.Upbit(access_key, secrets_key)

myBalance = upbit.get_balances()
df = pd.DataFrame(myBalance)

df = df['currency']

currencyList = df.values.tolist()
currencyList.pop(0)
print(currencyList)



print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for ticker in currencyList:
    nowBitcoinPrize = 0
    N = calculateN(ticker)
    print(N)
    totalMoney = totalMoney()

    ticker = 'KRW-'+ticker

    print(nowBitcoinPrize)

    if pyupbit.get_current_price(ticker) >= nowBitcoinPrize + N:
        nowBitcoinPrize = pyupbit.get_current_price(ticker)
        upbitBuy = pyupbit.Upbit(access_key, secrets_key)
        upbitBuy.buy_market_order(ticker,totalMoney*0.02)

    elif pyupbit.get_current_price(ticker) < nowBitcoinPrize - 2*N:
        nowBitcoinPrize = pyupbit.get_current_price(ticker)
        upbitSell =  pyupbit.Upbit(access_key, secrets_key)
        upbitSell.sell_market_order(ticker,loadAmountOfTheCoin(ticker))






#
# sum = 40+45+35+35+55+30+60+45+40+35+35+40+85+10+75+40+25+50+55
# print(sum)
# sum += 55*2
#
# sum = sum / 21