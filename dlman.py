import sys
import time
import os
import os.path

DIR = "urls"
DONE_SUBDIR = "_done_"
WGET = "wget --directory-prefix=dl/ --limit=1.1M --trust-server-names -c -i "
LOG_TICKS = 5 * 60

from config import *

done_full_path = DIR + "/" + DONE_SUBDIR + "/"

def download(f):
    path = DIR + "/" + f
    while True:
        print(WGET + path)
        rc = os.system(WGET + path)
        if rc == 0:
            break
        print("Error code: %d, sleeping before retry..." % (rc // 256))
        sys.stdout.flush()
        time.sleep(3)
    os.rename(path, done_full_path + f)

def loop():
    while True:
        t1 = time.time()
        files = os.listdir(DIR)
        files = filter(lambda f: f != DONE_SUBDIR, files)
        for f in files:
            print(f)
            download(f)
        t2 = time.time()
        if t2 < t1 or t2 - t1 > LOG_TICKS:
            print("Sleeping")
        time.sleep(5)

def main():
    if not os.path.isdir(done_full_path):
        os.makedirs(done_full_path)
    loop()

main()
