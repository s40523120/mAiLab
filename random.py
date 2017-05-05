#hw2 random numbres

import random

import statistics as s

#輸入隨機整數模組
#輸入Statistics統計模組,設別名 s

for i in range(5):
    print(random.randrange(1,100))
#用for迴圈印5個1~100的隨機整數


l = []
def r5():
    for i in range(5):
        l.append((random.randrange(1,100)))
        #將1~100的隨機整數用for迴圈印5個後串成數列l
r5()
m = s.mean(l)
#s = statistics mean為s統計模組的算數平均數,算出l
m
#不用印出來所以不加print()
