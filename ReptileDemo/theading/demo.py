#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:demo.py
   @author:zl
   @time:2022/09/21 17:24
   @software:PyCharm
   @desc:
"""
import os
import random
import time
from concurrent.futures import ProcessPoolExecutor


def task(n):
    print(n)
    print('%s is runing' % os.getpid())

    time.sleep(random.randint(1, 3))

    return n ** 2


if __name__ == '__main__':

    executor = ProcessPoolExecutor(max_workers=1)

    futures = []
    while True:
        future = executor.submit(task, 1)
        futures.append(future)
    # executor.shutdown(True)

    print('+++>')

    # for future in futures:
    #
    #     print(future.result())
