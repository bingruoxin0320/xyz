#! usr/bin/env/python
# -*- coding:utf-8 -*-


import requests
# from requests.auth import HTTPBasicAuth
from urllib import parse
import re


class AdControlRequest(object):
    def __init__(self, AuthCode):
        self.url = 'http://62.234.69.202/adv-cloud-console'
        self.header = {
            "OCELOT_LOGIN_USER": AuthCode,
            "OCELOT_USER_NAME": AuthCode
        }

    # 云控请求
    def adControl(self, data):
        # url = 'https://adctrlbsc-opentype.tt.cn/advertisement-cloud-new-api/data/adv.data'
        url = 'http://62.234.69.202/advertisement-cloud-new-api/data/adv.data'
        # url = 'http://172.18.18.185:8081/data/adv.data'
        # c = parse.urlencode({'rOSwHu': a})
        # b = re.search('"(.*)"', c)
        query = requests.post(url=url, data={'rOSwHu': data})
        try:
            relut = query.json()
            return relut
        except:
            relut = query.content.decode('utf-8')
            print('云控下发错误')
            return relut


    # 云控插件
    def adUnit(self, adUnitData):
        url = 'http://62.234.69.202/advertisement-cloud-new-api/plugin/gain'
        adUnitQuery = requests.post(url=url, data={'rOSwHu': adUnitData})
        try:
            adUnitRelut = adUnitQuery.json()
            return adUnitRelut
        except:
            print('插件返回错误')


    # 获取广告位名称
    def getAdvMould(self, appTypeId, os="1"):
        # url = self.url + '/advmould/getAdvMouldAll'
        # url = 'https://opendc.tt.cn/strategic-hub/dispatch/adv-cloud-console/advmould/getAdvMould'
        url = self.url + '/advmould/getAdvMould'
        data = {
            "appTypeId": appTypeId,
            "os": os,
            "pageSize": 10,
            "pageNo": 1,
        }
        advMouldQuery = requests.post(url=url, json=data, headers=self.header)
        advMould = advMouldQuery.json()
        if advMould['code'] == '1001':
            return advMould
        else:
            return {'data': []}


    # 查询人群包配置详情
    def advPlan(self, appTypeId, advMouldId, groupType, os = "1"):
        url = self.url + '/advplan/getdata'
        data = {
            "advMouldId": advMouldId,
            "appTypeId": appTypeId,
            "groupType": groupType,
            "os": os,
            "pageNo": 1,
            "pageSize": 100
        }
        advPlanQuery = requests.post(url=url, json=data, headers=self.header)
        advPlanConfig = advPlanQuery.json()
        return advPlanConfig


    # 查询计划配置详情
    def advdeploy(self, appTypeId, advMouldId, advPlanId, groupType, os="1"):
        url = self.url + '/advdeploy/getdata'
        data = {
            "groupType": groupType,
            "appTypeId": appTypeId,
            "advMouldId": advMouldId,
            "advPlanId": advPlanId,
            "os": os,
            "pageNo": 1,
            "pageSize": 10
        }
        advDevPloyQuery = requests.post(url=url, json=data, headers=self.header)
        advDevConfig = advDevPloyQuery.json()
        return advDevConfig


    # 查询AB详情
    def getABTest(self, appTypeId, advMouldId, groupType, os="1"):
        url = self.url + '/advplan/getABtest'
        data = {
            "advMouldId": advMouldId,
            "appTypeId": appTypeId,
            "groupType": groupType,
            "os": os
        }
        getABQuery = requests.post(url=url, json=data, headers=self.header)
        ABConfig = getABQuery.json()
        return ABConfig



if __name__ == '__main__':
    r = AdControlRequest('18255475750 ')
    # c = r.getAdvMould('19960')
    # a = '@012u9Oq0PMdvcpDvnHn07vrJKv9JP5cfc1rHKJnHBDCfKtGfnFNfb1NfceQvGUDvn5c0iMdvcpDvnyq076aJ7yMHBOdHbfa0PvrlFqTPBeGkX6G0PV7HbIiH3vGmG6GfEaQkceUfXvYvXOqjwtcjPMdvcpDvnqC034MSEvYvXOqjwtrSP1GmG6GSwyq4iyofBvrfKD9f9vYvXOqjwtQu3tMSP1GmG6GfBdLJc6GkX6G03tU4ny9vcpDvceAJEaCvGUDvn5UjwHMjnMA4XvTvXvUfB69fKjGkX6G03tU4ny9j9vTvXOA4PrYvGUDvn5UjwHMjxJolx1GmG6GlxyYlXvYvXOG03JMjNVq4bMglGvTvXOA4PrYvGUDvnJo4wdGmG6Gf7eUfB6UvGUDvnJglNOd4bMIHEvTvXvrJcvLmKjLJBFiJKeUvGUDvnVM4nMcHEvTvXOfEFsI1FUUfXvYvXOdH3Ho0iyGjn5AHXvTvXOvyF53VFdGkX6GHbyiSPJMSP1GmG6G0iv7HBMcfPFifcdCfKtMfXvYvXOdH3Ho0iyQu3tMvcpDvceGkX6GH3qQvcpDvxIjvxyblb5x3XvT3XvU3XvY3XOqHwHrSPVjvcojvxVcjiJ7fyUGk5UG4yVLjbyjvcojvc5jvGrjvn5dVnrqHCUGmMUGfyUG2EvYvXOxH3V7jnJQSPCMvcpDvc6GkX6GSPCMSEvTvXOA4PrYvGUDvnMIjidGmG6GlxyYlXvYvXOolxJQ0PrY4bMIHEvTvXv9fB6afc1GkX6GS3JQlNy9S3JQvcpDvceGkX6GS3JL4PyL4EvTvXvUvGUDvnrq4XvTvXv7fEa9fKdrf7FGkX6GlbLxvcpDvce9fEaif76NmEvYvXOI0PfGmG6GfcvTVeeTfKjTmKfTVBjTfF0GkX6Gl3yoHXvTvXvCfB4nHKdrmB4Gmbvaf7OGHcfCJK5dJPeCJKMc0PfUJEvYvXOAH3VNlNOzvcpDvceUfXvYvXOg0PMdvcpDvc5MJPeCJcfrkP1i07DIJbfrHGQafc5MkBDrmPJqJKFLHKqqmEvYvXOg0n5Q0iqoHXvTvXOq0BMqfPfimBj907vU07qnvGUDvn8UH3Oq4b894wMUHEvTvXvUvGUDvn87vcpDvd5AHwOgSP1GkX6GlNJiH3O7SP8AvcpDvceUvGUDvxtq0iIqHiyA0PCMvcpDvnJglELYH3Jp4EL7ln5zHEvYvXOUS3qMlXvTvXvNmK1WfBFCfGvYvXOUlNJo4bMglGvTvXv7fB6rfBFGkX6GjwOg4nMA0iFGmG6Gf7eUfK6UvGUDvxJcjnyMlnqMSP4p4XvTvXvrJBF9vGUDvxJcjnyMlx4oHwVpvcpDvcjaJXvYvXO7jnJUlb5QvcpDvnLClbUGkX6GjNOcjPMdvcpDvnLClbUGkX6G43JMjn5xHPLQvcpDvdVqlwHoS9s9kceAfX6pBbMA43DZv5FZve5AHwOgSP1DfB6ZverOB9CtBK6UveOCSPrdkQqy1y45EFrOB9CtBK6UREvYvXOCjiy9HnrqH9vTvXOA4PrYvGUDvxy7H3OolnHgvcpDvnLClbUGkX6G0i5YlbOq0iYGmG6GOB4XOBv90POcHbFMfcvMfQeMJQvMfcOq0nJdHELiOBv9OBJtOBv9fXaCJc6Ukc1QOBv9OBOKOBv90POcHbFAS9F9fGF71EF9fceMfcvMJQ1MJQ1G21=='
    # c = r.adControl(a)
    c = r.advdeploy('19960', 'aec13a4a12244e0095b19fd72a88a5f4', '134f6db9c7134da4b31590894ae6b47d', '0')
    # adv_deploy = [n for n in c['data'] if n['advOnOff'] == 1]
    # c = r.getAdvMould('19960')
    print(c)