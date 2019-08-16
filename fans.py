import time
import os
import tkinter as tk
from tkinter import * 
from tkinter import filedialog

webpage = 'https://www.facebook.com/FongshanHuangjie/'
name = 'oo.py'
dateline = 'datetime.datetime(2019, 8, 17, 1, 0, 0, 0)'
file_root = os.getcwd()

def add_line(pytxt,new):
	pytxt.write(new)
	pytxt.write('\n')

def create_txt(webpage,location,dateline):
	pytext = open(location,'a')
	#加入首頁
	add_line(pytext,'main = ' + '\'' + webpage + '\'')
	#套件
	add_line(pytext,'import datetime')
	#加入截止時間
	add_line(pytext,'dateline = ' + dateline)
	#開啟模檔新增
	kt = open('./mode/get.txt','r').read()
	lines = kt.split('\n')
	for line in lines:
		add_line(pytext,line)
	pytext.close()

def create():
	webpage = input_website.get()
	#print(webpage)
	location = os.path.join(file_root,input_file.get()+'.py')
	#print(location)
	year = str(int(input_year.get()))
	month = str(int(input_month.get()))
	day = str(int(input_day.get()))
	hour = str(int(input_hour.get()))
	minu = str(int(input_min.get()))
	sec = str(int(input_sec.get()))
	dateline = 'datetime.datetime('+ year + ','+ month + ',' + day + ',' + hour + ',' + minu + ',' + sec +',0)'
	#print(dateline)
	create_txt(webpage,location,dateline)
	pass


root = tk.Tk()
root.title('粉絲專頁抓取粉絲人數程式產生器')
root.geometry('600x400+100+100')
text_website = tk.Label(root,text = '粉絲專頁網址',font = ('Helvetica','30'))
text_website.place(x=0, y=0,width=600,height = 50)
input_website = Entry(root,font=('Helvetica','30'))
input_website.place(x=0,y=50,width=600,height = 50)
text_time = tk.Label(root,text = '抓取時間(24時制)',font = ('Helvetica','30'))
text_time.place(x=0, y=100,width=600,height = 50)
text_year = tk.Label(root,text = '年',font = ('Helvetica','30'))
text_month = tk.Label(root,text = '月',font = ('Helvetica','30'))
text_day = tk.Label(root,text = '日',font = ('Helvetica','30'))
text_hour = tk.Label(root,text = '時',font = ('Helvetica','30'))
text_min = tk.Label(root,text = '分',font = ('Helvetica','30'))
text_sec = tk.Label(root,text = '秒',font = ('Helvetica','30'))
text_year.place(x=0,y=150,width = 100, height = 50)
text_month.place(x=100,y=150,width = 100, height = 50)
text_day.place(x=200,y=150,width = 100, height = 50)
text_hour.place(x=300,y=150,width = 100, height = 50)
text_min.place(x=400,y=150,width = 100, height = 50)
text_sec.place(x=500,y=150,width = 100, height = 50)
input_year = Entry(root,font=('Helvetica','30'))
input_month = Entry(root,font=('Helvetica','30'))
input_day = Entry(root,font=('Helvetica','30'))
input_hour = Entry(root,font=('Helvetica','30'))
input_min = Entry(root,font=('Helvetica','30'))
input_sec = Entry(root,font=('Helvetica','30'))
input_year.place(x=0,y=200,width = 100, height = 50)
input_month.place(x=100,y=200,width = 100, height = 50)
input_day.place(x=200,y=200,width = 100, height = 50)
input_hour.place(x=300,y=200,width = 100, height = 50)
input_min.place(x=400,y=200,width = 100, height = 50)
input_sec.place(x=500,y=200,width = 100, height = 50)
text_file = tk.Label(root,text = '檔案儲存名稱(不需要加副檔名)',font = ('Helvetica','30'))
text_file.place(x=0,y=250,width=600,height=50)
input_file = Entry(root,font=('Helvetica','30'))
input_file.place(x=0,y=300,width=600,height=50)
btn_create = Button(root,text = '開始抓取',font = ('Helvetica','30'),command=create)
btn_create.place(x=0,y=350,width=600,height=50)
root.mainloop()
