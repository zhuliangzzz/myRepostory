#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:ThreadingDemo.py
   @author:zl
   @time:2022/05/27 18:09
   @software:PyCharm
   @desc:
"""
import math
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

numSize = [112272535095293] * 100


def is_prim(num):
    if num < 2: return False
    if num == 2: return False
    if num % 2 == 0: return False
    sqrt = int(math.floor(math.sqrt(num)))
    for i in range(3, sqrt + 1, 2):
        if num % i == 0: return False
    return True


def Single_Thread():
    for num in numSize:
        is_prim(num)


# 多线程执行
def muti_threading():
    with ThreadPoolExecutor() as pool:
        pool.map(is_prim, numSize)

def muti_processing():
    with ProcessPoolExecutor() as pool:
        pool.map(is_prim, numSize)


if __name__ == "__main__":
    start = time.time()
    Single_Thread()
    print(time.time() - start)
    start = time.time()
    muti_threading()
    print(time.time() - start)
    start = time.time()
    muti_processing()
    print(time.time() - start)