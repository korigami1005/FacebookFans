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
		xs.append(int(x)-787)
		ys.append(int(y))
		zs.append(str(z))
timecode = len(zs)

def animation(i):
	ax.clear()
	xdata.append(xs[i])
	ydata.append(ys[i])
	zdata.append(zs[i])
	ax.plot(xdata,ydata)
	ax.set_xlim(-5,timecode+5)
	ax.set_ylim(min(ys),max(ys))
	ax.set_xticks([])
	title =''
	title = str(zdata[-1]) + ' Number:' + str(ydata[-1])
	ax.set_title(title)

ani = FuncAnimation(fig, animation, interval = 1,frames=timecode, repeat=False)
#ani.save('sample.mp4', writer='ffmpeg',fps = 20)
plt.show()