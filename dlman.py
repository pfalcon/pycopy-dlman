import sys
import time
import os
import os.path

DIR = "urls"
DONE_SUBDIR = "_done_"
ERROR_SUBDIR = "_error_"
WGET = "wget --directory-prefix=dl/ --limit=1.1M --trust-server-names -c -i "
LOG_TICKS = 5 * 60

from config import *

TRANSIENT_ERRORS = (4, 7, 8)

done_full_path = DIR + "/" + DONE_SUBDIR + "/"
error_full_path = DIR + "/" + ERROR_SUBDIR + "/"

def download(f):
    path = DIR + "/" + f
    while True:
        print(WGET + path)
        rc = os.system(WGET + path)
        if rc == 0:
            break
        print("Error code: %d" % (rc // 256))
        if rc not in TRANSIENT_ERRORS:
            break
        print("Sleeping before retry...")
        sys.stdout.flush()
        time.sleep(3)
    if rc == 0:
        os.rename(path, done_full_path + f)
    else:
        os.rename(path, error_full_path + f)

def loop():
    t = time.time()
    while True:
        files = os.listdir(DIR)
        files = filter(lambda f: f[0] != "_", files)
        for f in files:
            print(f)
            download(f)
        t2 = time.time()
        if t2 < t or t2 - t > LOG_TICKS:
            t = t2
            print("Sleeping")
        time.sleep(5)

def main():
    if not os.path.isdir(done_full_path):
        os.makedirs(done_full_path)
    if not os.path.isdir(error_full_path):
        os.makedirs(error_full_path)
    loop()

main()
