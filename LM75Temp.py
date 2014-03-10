#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import commands
import time
from time import strftime
from time import sleep
f = open('datas.cvs', 'a')

cmd = 'i2cget -y 1 0x48 0x00 w'

def calcTemp(wert):
	vorkomma  = wert & 0xFF
	nachkomma = wert >> 15
	
	if (vorkomma & 0x80) != 0x80:
		temp = vorkomma + nachkomma * 0.5
	else:
		vorkomma = -((~vorkomma & 0xFF) + 1)
		temp = vorkomma + nachkomma * (0.5)
	now=time.localtime()
	ausgabe = time.strftime("%d.%m.%Y,%H:%M:%S",now) + ',' + str(temp)
	print 'Zeit: ' + ausgabe + '\n'
	f.write(ausgabe + '\n')
	#print 'Zeit: ' + time.strftime("%D, %T",now) + ', ' + str(temp) + ' Grad Celsius'
	#print str(temp) + ' Grad Celsius'
	
def main():
	go = True
	while go:
		try:
			status, output = commands.getstatusoutput(cmd)
			if status == 0:
				calcTemp(int(output, 16))
				sleep(60)
			else:
				print 'Fehler!'
				print output
				go = False
		except KeyboardInterrupt:
			go = False
				
if __name__ == '__main__':
	main()