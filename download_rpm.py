# 没有找到正确批量下载rp包的命令，自己写了一个包列表，可以基于这个包列表批量wget包

# download_rpm.py
import requests
import re,os
from bs4 import BeautifulSoup
save_file = 'pk.txt'

if os.path.exists(save_file):
    os.remove(save_file)

url = 'http://mirrors.163.com/centos/7.4.1708/os/x86_64/Packages/'
rep = re.compile('^\w')
r1 = requests.get(url=url)
obj = BeautifulSoup(r1.text,'html.parser')
tag_a = obj.find_all(name='a',text=rep)

f = open(save_file,'a')
for i in tag_a:
    half_pk = i.text
    pk = url + half_pk + "\n"
    f.write(pk)
f.close()
