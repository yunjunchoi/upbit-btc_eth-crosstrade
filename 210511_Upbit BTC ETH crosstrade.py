#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pyupbit
import pprint
import time
import datetime

#로그인 관련
f = open(r"C:\\Users\LG\Desktop\upbit.txt") #유니코드 인식 에러로 ""앞에 r 집어넣음
lines = f.readlines()
access = lines[0].strip() #줄바꿈 기호 삭제 위해 strip()을 추가
secret = lines[1].strip()
f.close()
upbit = pyupbit.Upbit(access, secret)

op_mode = True

while True:
    now = datetime.datetime.now()
    krw_balance = upbit.get_balance("KRW")
    
    if ((pyupbit.get_current_price("KRW-ETH")*upbit.get_balance("KRW-ETH"))-(pyupbit.get_current_price("KRW-BTC")*upbit.get_balance("KRW-BTC"))) >= 10000 and op_mode is True:
        upbit.sell_market_order("KRW-ETH", 5000)
        upbit.buy_market_order("KRW-BTC", 5000)
        print("ETH부분매도, BTC부분매수 진행")
        time.sleep(3)
        op_mode = False
    else:
        op_mode = False
    
    if ((pyupbit.get_current_price("KRW-BTC")*upbit.get_balance("KRW-BTC"))-(pyupbit.get_current_price("KRW-ETH")*upbit.get_balance("KRW-ETH"))) >= 10000 and op_mode is False:
        upbit.sell_market_order("KRW-BTC", 5000)
        upbit.buy_market_order("KRW-ETH", 5000)
        print("BTC부분매도, ETH부분매수 진행")
        time.sleep(3)
        op_mode = True
    else:
        op_mode = True
    
    print(f"현재시간: {now} -----------------------------------------------")
    print("비트코인 가격")
    print(pyupbit.get_current_price("KRW-BTC"))
    print("이더리움 가격")
    print(pyupbit.get_current_price("KRW-ETH"))
    print("비트코인 보유금액")
    print((pyupbit.get_current_price("KRW-BTC")*upbit.get_balance("KRW-BTC")))
    print("이더리움 보유금액")
    print((pyupbit.get_current_price("KRW-ETH")*upbit.get_balance("KRW-ETH")))
    print("BTC vs ETH 보유 차이금액")
    print((pyupbit.get_current_price("KRW-BTC")*upbit.get_balance("KRW-BTC"))-(pyupbit.get_current_price("KRW-ETH")*upbit.get_balance("KRW-ETH")))
    
    time.sleep(2)


# In[ ]:




