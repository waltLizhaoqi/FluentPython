# -*- coding: utf-8 -*- 
"""
《流畅的Python》
16.5 终止协程和异常处理
"""
from coroaverager1 import averager

coro_avg = averager()
a = coro_avg.send(40)
print(a)
b = coro_avg.send(50)
print(b)
c = coro_avg.send('spam')
print(c)
