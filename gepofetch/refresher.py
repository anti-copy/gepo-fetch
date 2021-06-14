
import os
from csv2json import save2json
from getrepocsv import save_from_url

DIR=os.getcwd()
CSV_PATH=os.path.join(DIR, 'repoData.csv')
URL="https://gitee.com/anti-copy/fxcgo/raw/master/data/index.csv"
JSON_PATH='/root/anti-copy/ui/data.json'

def refresh():
    print("try refreshing")
    csvpath=CSV_PATH
    save_from_url(URL, csvpath)
    jsonpath=JSON_PATH
    save2json(csvpath,jsonpath)


if __name__ == '__main__':
    refresh()
