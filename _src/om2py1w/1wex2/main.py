#!/user/bin/env python
#_*_coding:utf-8_*_

import time
print '-'*22
f=open('c:\shaowan\diary.txt','r')
for line in f:
    print line
f.close()
option=raw_input('continue to write? yes/no')
while option=='yes':
    fw=open('c:\shaowan\diary.txt','a')
    fl=raw_input('you can write here')
    save=raw_input('save or not or save and quit')
    localtime=time.asctime(time.localtime(time.time()))
    if save=='save':
        fw.write(fl+'\n')
        fw.close()
    elif save=='not':
        fw.close()
    else:
        fw.write(fl+'\n'+localtime)
        fw.close()
        break
else:fw.close()