# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.





import pyupbit
import pandas as pd
import numpy as np
import statistics
import time
import threading
import datetime



def calculateN(ticker):
    df = pyupbit.get_ohlcv(ticker = ticker)



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

    # print(df)

    for i in range(1,len(df)):
        totalMoney += df.iloc[i][1]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])+df.iloc[i][2]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])


    return totalMoney






def loadAmountOfTheCoin(ticker):


    access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
    secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
    upbit = pyupbit.Upbit(access_key, secrets_key)

    myBalance = upbit.get_balances()
    df = pd.DataFrame(myBalance)


    # print(df.loc[df['currency'] == ticker , 'balance'].iloc[0])
    amountOfTheCoin = df.loc[df['currency'] == ticker , 'balance'].iloc[0]
    return amountOfTheCoin

def loadMyBalanceAsDataFrame():
    access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
    secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
    upbit = pyupbit.Upbit(access_key, secrets_key)

    myBalance = upbit.get_balances()
    df = pd.DataFrame(myBalance)
    pd.set_option('display.max_columns', None)
    # print(df)
    return df




def updateAndCutCoinData(lengthOfBalnceDataFrame,df):

    dfDelegate =df['currency'].tolist()
    dfDelegate.pop(0)
    print(dfDelegate)
    num = 0
    outName = ''

    coinDataName = []
    for i in coinData:
        coinDataName.append(i[0])


    for i in coinDataName:
        if i not in dfDelegate :
            print("coinData not containing :")
            print(i)
            outName = i

    for i in coinData[:][0]:
        if i == outName:
            coinData.pop(num)
        num += 1

#0,1
# if i == len(coinData)-1: #1
#     coinData.pop(i)



###

def updateAndAddCoinData(lengthOfBalnceDataFrame,df):

    # print(lengthOfBalnceDataFrame)
    dfDelegate = df['currency'].tolist()
    dfDelegate.pop(0)
    #print(dfDelegate)
    num = 0
    outName = ''

    coinDataName = []
    for i in coinData:
        coinDataName.append(i[0])

    for i in dfDelegate:
        if i not in coinDataName:
            print("coinData not containing :")
            print(i)
            outName = i

    sample = df[df['currency'] == outName]
    print(sample)
    print(sample.iloc[0][3])


    for i in range(0,lengthOfBalnceDataFrame): # 0,1,2
        if i == lengthOfBalnceDataFrame-1 :# 3-1 = 2
            coinData.append(['코인이름',1,2,3,4,5,6,7])
            coinData[i-1][0] = outName
            coinData[i-1][1] = float(sample.iloc[0][3])
            coinData[i-1][2] = float(sample.iloc[0][3])





coinData = []


#while은 반복문으로 sec가 0이 되면 반복을 멈춰라
while True:
    balanceDf = loadMyBalanceAsDataFrame()

    print(balanceDf)

    for i in range(1,6):
        if len(balanceDf) == len(coinData):
            updateAndCutCoinData(len(balanceDf),balanceDf)
        elif len(balanceDf) == len(coinData)+2: # 2 = 0+ 2
            updateAndAddCoinData(len(balanceDf),balanceDf)






        for j in range(0, len(coinData)):
            ticker = 'KRW-' + coinData[j][0]
            coinData[j][i + 2] = pyupbit.get_current_price(ticker)

            N = calculateN(ticker)

            if coinData[j][i] >= coinData[j][2] + N :
                coinData[j][2] = coinData[j][i]
                if coinData[j][i] <= coinData[j][1] + 6*N:
                    upbitBuy = pyupbit.Upbit(access_key, secrets_key)
                    upbitBuy.buy_market_order(ticker, totalMoney()* 0.02)
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                    print("ㅡㅡㅡㅡㅡㅡ매수주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")


            elif coinData[j][i] < coinData[j][2] - 2*N:
                # coinData[j][2] = coinData[j][i]
                upbitSell = pyupbit.Upbit(access_key, secrets_key)
                upbitSell.sell_market_order(ticker, loadAmountOfTheCoin(ticker))
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")
                print("ㅡㅡㅡㅡㅡㅡ매도주문 체결ㅡㅡㅡㅡㅡㅡㅡㅡ")

        print(datetime.datetime.now())
        print(coinData)


        time.sleep(1)









a = pd.DataFrame(coinData)
print(a)


# def ToDo():
#     print("Timer")
#     timer = threading.Timer(10, ToDo)
#     timer.start()
#
#
# if __name__ == '__main__':
#     startTimer()


#
#
#
# print(len(coinData))
#

#

#
# print(coinData)
# a = pd.DataFrame(coinData)
# print(a)

# ticker = 'WAXP'
# loadAmountOfTheCoin(ticker)
#
# access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
# secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
# upbit = pyupbit.Upbit(access_key, secrets_key)
#
# myBalance = upbit.get_balances()
# df = pd.DataFrame(myBalance)
#
# df = df['currency']
#
# currencyList = df.values.tolist()
# currencyList.pop(0)
# print(currencyList)
#
#
#
# print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# for ticker in currencyList:
#     nowBitcoinPrize = 0
#
#     print(N)
#     totalMoney = totalMoney()
#
#     ticker = 'KRW-'+ticker
#
#     print(nowBitcoinPrize)
#

#
#




#
# sum = 40+45+35+35+55+30+60+45+40+35+35+40+85+10+75+40+25+50+55
# print(sum)
# sum += 55*2
#
# sum = sum / 21