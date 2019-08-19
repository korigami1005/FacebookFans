import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import floor

fig ,ax = plt.subplots()
xdata, ydata, zdata = [], [], []
avg = []
timecode = 0

graph = open('data.txt','r').read()
lines = graph.split('\n')
xs = []
ys = []
zs = []
for line in lines:
	if len(line) > 0:
		x, y, z = line.split(',')
		xs.append(int(x))
		ys.append(int(y))
		zs.append(str(z))
timecode = len(zs)
y_m = max(ys)
y_mm = min(ys)

def animation(i):
	ax.clear()
	xdata.append(xs[i])
	ydata.append(ys[i])
	zdata.append(zs[i])
	ax.plot(xdata,ydata)
	ax.set_xlim(-5,timecode+5)
	ax.set_ylim(y_mm,y_m)
	ax.set_xticks([])
	title =''
	title = 'Start Time: '+str(zs[0])+ ' Number:'+str(ys[0])+'\n End Time:'+str(zdata[-1]) + ' Number:' + str(ydata[-1])
	ax.set_title(title)

ani = FuncAnimation(fig, animation, interval = 1,frames=timecode, repeat=False)
#ani.save('sample.mp4', writer='ffmpeg',fps = 40)
plt.show()
