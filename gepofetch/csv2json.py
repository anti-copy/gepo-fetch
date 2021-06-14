import os
from datetime import datetime
import csv
import json
from diff import has_diff

BYPASS_ERROR_ENTRY=True



def load(mycsv, delimiter=';'):
    result = list()
    with open(mycsv, 'r') as file:
        csv_data = csv.reader(file,dialect="excel",delimiter=delimiter)
        header = next(csv_data)
        hlen = len(header)
        print("header len %s " % hlen)
        line_no = 0
        for value in csv_data:
            line_no +=1
            entry = dict()
            id = 0
            status = check_entry(value,hlen)
            if not status:
                print("Ignore entry[%s]: %s" %(line_no, value))
                continue
            for h in header:
                v = value[id]
                entry[h] = v.decode('utf8')
                id +=1
            result.append(entry)
    return result

def check_entry(entry, elen):
    print('entry: %s', entry)
    if len(entry) != elen:
        if not BYPASS_ERROR_ENTRY:
            raise ValueError("Detect invalid entry")
        else:
            return False
    return True

def csv2json(mycsv):
    data = load(mycsv)
    return json.dumps(data, ensure_ascii=False, encoding='utf-8')

def print_csv(mycsv):
    result = load(mycsv)
    for x in result:
        print('entry=%s' % x)

def save2json(mycsv, fname):
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    data = csv2json(mycsv)
    if not has_diff(fname, data):
        print("No diff, not regenerate json")
        return
    new_path_tmp = fname+'.tmp'
    with open(new_path_tmp,'w') as file:
        file.write(data)
        print("save csv as json at %s " % new_path_tmp)
    if os.path.exists(new_path_tmp):
        print("backup and repoint latest csv")
        os.rename(fname, fname+'bk'+datetime.now().strftime("%Y-%m-%d%H%M%S"))
        print("save data as json at %s" %fname)
        os.rename(new_path_tmp, fname)
        

def backup(data, fname):
    with open(fname,'w') as f:
        f.write(data)
        print("save csv as json to path %s", fname)

if __name__ == '__main__':
     print("run testing")
     print_csv('repoData.csv')
     data=csv2json('repoData.csv')
     print("json:",data)
     save2json('repoData.csv','./data.json')
