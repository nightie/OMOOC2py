#!/user/bin/env python
#_*_coding:utf-8_*_

import time
print '-'*20
f=open('c:\shaowan\diary.txt','r')
for line in f:
    print line
f.close()
print u'你以前写了这些你还记得吗'
option=raw_input('快来写我啊T T,要继续写吗 yes/no')
while option=='yes':
    fw=open('c:\shaowan\diary.txt','a')
    fl=raw_input('请写入日志')
    save=raw_input('说吧，存不存！save or not or save and quit')
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