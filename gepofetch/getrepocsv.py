#coding:utf-8
import ssl
import urllib2
import os
import cookielib
from datetime import datetime
from diff import has_diff

DIR=os.getcwd()
DATA_CFG=os.path.join(DIR, 'repoData.csv')
print("workindg dir: %s" %DIR)
print("dataFileSave2Path: %s" %DATA_CFG)
context = ssl._create_unverified_context()
URL="https://gitee.com/anti-copy/fxcgo/raw/master/data/index.csv"


def save_from_url(url, path):
    response1=urllib2.urlopen(url,context=context)
    code = response1.getcode()
    print('code:',code)
    if code != 200:
        print("error")
    data = response1.read()
    print len(data)
    if len(data) == 0:
        print("No data loaded from url %s" % url)
        return
    if not has_diff(path, data):
        print("No data change, will not regenerate csv")
        return
    new_path_tmp = path+'.tmp' 
    with open(new_path_tmp,'w') as file:
        file.write(data)
    if os.path.exists(new_path_tmp):
        print("backup and repoint latest csv")
        os.rename(path, path+'bk'+datetime.now().strftime("%Y-%m-%d%H%M%S"))
        os.rename(new_path_tmp, path)

def test():
    save_from_url(URL, DATA_CFG)

if __name__ == '__main__':
    print("testing")
    test()
