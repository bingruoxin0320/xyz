# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 10:21
# @Author  : cloud
# @Site    : 
# @File    : 99.py
# @Software: PyCharm

import pyperclip
import urllib.parse
from requests.adapters import HTTPAdapter
import requests
import json
import time
from styleframe import StyleFrame,Styler,utils

s = requests.Session()
# 重试次数为3
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
import  pandas  as pd
from pandas import DataFrame



def  del_fh_list(input_list):
    temp_list=[]
    for item in input_list:
        if item!='':
            temp_list.append(item)
    return temp_list


def  get_result():
    lines = pyperclip.paste().strip()
    lines=lines.replace('\r','')
    sdkurl_list,triggerid_list,adreturn_list,adsdkver_list,platform_list,platformver_list,tagid_list,pagetype_list,\
    gametype_list,biddingprice_list,istimeout_list,errormessage_list,errorcode_list,apptypeid_list,packagename_list,appqid_list,appver_list=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

    sdklog_filename="sdk_adver_log_{}.txt".format(time.strftime("%Y%m%d_%H%M%S", time.localtime()))
    with open(sdklog_filename, "a", encoding="utf-8") as f:
        f.write("triggerid" + '\t' + 'adreturn' + '\t' + 'adsdkver' + '\t' + 'platform' + '\t' + 'platformver' + '\t'
                + 'tagid' + '\t' + 'pagetype' + '\t' + 'gametype' + '\t' + 'biddingprice' + '\t'
                + 'istimeout' + '\t' + 'errormessage' + '\t' + 'errorcode' + '\t')
        f.write('\n')

    log_list=lines.split("------------------------------------------------------------------")
    for index,_ in  enumerate(log_list):
        output_list=_.split('\n')
        templist=del_fh_list(output_list)
        with open(sdklog_filename, "a",encoding="utf-8") as f:
            for value in templist:
                if  "sdknewrequest" in value or "sdkreturn"  in value or"sdkshow"  in value :
                    # triggerid_list.append(value.split(" ")[1].strip())
                    f.write (value.split(" ")[1].strip())
                    f.write("\n")
                    sdkurl_list.append(value.split(" ")[1].strip())

                elif  "rOSwHu="in value:
                    content_str =urllib.parse.unquote(value.split("rOSwHu=")[1].strip())

                    req_data = {
                        "bpStr": content_str
                    }
                    try:
                        headers = {"Authorization": "E35A5DE437EBE8119A507D74ED459DC3"}
                        json_result = (
                            s.post("http://dc.021.com/strategic-hub/dispatch/ToolWeb/journalDecode", json=req_data, headers=headers)
                                .json().get('decodeStr'))
                        res_json= json.loads(json_result)


                        triggerid_list.append(res_json.get('triggerid'))
                        adreturn_list.append(res_json.get("adreturn",'*'))
                        adsdkver_list.append(res_json.get('adsdkver'))
                        platform_list.append(res_json.get('platform'))
                        platformver_list.append(res_json.get('platformver'))
                        apptypeid_list.append(res_json.get('apptypeid'))
                        appqid_list.append(res_json.get('appqid'))
                        packagename_list.append(res_json.get('packagename'))
                        appver_list.append(res_json.get('appver'))

                        # appid_list.append(res_json.get('appid'))
                        tagid_list.append(res_json.get('tagid'))
                        pagetype_list.append(res_json.get('pagetype'))
                        gametype_list.append(res_json.get("gametype"))
                        biddingprice_list.append(res_json.get('biddingprice'))
                        istimeout_list.append(res_json.get('istimeout',''))
                        errormessage_list.append(res_json.get('errormessage',''))
                        errorcode_list.append(res_json.get('errorcode',''))


                        f.write(res_json.get('triggerid')+'\t'+res_json.get("adreturn",'*')+'\t'+res_json.get('adsdkver')+'\t'
                               +'\t'+res_json.get('platform')+'\t'+res_json.get('platformver')+'\t'+res_json.get('tagid')+'\t'
                               +'\t'+res_json.get('pagetype')+'\t'+res_json.get('gametype')+'\t'+res_json.get('biddingprice')+'\t'
                               +'\t'+res_json.get('istimeout','')+'\t'+res_json.get('errormessage','')+'\t'+res_json.get('errorcode',''))
                        f.write('\n')
                        # print (res_json.get('triggerid'),res_json.get("adreturn",'***'),res_json.get('adsdkver'),
                        #        res_json.get('platform'),res_json.get('platformver'),res_json.get('tagid'),
                        #        res_json.get('pagetype'), res_json.get('gametype'), res_json.get('biddingprice'),
                        #        res_json.get('istimeout','***'), res_json.get('errormessage','***'), res_json.get('errorcode','***')
                        #
                        #        )
                    except Exception as e:
                        print({'code': '解密失败，请检查ocelot java_authorization的配置'})

    return  {'sdkurl':sdkurl_list,'triggerid':triggerid_list,'adreturn':adreturn_list,'apptypeid':apptypeid_list,'appqid':appqid_list,'packagename':packagename_list,'appver':appver_list,
             'adsdkver':adsdkver_list,'platform':platform_list,'platformver':platformver_list,'tagid':tagid_list, \
             'pagetype':pagetype_list,'gametype':gametype_list,'biddingprice':biddingprice_list,'istimeout':istimeout_list,'errormessage':errormessage_list,'errorcode':errorcode_list}


if __name__ == '__main__':
    dic1 = get_result()
    sf=StyleFrame(dic1)
    sf.apply_column_style(cols_to_style=['sdkurl','triggerid','adreturn','apptypeid','appqid','packagename','appver','adsdkver','platform','platformver','tagid',
                                         'pagetype','gametype','biddingprice','istimeout','errormessage','errorcode'],
                          styler_obj=Styler(horizontal_alignment="center",bg_color='#E0EEE0',font='Arial',border_type='thin',font_size=12,wrap_text=False,indent=0),
                          style_header=True)

    sf.apply_column_style(cols_to_style=['adreturn','biddingprice'],styler_obj=Styler(font_color='red',bg_color='#E0EEE0',font='Arial',font_size=12,),
                          style_header=True
                          )
    ew=StyleFrame.ExcelWriter('result_{}.xlsx'.format(time.strftime("%Y%m%d_%H%M%S", time.localtime())))
    #单元格自适应
    # sf.to_excel(ew, best_fit=['triggerid','adreturn','adsdkver','platform','platformver',
    #                           'tagid','pagetype','gametype','biddingprice','istimeout','errormessage','errorcode'])
    sf.to_excel(ew)
    ew.save()

