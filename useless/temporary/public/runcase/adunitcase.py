#! usr/bin/env/python
# -*- conding:utf-8 -*-


from temporary.public.runcase import yunkongqingqiu
from temporary.public.common import paramDecrype
import xlrd
import xlwt
import json
import urllib.parse
import unittest




class AdUnitRequest(unittest.TestCase):
    # def __init__(self):
        # network request
    def setUp(self):
        self.adqq = yunkongqingqiu.AdControlRequest()
        # params encrypt
        self.parajiami = paramDecrype.Params()
        self.rOSwHu2 = {
            "aaid": "7f1ae39e-9c5b-4ac6-b889-333f8a02e80b",
            "accid": "null",
            "adsdkver": "1.3.121",
            "appcqid": "Banma",
            "appqid": "Banma210907",
            "apptypeid": "004",
            "appver": "1.4.3",
            "appverint": "050208",
            "appvers": "null",
            "appversint": "null",
            "basestation": "null",
            "city": "110000",
            "coordtime": "-1",
            "device": "Redmi Note 7",
            "devicebrand": "xiaomi",
            "deviceid": "076b8cbd2d6f8d8a",
            "devicetype": "1",
            "ext": "{\"uFlag\":\"0\",\"advqid\":\"banma\",\"uType\":\"1\",\"adFlag\":\"1\"}",
            "getsrctime": "1631000364381",
            "host_version": "1.0.6",
            "imei": "null",
            "imsi": "null",
            "installtime": "210907",
            "istourist": "0",
            "isyueyu": "0",
            "lat": "0.0",
            "lng": "0.0",
            "mac": "48:FD:A3:03:85:63",
            "muid": "null",
            "network": "4",
            "oaid": "f482c132e198d463",
            "obatchid": "dd33514e72aede9e",
            "operatortype": "2",
            "os": "Android",
            "osversion": "10",
            "packagename": "com.komoxo.octopusimebigheader",
            "pixel": "1080*2217",
            "position": "110000",
            "province": "110000",
            "screenheight": "2217",
            "screenwidth": "1080",
            "srcplat": "200001",
            "srcqid": "banmatest",
            "useragent": "Dalvik/2.1.0 (Linux; U; Android 10; Redmi Note 7 MIUI/V12.0.3.0.QFGCNXM)",
            "userinfo": "null"
        }

    # 插件
    def test2(self):
        self.rOSwHu2["apptypeid"] = "004"
        self.rOSwHu2["appver"] = "1.4.9"
        self.rOSwHu2["host_version"] = "1.0.6"
        self.rOSwHu2["srcqid"] = "youhuawei"
        self.rOSwHu2["province"] = "120000"
        self.rOSwHu2["city"] = "120000"
        self.parajiami.paramWrite(json.dumps(self.rOSwHu2))
        self.parajiami.useJar(r"base64rebuild encrypt ..\file\plaintext.txt ..\file\ciphertext.txt")
        rOSwHu = self.parajiami.paramRead()
        print(rOSwHu)
        adUnitJieGuo = self.adqq.adUnit(rOSwHu)
        self.parajiami.paramWrite(adUnitJieGuo['RQXGIr'])
        self.parajiami.useJar(r"base64rebuild decrypt ..\file\plaintext.txt ..\file\ciphertext.txt")
        adReadRelut = self.parajiami.paramRead()
        # print(adReadRelut)
        return json.dumps(json.loads(adReadRelut), sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    adcol = AdUnitRequest()
    b = adcol.test2()
    print(b)
    # unittest.main()
