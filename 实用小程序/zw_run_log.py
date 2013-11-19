#coding=gb2312
#本程序的作用是在电脑处于运行状态时，定期输出当前时间到一个日志文件，以便判断电脑运行的时间段
import datetime as dt
import time as tm
import io
#定义记录日志的间隔，以秒为单位
zw_log_gap=60
#定义日志文件名
mylog='zw_computer_runlog.txt'
fh=open(mylog,'a')
fh.write("运行时间记录\n")
fh.close()
while 1:
	fh=open(mylog,'a')
	mynow=dt.datetime.now()
	ss=str(mynow)	#把当前时间化为字符串形式
	print(ss)		#输出到屏幕上供调试
	fh.write(ss)	#记录到文件
	fh.write('\n')	
	fh.close()		#关闭文件，以防意外关机等等；
	tm.sleep(zw_log_gap)
print("end")
