#coding=gb2312
#��������������ڵ��Դ�������״̬ʱ�����������ǰʱ�䵽һ����־�ļ����Ա��жϵ������е�ʱ���
import datetime as dt
import time as tm
import io
#�����¼��־�ļ��������Ϊ��λ
zw_log_gap=60
#������־�ļ���
mylog='zw_computer_runlog.txt'
fh=open(mylog,'a')
fh.write("����ʱ���¼\n")
fh.close()
while 1:
	fh=open(mylog,'a')
	mynow=dt.datetime.now()
	ss=str(mynow)	#�ѵ�ǰʱ�仯Ϊ�ַ�����ʽ
	print(ss)		#�������Ļ�Ϲ�����
	fh.write(ss)	#��¼���ļ�
	fh.write('\n')	
	fh.close()		#�ر��ļ����Է�����ػ��ȵȣ�
	tm.sleep(zw_log_gap)
print("end")
