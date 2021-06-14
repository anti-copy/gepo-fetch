from gepofetch.csv2json import csv2json
import os

class TestCsv2JSON:
    def test_csv2json(self):
        data = """header1;h2;h3
sampV;v002;v003
v221;v222;v223
"""
        csvfile = "./data.csv"
        with open(csvfile,'w') as f:
            f.write(data)
        jdata = csv2json(csvfile)
        os.remove(csvfile)
        assert jdata == '[{"h2": "v002", "h3": "v003", "header1": "sampV"}, {"h2": "v222", "h3": "v223", "header1": "v221"}]'
