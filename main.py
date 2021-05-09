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
import json
import re
import requests
import numpy
import talib
from slacker import Slacker

def calculateN(ticker):
    df = pyupbit.get_ohlcv(ticker = ticker,interval="day")


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
        time.sleep(0.1)
        totalMoney += df.iloc[i][1]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])+df.iloc[i][2]*pyupbit.get_current_price("KRW-"+df.iloc[i][0])


    return totalMoney






def loadAmountOfTheCoin(ticker):


    access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
    secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
    upbit = pyupbit.Upbit(access_key, secrets_key)

    myBalance = upbit.get_balances()
    time.sleep(0.1)
    df = pd.DataFrame(myBalance)
    # print(df)
    # print(ticker)
    ticker = str(ticker)
    ticker = re.sub("KRW-","", ticker)
    # print(ticker)
    time.sleep(0.1)
    print(ticker)
    # a = df.loc[df['currency'] == ticker , 'balance'].iloc[0]
    #
    amountOfTheCoin = df.loc[df['currency'] == ticker , 'balance']
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    print("ASDSADASDASDASDASDAFFFS")
    a = list(amountOfTheCoin)

    print(a[0])

    return float(a[0])

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
    dfDelegate = df['currency'].tolist()
    dfDelegate.pop(0)
    print(dfDelegate)
    num = 0
    outName = []

    coinDataName = []
    for i in coinData:
        coinDataName.append(i[0])
        print(i[0])

    for i in coinDataName:
        if i not in dfDelegate:
            print("뺴기함수에서 왔습니다 coinData not containing :")
            print(i)
            outName.append(i)
            print(type(outName))

    print(outName)
    print(coinData)
    print("zzzz")
    print(len(outName))
    print("zzzz")
    for i in coinData:
        print("aaaaaaa")
        print(i)
        print("aaaaaaaa")
        for j in range(0, len(outName)):
            print(j)

            if i[0] == outName[j]:
                i[0] ="삭제"
        num += 1

    for i in coinData[:]:
        if i[0] == "삭제":
            coinData.remove(i)
    print("kkkkk")
    print(coinData)
    print("kkkkk")
#0,1
# if i == len(coinData)-1: #1
#     coinData.pop(i)



###



def updateAndAddCoinData(lengthOfBalnceDataFrame,df):
    # print(lengthOfBalnceDataFrame)
    dfDelegate = df['currency'].tolist()
    dfDelegate.pop(0)
    # print(dfDelegate)
    num = 0
    SameName = []

    coinDataName = []
    for i in coinData:
        coinDataName.append(i[0])

    for i in dfDelegate:
        if i not in coinDataName:
            print("coinData not containing :")
            print(i)
            SameName.append(str(i))
    print(SameName)

    coinInfoAbp = []


    for i in range(0,len(SameName)):
        isin_filter = df['currency'].isin([SameName[i]])
        df_isin = float(df[isin_filter].iloc[:,3])
        print(df_isin)
        coinInfoAbp.append(df_isin)
        print("빠")

    print(coinInfoAbp)
    # for i in range(0,len(SameName)):
    #     df['avg_buy_price'] = np.select(condition)
    #     print(df)

    for j in range(0, len(SameName)):
            coinData.append([SameName[j],  coinInfoAbp[j],  coinInfoAbp[j], 3.0, 4.0, 5.0, 6.0, 7.0])




def listTrueOrNO(): # 코인이름(A~Z)로 나열하여 빠진거 혹시 없는지 확인

    dfDelegate = loadMyBalanceAsDataFrame()
    print(dfDelegate)
    df = dfDelegate.sort_values(by='currency',axis=0,ascending=True)
    print(df)


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer " + token},
                             data={"channel": channel, "text": text}
                             )
    print(response)



def coinData에있는지(coin):

    for coinOfcoinData in coinData:
        if 'KRW-'+coinOfcoinData[0] == coin:
            return True

    return False

def MACD(coin):
    import requests
    import pandas as pd
    import time
    import webbrowser

    a = 1


    url = "https://api.upbit.com/v1/candles/days"


    querystring = {"market": coin, "count": "100"}

    response = requests.request("GET", url, params=querystring)
    time.sleep(0.1)
    data = response.json()

    df = pd.DataFrame(data)


    df = df.iloc[::-1]

    df = df['trade_price']


    exp1 = df.ewm(span=12, adjust=False).mean()
    exp2 = df.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    exp3 = macd.ewm(span=9, adjust=False).mean()

    print(coin)

    print('1번쨰 수 :',  macd[0]-exp3[0] ,end= ' ')
    print('2번쨰수 MACD: ', macd[0],end = ' ')
    print('3번쨰수 Signal: ', exp3[0],end = ' ')


    test1 =  macd[0] -exp3[0]
    test2 =  macd[1]- exp3[1]

    call = '매매 필요없음'

    # print("4번쨰수 :",test2)

    #
    if test1 < 0 and test2 > 0:
        call = '매도'
        return False
        # print(coin + '매매의견: ', call)


    if test1 > 0 and test2 < 0 :
        call = '매수'
        # print(coin + '매매의견: ', call)

        return True

    # print(coin + '매매의견: ', call)

    time.sleep(0.1)



def AD(coin):

    df = pyupbit.get_ohlcv(ticker= coin,count = 200,interval="day")
    pd.set_option('display.max_row', 200)

    real = talib.AD(df.high, df.low, df.close, df.volume)
    df['ad'] = real

    temp = []
    temp.append(df['ad'].iloc[-1])
    temp.append(df['ad'].iloc[-2])

    if max(temp) == temp[0]:
        print("AD반응 ok")
        return True



def twentyDaysExpect넘었다():
    return True

def 이동평균선대순환():
    return True

def RsI지수(coin):
    df = pyupbit.get_ohlcv(ticker=coin, count=200, interval="day")

    real = talib.RSI(df.close, timeperiod=14)
    # print(":asdasdasdasdasdasdasdasdqweqwe")
    # print(real)
    print(coin)
    print(real[-1])
    if real[-1] > 50:

        print("리얼반응 Ok")
        return True



def 진입():



    for coin in coinList:
        start_time = timeit.default_timer()  # 시작 시간 체크


        if not coinData에있는지(coin) and MACD(coin):
            access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
            secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
            upbitBuy = pyupbit.Upbit(access_key, secrets_key)
            upbitBuy.buy_market_order(coin, totalMoney() * 0.04)



            myToken = "xoxb-2027211587383-2035455281590-KFkVTgLoYPYO2w8rord2mwtr"

            post_message(myToken, "#coin",coin+ "비트코인 처음!!!!!구매!! ")

        terminate_time = timeit.default_timer()  # 종료 시간 체크

        print("진입 함수 %f초 걸렸습니다." % (terminate_time - start_time))


listTrueOrNO()


path = "/Users/jeonseongju/PycharmProjects/myMyBitcoingTradingSystem/coinData.json"

coinList = pyupbit.get_tickers(fiat="KRW")
coinData = []


while True:
    try:
        try:
            path = "/Users/jeonseongju/PycharmProjects/myMyBitcoingTradingSystem/coinData.json"
            with open(path) as json_file:
                data = json.load(json_file)
            print(data)
            coinData = data
            print(coinData)
            print("지금 가지고 있는 코인의 갯수:")
            print(len(coinData))


        except Exception as e:
            print("데이터가 없습니다!")
            print(e)
            time.sleep(0.5)



        #
        # for i in range(1,len(existedBalanceDf)):
        #     coinData.append([existedBalanceDf.iloc[i][0],existedBalanceDf.iloc[i][3],pyupbit.get_current_price('KRW-' + existedBalanceDf.iloc[i][0]),4,5,6,7,8])
        #     print(pyupbit.get_orderbook('KRW-' + existedBalanceDf.iloc[i][0]))





        while True:




            import timeit



            for num in range(0,2):
                balanceDf = loadMyBalanceAsDataFrame()

                print(balanceDf)
                print("코인의 개수는")
                print(len(coinData))

                if len(balanceDf) <= len(coinData):
                    updateAndCutCoinData(len(balanceDf), balanceDf)
                elif len(balanceDf) >= len(coinData) + 2:  # 2 = 0+ 2
                    updateAndAddCoinData(len(balanceDf), balanceDf)

                for i in range(1, 6):

                    if len(balanceDf) <= len(coinData):
                        updateAndCutCoinData(len(balanceDf), balanceDf)
                    elif len(balanceDf) >= len(coinData) + 2:  # 2 = 0+ 2
                        updateAndAddCoinData(len(balanceDf), balanceDf)

                    for j in range(0, len(coinData)):  # 코인 첫번쨰부터 끝까지

                        print(coinData)
                        ticker = 'KRW-' + coinData[j][0]  # 코인 이름
                        coinData[j][i + 2] = pyupbit.get_current_price(ticker)
                        print(ticker)
                        N = calculateN(ticker)

                        if coinData[j][i + 2] >= coinData[j][2] +N:
                            coinData[j][2] = coinData[j][i + 2]

                            if coinData[j][i + 2] < coinData[j][1] + 4.2*N:
                                access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
                                secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
                                upbitBuy = pyupbit.Upbit(access_key, secrets_key)
                                upbitBuy.buy_market_order(ticker, totalMoney() * 0.04)
                                myToken = "xoxb-2027211587383-2035455281590-KFkVTgLoYPYO2w8rord2mwtr"
                                time.sleep(0.1)
                                post_message(myToken, "#coin", ticker + "비트코인 추가 !!!!구매!! ")


                        elif  coinData[j][i+2] <=  coinData[j][2] - 2*N :
                            # coinData[j][2] = coinData[j][i]

                            access_key = "x44YC9AQxeISmQngxCTS7VnMemHRhoomVOfR7XOw"
                            secrets_key = "3uXAMditiZXguREKxNnEnhk7EWI0ubUbVB5c9xxl"
                            upbitSell = pyupbit.Upbit(access_key, secrets_key)
                            time.sleep(0.2)
                            print(ticker)
                            upbitSell.sell_market_order(ticker, loadAmountOfTheCoin(ticker))
                            time.sleep(0.2)
                            if len(balanceDf) <= len(coinData):
                                updateAndCutCoinData(len(balanceDf), balanceDf)
                            elif len(balanceDf) >= len(coinData) + 2:  # 2 = 0+ 2
                                updateAndAddCoinData(len(balanceDf), balanceDf)
                            time.sleep(0.2)
                            myToken = "xoxb-2027211587383-2035455281590-KFkVTgLoYPYO2w8rord2mwtr"

                            post_message(myToken, "#coin", ticker + "비트코인 판매!! ")

                    print(datetime.datetime.now())
                    print(coinData)

                    if len(balanceDf) <= len(coinData):
                        updateAndCutCoinData(len(balanceDf), balanceDf)
                    elif len(balanceDf) >= len(coinData) + 2:  # 2 = 0+ 2
                        updateAndAddCoinData(len(balanceDf), balanceDf)

                    path = "/Users/jeonseongju/PycharmProjects/myMyBitcoingTradingSystem/coinData.json"
                    with open(path, 'w') as outfile:
                        json.dump(coinData, outfile)

                    time.sleep(0.5)

            진입()

        myToken = "xoxb-2027211587383-2035455281590-KFkVTgLoYPYO2w8rord2mwtr"

        post_message(myToken, "#coin", "비트코인 자동매매 프로그램 오류남 ")

        time.sleep(6)


    except Exception as e:

        print(e)
        myToken = "xoxb-2027211587383-2035455281590-KFkVTgLoYPYO2w8rord2mwtr"
        time.sleep(0.1)
        post_message(myToken, "#coin", "에러남")

        time.sleep(0.5)
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
