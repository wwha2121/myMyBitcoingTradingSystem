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
    print(dfDelegate)
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

    print(coinData)

coinData = [['OMG', 11690.0, 11690.0, 11230.0, 11250.0, 11220.0, 11200.0, 11220.0], ['LAMB', 113.0, 113.0, 106.0, 106.0, 106.0, 106.0, 106.0], ['CRE', 24.2, 24.2, 24.2, 24.3, 24.2, 24.2, 24.1], ['MFT', 23.8, 23.8, 23.8, 23.9, 23.9, 23.9, 23.8], ['STRAX', 4435.0, 4435.0, 4660.0, 4670.0, 4670.0, 4670.0, 4665.0], ['TRX', 160.0, 160.0, 156.0, 156.0, 157.0, 157.0, 157.0], ['XTZ', 7265.0, 7265.0, 7060.0, 7065.0, 7065.0, 7065.0, 7065.0], ['ADA', 1660.0, 1660.0, 1625.0, 1625.0, 1625.0, 1630.0, 1625.0], ['TT', 22.7, 22.7, 21.9, 21.9, 21.9, 21.9, 21.9], ['BCH', 1251000.0, 1251000.0, 1199000.0, 1198500.0, 1198500.0, 1198500.0, 1198500.0], ['ARDR', 481.0, 481.0, 464.0, 464.0, 464.0, 464.0, 465.0], ['BTC', 70266000.0, 70266000.0, 69086000.0, 69089000.0, 69092000.0, 69086000.0, 69092000.0], ['EMC2', 600.0, 600.0, 579.0, 580.0, 579.0, 579.0, 579.0], ['THETA', 14110.0, 14110.0, 13710.0, 13670.0, 13710.0, 13710.0, 13710.0], ['WAVES', 45950.0, 45950.0, 47730.0, 47520.0, 47400.0, 47500.0, 47300.0], ['FLOW', 41500.0, 41500.0, 41840.0, 42030.0, 42020.0, 41980.0, 41910.0], ['BTG', 125900.0, 125900.0, 125900.0, 125900.0, 125900.0, 125900.0, 125850.0], ['SAND', 851.0, 851.0, 848.0, 848.0, 850.0, 850.0, 848.0], ['LSK', 7520.0, 7520.0, 7455.0, 7455.0, 7445.0, 7450.0, 7450.0], ['SRM', 14690.0, 14690.0, 14680.0, 14730.0, 14720.0, 14700.0, 14700.0], ['KAVA', 8000.0, 8000.0, 7940.0, 7995.0, 7965.0, 7950.0, 7920.0]]#['코인이름','맨처음데이터 즉 avg_buy_price 매수 평균','데이터1','데이터2','데이터3','데이터4','데이터5'],







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