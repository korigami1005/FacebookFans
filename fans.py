import time
import os
import tkinter as tk
from tkinter import * 
from tkinter import filedialog
import codecs

webpage = 'https://www.facebook.com/FongshanHuangjie/'
name = 'oo.py'
dateline = 'datetime.datetime(2019, 8, 17, 1, 0, 0, 0)'
file_root = os.getcwd()

def add_line(pytxt,new):
	pytxt.write(new)
	pytxt.write('\n')

def create_txt(webpage,location,dateline):
	pytext = codecs.open(location,'a','utf-8')
	#加入首頁
	add_line(pytext,'main = ' + '\'' + webpage + '\'')
	#套件
	add_line(pytext,'import datetime')
	#加入截止時間
	add_line(pytext,'dateline = ' + dateline)
	#開啟模檔新增
	add_line(pytext,'')
	add_line(pytext,'from selenium import webdriver')
	add_line(pytext,'import os')
	add_line(pytext,'#import datetime')
	add_line(pytext,'import time')
	add_line(pytext,'import random as rd')
	add_line(pytext,'from selenium.webdriver.common.keys import Keys')
	add_line(pytext,'#按讚人數轉換')
	add_line(pytext,'def trans(str):')
	add_line(pytext,'    eng = str.split(\' 人說這讚\')[0]')
	add_line(pytext,'    split_num = eng.split(\',\')')
	add_line(pytext,'    num = 0')
	add_line(pytext,'    for i in range(len(split_num)):')
	add_line(pytext,'        num = num + int(split_num[i]) * (1000**(len(split_num)-i-1))')
	add_line(pytext,'    return num')
	add_line(pytext,'#取得更新時間')
	add_line(pytext,'def now():')
	add_line(pytext,'	now = datetime.datetime.now()')
	add_line(pytext,'	yy = now.year')
	add_line(pytext,'	MM = now.month')
	add_line(pytext,'	dd = now.day')
	add_line(pytext,'	hh = now.hour')
	add_line(pytext,'	mm = now.minute')
	add_line(pytext,'	ss = now.second')
	add_line(pytext,'	string1 = str(yy) + \'/\' + str(MM) + \'/\' + str(dd) + \'-\' + str(hh) + \':\' + str(mm) + \':\' + str(ss)')
	add_line(pytext,'	return string1')
	add_line(pytext,'#網頁啟動')
	add_line(pytext,'driver = webdriver.Chrome(\'./chromedriver\')')
	add_line(pytext,'driver.get(main)')
	add_line(pytext,'#確認現有資料筆數')
	add_line(pytext,'count = -1')
	add_line(pytext,'try:')
	add_line(pytext,'	graph = open(\'data.txt\',\'r\').read()')
	add_line(pytext,'	lines = graph.split(\'\\n\')')
	add_line(pytext,'	xs, ys, zs = [], [], []')
	add_line(pytext,'	for line in lines:')
	add_line(pytext,'		if len(line) > 0:')
	add_line(pytext,'			xs.append(int(x))')
	add_line(pytext,'			ys.append(int(y))')
	add_line(pytext,'			zs.append(int(z))')
	add_line(pytext,'	if len(xs) > 0:')
	add_line(pytext,'		count = xs[-1]')
	add_line(pytext,'	else:')
	add_line(pytext,'		pass')
	add_line(pytext,'except:')
	add_line(pytext,'	pass')
	add_line(pytext,'#更新網頁抓資料')
	add_line(pytext,'refrash_time = 60')
	add_line(pytext,'while datetime.datetime.now() - dateline < datetime.timedelta(seconds = 1):')
	add_line(pytext,'	try:')
	add_line(pytext,'		count = count + 1')
	add_line(pytext,'		driver.refresh()')
	add_line(pytext,'		good = driver.find_elements_by_class_name(\'_4bl9\')')
	add_line(pytext,'		k = 0')
	add_line(pytext,'		for i in range(len(good)):')
	add_line(pytext,'			if len(good[i].text.split(\' 人說這讚\')) > 1:')
	add_line(pytext,'				k = i')
	add_line(pytext,'		true_num = trans(good[k].text)')
	add_line(pytext,'		txt = open(\'date.txt\',\'a\')')
	add_line(pytext,'		txt.write(\'\\n\' + str(count) + \',\' + str(true_num) + \',\' + now())')
	add_line(pytext,'		txt.close()')
	add_line(pytext,'		print(\'update success at \' + now() + \' data is \' + str(true_num))')
	add_line(pytext,'		body = driver.find_element_by_css_selector(\'body\')')
	add_line(pytext,'		keep_time = rd.randint(1,45)')
	add_line(pytext,'		refrash_time = refrash_time - keep_time')
	add_line(pytext,'		time.sleep(keep_time)')
	add_line(pytext,'		body.send_keys(Keys.PAGE_DOWN)')
	add_line(pytext,'		time.sleep(refrash_time)')
	add_line(pytext,'		refrash_time = 60')
	add_line(pytext,'	except:')
	add_line(pytext,'		pass')
	add_line(pytext,'#關閉瀏覽器')
	add_line(pytext,'driver.quit()	')
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
text_time = tk.Label(root,text = '停止抓取時間(24時制)',font = ('Helvetica','30'))
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
btn_create = Button(root,text = '產生',font = ('Helvetica','30'),command=create)
btn_create.place(x=0,y=350,width=600,height=50)
root.mainloop()
