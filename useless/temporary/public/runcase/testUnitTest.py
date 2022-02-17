#! usr/bin/env/python
# -*- conding:utf-8 -*-


from temporary.public.runcase import yunkongqingqiu
from temporary.public.common import paramDecrype
import unittest
import xlrd
import xlwt
import json
import time
import datetime
import urllib.parse
import logging



class AdCase(unittest.TestCase):


    @classmethod
    def setUpclass(self):
        # self.ad_qq = yunkongqingqiu.AdControlRequest('BA175781266756AF605132A73A33685B')
        # params encrypt
        # self.para_encrypt = paramDecrype.Params()
        logger = logging.getLogger('sss')
        pass

    def setUp(self):
        # self.rOSwHu = {
        #     "aaid": "ffc214225ac241d3fe8500b2e70d72141",
        #     "accid": "eac0875ee2ddc8ab1mHzY11",
        #     "adsdkver": "1.4.100",
        #     "appcqid": "huawei",
        #     "appqid": "huawei1210823",
        #     "apptypeid": "19960",
        #     "appver": "1.4.0",
        #     "appverint": "010207",
        #     "appvers": "null",
        #     "appversint": "null",
        #     "basestation": "null",
        #     "city": "310000",
        #     "coordtime": "1629879556410",
        #     "device": "LIO-AL01",
        #     "devicebrand": "HUAWEI",
        #     "deviceid": "cb3e9c1e629500e0",
        #     "devicetype": "1",
        #     "ext": "{\"uFlag\":\"0\",\"advqid\":\"tcscs1\",\"uType\":\"1\",\"adFlag\":\"1\"}",
        #     "getsrctime": "0",
        #     "imei": "null",
        #     "imsi": "null",
        #     "installtime": "210824",
        #     "istourist": "1",
        #     "isyueyu": "0",
        #     "lat": "31.209135",
        #     "lng": "121.63079",
        #     "mac": "22:DA:07:83:E7:1F",
        #     "muid": "517fd9197b8b832bf3541d5a549cac05",
        #     "network": "100",
        #     "oaid": "1e5a5631-d6c8-4c1f-821e-819ca459d8a8",
        #     "obatchid": "aa9a1c6972c20c8f",
        #     "operatortype": "0",
        #     "os": "android",
        #     "osversion": "10",
        #     "packagename": "com.leshu.snake",
        #     "pixel": "784*1552",
        #     "position": "310115",
        #     "province": "310000",
        #     "screenheight": "1552",
        #     "screenwidth": "784",
        #     "srcplat": "null",
        #     "srcqid": "null",
        #     "useragent": "Dalvik/2.1.0 (Linux; U; Android 10; LIO-AL00 Build/HUAWEILIO-AL00)",
        #     "userflag": "null",
        #     "userinfo": "null",
        #     "callback": "%7B%22abcde%22%3A%7B%7D%7D"
        # }
        pass



    def testAdControl(self, i):
        # 聚合平台请求
        # get_mould = self.ad_qq.getAdvMould(self.rOSwHu['apptypeid'])
        # log_data = logging.basicConfig()
        pass