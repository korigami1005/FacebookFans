import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import floor
import datetime

#plt.style.use('fivethirtyeight')

fig ,ax = plt.subplots()

def animation(i):
	graph = open('date.txt','r').read()
	lines = graph.split('\n')
	xs = []
	ys = []
	zs = []
	for line in lines:
		if len(line) > 0:
			x, y , z= line.split(',')
			xs.append(int(x))
			ys.append(int(y))
			zs.append(str(z))
	ax.clear()
	xlabel = 0
	ylabel_min = 0
	ylabel_max = 500
	try:
		xlabel = max(xs)
	except:
		pass
	if xlabel < 60:
		xlabel = 60
		new_ys = ys
	else:
		new_ys = ys[-61:-1]
	try:
		ylabel_min = min(new_ys)
		ylabel_max = max(new_ys)
	except:
		pass
	y_h = ylabel_max+200
	y_l = ylabel_min-200
	if y_h - y_l < 1000:
		y_h = y_l +1000
	ax.set_xlim(xlabel-65,xlabel+15)
	ax.set_ylim(y_l,y_h)
	ax.plot(xs,ys,'r',xs,ys,'b*',linewidth =1)
	for i,j in zip(xs,ys):
		ax.annotate(str(j),xy=(i-.5,j-30),fontsize=8,rotation=-90)
	last_x, last_y = xs[-1], ys[-1]
	ax.annotate('Latest update time: ' +zs [-1],xy=(xlabel-60,y_h-100),fontsize=30)
	ax.annotate('Latest number: '+ str(ys[-1]) + '('+str(ys[-1]-ys[-2])+')',xy=(xlabel-60,y_h-200),fontsize=30)

ani = FuncAnimation(fig, animation, interval = 20)

plt.yticks(fontsize=8)
plt.show()