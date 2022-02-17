#! usr/bin/env/python
# -*- coding:utf-8 -*-


import pytest


# 不创建类用法
# def setup_module():
#     print('setup_module')
#
#
# def teardown_module():
#     print('teardown_module')


# def setup_function():
#     print('setup_function')


def setup():
    print('setup')


def teardown():
    print('teardown')
#
#
# def test_a():
#     print('a')


# def teardown_function():
#     print('teardown_function')


# def test_b():
#     print('b')


if __name__ == '__main__':

    pytest.main(['-s'])