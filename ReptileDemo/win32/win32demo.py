#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   @file:win32demo.py
   @author:zl
   @time:2022/06/14 16:19
   @software:PyCharm
   @desc:
"""

import win32service
class StartService(object):
    hSCManager = win32service.OpenSCManager(None, None, win32service.SeDebugPrivilege)
    win32service.OpenService(hSCManager,'vncserver',win32service.SERVICE_ALL_ACCESS)
    
    
if __name__ == '__main__':
    service = StartService()
    