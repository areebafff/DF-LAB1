
#assignment1
#input:python3 backup.py "any image file name"
import time
import tarfile
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-b',type=int,default=512,help='reading blocksize')
arg=parser.parse_args()
source=open(arg.file,'rb')
tm=str(time.time())
bytes=b'x00'
content = source.read()
md5_hash = hashlib.md5()
md5_hash.update(content)

digest = md5_hash.hexdigest()
print(digest)
source.close()
