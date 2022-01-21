# -*- coding: utf-8 -*- 
"""
《流畅的Python》
16.4 预激协程的装饰器
"""

from functools import wraps

def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

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

coro_avg = averager()
from inspect import getgeneratorstate
print(getgeneratorstate(coro_avg))
a = coro_avg.send(10)
print(a)
