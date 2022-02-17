#! usr/bin/env/python
# -*- conding:utf-8 -*-


import logging

def ad_cloud_logger():
    lgf = logging.getLogger('AdCloud')  # 定义日志输出通道
    lgf.setLevel(logging.DEBUG)   # 定义日志等级

    position_file = logging.FileHandler(r'..\log\adlog.txt', encoding='UTF-8')
    fmt = logging.Formatter('%(asctime)s: %(message)s', datefmt='%Y:%m:%d %H:%M:%S')  # 定义日志输出格式
    position_file.setFormatter(fmt)   # 添加日志格式
    position_file.setLevel(logging.DEBUG)

    position = logging.StreamHandler()  # 定义日志输出位置
    fmt_2 = logging.Formatter('%(lineno)d-%(asctime)s:%(message)s')
    position.setFormatter(fmt_2)
    position.setLevel(logging.INFO)
    # lgf.removeHandler(position)

    lgf.addHandler(position_file)     # 组合日志收集
    lgf.addHandler(position)
    return lgf




if __name__ == '__main__':
    lgf = ad_cloud_logger()



