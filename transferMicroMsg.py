#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Copyleft (c) 2017 - hwade <hwade_good@163.com>
import fire
import sys
import csv

def filterContentByTalker(fileName, talkerId):
	""" 通过说话者id筛选聊天内容 """
	fp = open(fileName,"r")

	content = []
	dataline = fp.readline()
	while dataline:
		if dataline.find(talkerId) >= 0:
			dataArray = dataline.strip().split(",")
			dataLen = len(dataArray)
			try:
				i = 0
				while dataArray[i].find(talkerId) < 0 and i < dataLen:
					i = i + 1
				if i+1 < dataLen:
					c = dataArray[i+1].split('"')[1]
					if len(c) > 0 and c.find("<") < 0 and c.find("wxid") < 0 and c.find(talkerId) < 0 :
						content.append(c)
						print c.decode('gb18030')
			except:
				print i+1, len(dataArray)
				print dataArray
				sys.exit(-1)
		dataline = fp.readline()

	return content

def main(**args):

	fileName = args['msgFileName']# "message.csv"
	talkerId = args['talkerId']# "love-a-jun"
	content = filterContentByTalker(fileName, talkerId)
	fp = open(args['recFileName'], "w") # "record-17-01-01.csv"
	spamwriter = csv.writer(fp,delimiter="\n")
	spamwriter.writerow(content)
	fp.close()

if __name__ == '__main__':
	fire.Fire()
