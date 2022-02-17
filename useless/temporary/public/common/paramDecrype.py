#! /usr/bin/env/python
# —*— coding:utf-8 -*-


import subprocess
import chardet
import xlrd


class Params():
    def useJar(self, arg0):
        command = r"java -jar ..\file\decrypt-tools-1.0-SNAPSHOT.jar"
        cmd = [command, arg0]
        new_cmd = ' '.join(cmd)
        stdout, stderr =subprocess.Popen(new_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE).communicate()
        # print(stdout, stderr)
        encode = chardet.detect(stdout)['encoding']
        result = stdout.decode(encode)
        return result

    def paramRead(self, path=r'..\file\ciphertext.txt'):
        with open(path, 'r+', encoding='GBK') as ct:
            cw = ct.read()
            return cw


    def paramWrite(self, rOSwHu, path=r'..\file\plaintext.txt'):
        with open(path, 'w+', encoding='GBK') as cr:
            cr.write(str(rOSwHu))


    def caseRead(self):
        casefile = xlrd.open_workbook(r'..\file\adcontrolcase.xlsx')
        sheet = casefile.sheets()[0]
        content = sheet.cell(2.1).value
        return content




if __name__ == "__main__":
    shili = Params()
    a = shili.useJar(r"..\file\ciphertext.txt ..\file\plaintext.txt")
    b = shili.paramRead()
    print(b)