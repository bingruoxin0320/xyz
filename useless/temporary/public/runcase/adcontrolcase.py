#! usr/bin/env/python
# -*- conding:utf-8 -*-


from temporary.public.runcase import yunkongqingqiu
from temporary.public.common import paramDecrype
from temporary.public.common import logCfg
import unittest
import xlrd
import xlwt
import json
import time
import datetime
import urllib.parse



class AdCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.lgf = logCfg.ad_cloud_logger()

        # network request
        self.adqq = yunkongqingqiu.AdControlRequest('18255475750')
        # params encrypt
        self.parajiami = paramDecrype.Params()

    def setUp(self):

        self.rOSwHu = {
            "aaid": "ffc214225ac241d3fe8500b2e70d72141",
            "accid": "eac0875ee2ddc8ab1mHzY11",
            "adsdkver": "1.4.100",
            "appcqid": "huawei",
            "appqid": "huawei1220123",
            "apptypeid": "19960",
            "appver": "1.2.3",
            "appverint": "010207",
            "appvers": "null",
            "appversint": "null",
            "basestation": "null",
            "city": "220000",
            "coordtime": "1629879556410",
            "device": "LIO-AL01",
            "devicebrand": "HUAWEI",
            "deviceid": "cb3e9c1e629500e0",
            "devicetype": "1",
            "ext": "{\"uFlag\":\"0\",\"advqid\":\"tcscs1\",\"uType\":\"1\",\"adFlag\":\"1\"}",
            "getsrctime": "0",
            "imei": "null",
            "imsi": "null",
            "installtime": "210824",
            "istourist": "1",
            "isyueyu": "0",
            "lat": "31.209135",
            "lng": "121.63079",
            "mac": "22:DA:07:83:E7:1F",
            "muid": "517fd9197b8b832bf3541d5a549cac05",
            "network": "100",
            "oaid": "1e5a5631-d6c8-4c1f-821e-819ca459d8a8",
            "obatchid": "aa9a1c6972c20c8f",
            "operatortype": "0",
            "os": "ios",
            "osversion": "10",
            "packagename": "com.leshu.snake",
            "pixel": "784*1552",
            "position": "310115",
            "province": "220000",
            "screenheight": "1552",
            "screenwidth": "784",
            "srcplat": "null",
            "srcqid": "null",
            "useragent": "Dalvik/2.1.0 (Linux; U; Android 10; LIO-AL00 Build/HUAWEILIO-AL00)",
            "userflag": "null",
            "userinfo": "null",
            "callback": "%7B%22abcde%22%3A%7B%22abcde.v%22%3A%220.6300.37%22%2C%22abcde.k%22%3A%221%22%7D%7D"
        }


    def testDistrict(self):

        # ??????????????????
        self.parajiami.paramWrite(json.dumps(self.rOSwHu))
        # ????????????
        self.parajiami.useJar(r"base64rebuild encrypt ..\file\plaintext.txt ..\file\ciphertext.txt")
        # ??????????????????
        rOSwHu = self.parajiami.paramRead()
        adLssue = self.adqq.adControl(rOSwHu)

        # ?????????
        advMould = self.adqq.getAdvMould(self.rOSwHu['apptypeid'])
        advMouldList = []
        for adv_i in advMould['data']:
            advMouldList.append(adv_i['mouldKey'])
        adLssueKye = set(adLssue['advs']['adv_position'].keys())
        # self.lgf.info(advMouldList)
        # print(adLssueKye)
        # ??????????????????????????????????????????????????? len(adLssue['advs']['adv_position'].keys) == len(advMould['data'])
        if not(adLssueKye ^ set(advMouldList)):
            # ???????????????
            for am in advMould['data']:
                # ????????????ABtest
                if adLssue['advs']['adv_position'][am['mouldKey']]['useTest'] == '-1':
                    # ????????????id
                    throngPack = self.adqq.advPlan(self.rOSwHu['apptypeid'], am['id'], '0')
                    # self.lgf.info(throngPack)
                    # ****
                    for i in range(len(throngPack['data'])):
                        # ??????????????????
                        if self.rOSwHu['appver'] in throngPack['data'][i]['personPackID']['versionNew'] or \
                                throngPack['data'][i]['personPackID']['versionNew'][0] == 'all':
                            if self.rOSwHu['srcqid'] in throngPack['data'][i]['personPackID']['groupNew'] or \
                                    throngPack['data'][i]['personPackID']['groupNew'][0] == 'all':
                                currentTime = time.strftime('%y%m%d')
                                d1 = datetime.date(int(self.rOSwHu['appqid'][-6:-4]), int(self.rOSwHu['appqid'][-4:-2]),
                                                   int(self.rOSwHu['appqid'][-2:]))
                                d2 = datetime.date(int(currentTime[0:2]), int(currentTime[2:4]), int(currentTime[4:]))
                                if (d2-d1).days <= throngPack['data'][i]['personPackID']['userTypeDay'] or \
                                        throngPack['data'][i]['personPackID']['userTypeDay'] == 0:
                                    if self.rOSwHu['city'] in throngPack['data'][i]['personPackID']['areaCodeNew'] or \
                                            throngPack['data'][i]['personPackID']['areaCodeNew'][0] == 'all':
                                        # ????????????
                                        adv_deploy = self.adqq.advdeploy(self.rOSwHu['apptypeid'], am['id'],
                                                                         throngPack['data'][i]['id'], '0')
                                        adv_deploy_list = len([x for x in adv_deploy['data'] if x['advOnOff'] == 0])
                                        adLssue_list = len(adLssue['advs']['adv_position'][am['mouldKey']]['plan'])
                                        self.lgf.debug('%s:%s' % (am['mouldKey'], adLssue['advs']['adv_position'][am['mouldKey']]))
                                        if adv_deploy_list == adLssue_list:
                                            self.lgf.info("?????????: %s,?????????: %s,?????????: %d ???" %
                                                          (am['advMouldName'], throngPack['data'][i]['personPackID']['packName'], adLssue_list))
                                            break
                                        else:
                                            self.lgf.warning("%s: %s????????????.???????????????????????????: %s" %
                                                             (am['advMouldName'], am['mouldKey'], throngPack['data'][i]['personPackID']['packName']))
                                    elif self.rOSwHu['province'] in throngPack['data'][i]['personPackID']['areaCodeNew'] or \
                                            throngPack['data'][i]['personPackID']['areaCodeNew'][0] == 'all':
                                        # ????????????
                                        adv_deploy = self.adqq.advdeploy(self.rOSwHu['apptypeid'], am['id'],
                                                                         throngPack['data'][i]['id'], '0')
                                        adv_deploy_list = len([x for x in adv_deploy['data'] if x['advOnOff'] == 0])
                                        adLssue_list = len(adLssue['advs']['adv_position'][am['mouldKey']]['plan'])
                                        if adv_deploy_list == adLssue_list:
                                            self.lgf.info("?????????: %s,?????????: %s,?????????: %d ???" %
                                                          (am['advMouldName'], throngPack['data'][i]['personPackID']['packName'], adLssue_list))
                                            break
                                        else:
                                            self.lgf.warning("%s: %s????????????.???????????????????????????: %s" %
                                                             (am['advMouldName'], am['mouldKey'], throngPack['data'][i]['personPackID']['packName']))
                    # ???????????????
                    # ??????ABtest
                else:
                    use_test = adLssue['advs']['adv_position'][am['mouldKey']]['useTest']
                    throngPack = self.adqq.advPlan(self.rOSwHu['apptypeid'], am['id'], str(use_test))
                    # self.lgf.info(throngPack)
                    for i in range(len(throngPack['data'])):
                        # ??????????????????
                        if self.rOSwHu['appver'] in throngPack['data'][i]['personPackID']['versionNew'] or \
                                throngPack['data'][i]['personPackID']['versionNew'][0] == 'all':
                            if self.rOSwHu['srcqid'] in throngPack['data'][i]['personPackID']['groupNew'] or \
                                    throngPack['data'][i]['personPackID']['groupNew'][0] == 'all':
                                currentTime = time.strftime('%y%m%d')
                                d1 = datetime.date(int(self.rOSwHu['appqid'][-6:-4]), int(self.rOSwHu['appqid'][-4:-2]),
                                                   int(self.rOSwHu['appqid'][-2:]))
                                d2 = datetime.date(int(currentTime[0:2]), int(currentTime[2:4]), int(currentTime[4:]))
                                if (d2-d1).days <= throngPack['data'][i]['personPackID']['userTypeDay'] or \
                                        throngPack['data'][i]['personPackID']['userTypeDay'] == 0:
                                    if self.rOSwHu['city'] in throngPack['data'][i]['personPackID']['areaCodeNew'] or \
                                            throngPack['data'][i]['personPackID']['areaCodeNew'][0] == 'all':
                                        # ????????????
                                        adv_deploy = self.adqq.advdeploy(self.rOSwHu['apptypeid'], am['id'],
                                                                         throngPack['data'][i]['id'], '0')
                                        adv_deploy_list = len([x for x in adv_deploy['data'] if x['advOnOff'] == 0])
                                        adLssue_list = len(adLssue['advs']['adv_position'][am['mouldKey']]['plan'])
                                        self.lgf.debug('%s:%s' % (am['mouldKey'], adLssue['advs']['adv_position'][am['mouldKey']]))
                                        if adv_deploy_list == adLssue_list:
                                            self.lgf.info("?????????: %s,?????????: %s,?????????: %d ???" %
                                                          (am['advMouldName'], throngPack['data'][i]['personPackID']['packName'], adLssue_list))
                                            break
                                        else:
                                            self.lgf.warning("%s: %s????????????.???????????????????????????: %s" %
                                                             (am['advMouldName'], am['mouldKey'], throngPack['data'][i]['personPackID']['packName']))
                                    elif self.rOSwHu['province'] in throngPack['data'][i]['personPackID']['areaCodeNew'] or \
                                            throngPack['data'][i]['personPackID']['areaCodeNew'][0] == 'all':
                                        # ????????????
                                        adv_deploy = self.adqq.advdeploy(self.rOSwHu['apptypeid'], am['id'],
                                                                         throngPack['data'][i]['id'], '0')
                                        adv_deploy_list = len([x for x in adv_deploy['data'] if x['advOnOff'] == 0])
                                        adLssue_list = len(adLssue['advs']['adv_position'][am['mouldKey']]['plan'])
                                        if adv_deploy_list == adLssue_list:
                                            self.lgf.info("?????????: %s,?????????: %s,?????????: %d ???" %
                                                          (am['advMouldName'], throngPack['data'][i]['personPackID']['packName'], adLssue_list))
                                            break
                                        else:
                                            self.lgf.warning("%s: %s????????????.???????????????????????????: %s" %
                                                             (am['advMouldName'], am['mouldKey'], throngPack['data'][i]['personPackID']['packName']))
        else:
            print('????????????????????????')
            print(adLssueKye ^ set(advMouldList))
        # ??????????????????




if __name__ == '__main__':
    # unittest.main()
    i = 0
    while i < 1:
        suite = unittest.TestSuite()
        suite.addTest(AdCase("testDistrict"))
        unittest.TextTestRunner().run(suite)
        i += 1