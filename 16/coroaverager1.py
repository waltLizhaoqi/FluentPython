# -*- coding: utf-8 -*- 
from coroutil import coroutine

@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

# coro_avg = averager()
# from inspect import getgeneratorstate
# print(getgeneratorstate(coro_avg))
# a = coro_avg.send(10)
# print(a)
# b = coro_avg.send(30)
# print(b)
# c = coro_avg.send(5)
# print(c)