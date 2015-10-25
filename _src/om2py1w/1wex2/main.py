#_*_coding:utf-8_*_

import time
import os

filename='diary.txt'
if not os.path.exists(filename):
    f=open(filename,'w')
else:
    f=open(filename,'r')
    for line in f:
        print line
f.close()
option=raw_input('continue to write? yes/no')
while option=='yes':
    f=open(filename,'a')
    fl=raw_input('you can write here')
    save=raw_input('save or not or save and quit')
    localtime=time.asctime(time.localtime(time.time()))
    if save=='save':
        f.write(fl+'\n')
        f.close()
    elif save=='not':
        f.close()
    else:
        f.write(fl+'\n'+localtime)
        f.close()
        break
else:f.close()