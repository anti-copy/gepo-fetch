from gepofetch.diff import has_diff
import os

class TestDiffClass:
    def test_diff(self):
        data="""header
sample
"""
        csvfile = "./data.csv"
        status = has_diff(csvfile,data)
        assert status


    def test_nodiff(self):
        data = """header
sample
"""
        csvfile = "./data.csv"
        with open(csvfile,'w') as f:
            f.write(data)
        status = has_diff(csvfile, data)
        os.remove(csvfile)
        assert not status
