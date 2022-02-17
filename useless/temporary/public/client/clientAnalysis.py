#! usr/bin/env/python
# -*- conding:utf-8 -*-


import json
import re
import urllib.parse
import time
from wsgiref.simple_server import make_server
import subprocess
import chardet
from temporary.public.common.paramDecrype import Params



def application(environ, start_response):
    # print(environ)
    # method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    # 获取内容长度
    try:
        content_length = environ['CONTENT_LENGTH']
    except:
        content_length = 0
    # 对内容进行编码
    content_input = environ['wsgi.input'].read(int(content_length))
    con_parse = urllib.parse.unquote(content_input.decode())
    rOSwHu = re.search('rOSwHu=(.*)', con_parse, flags=0)
    # 解密
    Params().paramWrite(rOSwHu.group(1), r'..\file\plaintext.txt')
    file_path = r'base64rebuild decrypt ..\file\plaintext.txt ..\file\ciphertext.txt'
    Params().useJar(file_path)
    # 日志记录
    look_log(path)
    start_response('200 ok', [('Content-Type', 'application/json')])
    if str(path) == '/report':
        return ['{"RQXGIr":"@0023RLjvTiKvXzpNJtl"}'.encode('utf-8')]
    else:
        return ['{"RQXGIr":"@0023RLjvTiKvXzpNJtl"}'.encode('utf-8')]



def look_log(ty):
    reFile = json.loads(Params().paramRead(r'..\file\ciphertext.txt'))
    with open(r'..\log\testlog.txt', 'a+') as f:
        # read_file()
        if str(ty) == '/sdkreturn':
            f.write('type: {}'.format(ty) + '\t')
            f.write('adreturn: {}'.format(reFile['adreturn']) + '\t')
            f.write('batch: {}'.format(reFile['batch']) + '\t')
            f.write('platformver: {}'.format(reFile['platformver']) + '\t')
            f.write('biddingprice: {}'.format(reFile['biddingprice']) + '\t')
            f.write('platform: {}'.format(reFile['platform']) + '\t')
            f.write('tagid: {}'.format(reFile['tagid']) + '\t')
            f.write('gametype:%s' % reFile['gametype'] + '\t')
            # f.write('starttime: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(reFile['starttime'][:10])))) + '\t')
            f.write('errorcode: {}'.format(reFile['errorcode']) + '\t')
            f.write('errormessage: {}'.format(reFile['errormessage']) + '\t')
            f.write('\r')
        elif str(ty) == '/sdknewrequest':
            f.write('type: {}'.format(ty) + '\t')
            f.write('batch: {}'.format(reFile['batch']) + '\t')
            # f.write('triggerid: {}'.format(reFile['triggerid']) + '\t')
            f.write('biddingprice: {}'.format(reFile['biddingprice']) + '\t')
            f.write('platform: {}'.format(reFile['platform']) + '\t')
            f.write('tagid: {}'.format(reFile['tagid']) + '\t')
            f.write('gametype:%s' % reFile['gametype'] + '\t')
            f.write('starttime: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(reFile['starttime'][:10])))) + '\t')
            f.write('\r')
        elif str(ty) == '/sdkclick':
            f.write('type: {}'.format(ty) + '\t')
            # f.write('lossreason: {}'.format(reFile['lossreason'] + '\t'))
            # f.write('biddingresult: {}'.format(reFile['biddingresult'] + '\t'))
            f.write('batch: {}'.format(reFile['batch']) + '\t')
            # f.write('triggerid: {}'.format(reFile['triggerid']) + '\t')
            f.write('biddingprice: {}'.format(reFile['biddingprice']) + '\t')
            f.write('platform: {}'.format(reFile['platform']) + '\t')
            f.write('tagid: {}'.format(reFile['tagid']) + '\t')
            f.write('pagetype: {}'.format(reFile['pagetype']) + '\t')
            f.write('ceffect: {}'.format(reFile['ceffect']) + '\t')

            # f.write('starttime: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(reFile['starttime'][:10])))) + '\t')
            f.write('\r')

        else:
            f.write('type: {}'.format(ty) + '\t')
            f.write('batch: {}'.format(reFile['batch']) + '\t')
            # f.write('triggerid: {}'.format(reFile['triggerid']) + '\t')
            f.write('biddingprice: {}'.format(reFile['biddingprice']) + '\t')
            f.write('platform: {}'.format(reFile['platform']) + '\t')
            f.write('tagid: {}'.format(reFile['tagid']) + '\t')
            f.write('pagetype: {}'.format(reFile['pagetype']) + '\t')
            # f.write('starttime: {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(reFile['starttime'][:10])))) + '\t')
            f.write('\r')


if __name__ == '__main__':
    httpd = make_server('', 6789, application)
    print("服务正在启动......")
    httpd.serve_forever()
    # look_log('/sdkreturn')