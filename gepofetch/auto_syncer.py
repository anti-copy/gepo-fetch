# Copyright (c) Anti-Copy Development Team.
# Distributed under the terms of the Modified Apache License.


from datetime import datetime
import time

import refresher

#300 second / 5min
REFRESH_INT=60

def timed_job():
    while True:
       print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       refresher.refresh()
       time.sleep(REFRESH_INT)


if __name__ == '__main__':
    timed_job()
