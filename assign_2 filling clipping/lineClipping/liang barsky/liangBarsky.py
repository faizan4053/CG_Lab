from winSize import *
from graphics import *
from drawLine import *
from drawPolygon import *
from windowToViewport import *

print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xwmin , xwmax , ywmin , ywmax = map(int, input().split())
window = size(xwmin , xwmax , ywmin , ywmax)

print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input().split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

drawLine(win, 0, window.ymax, 0, window.ymin, 'blue', window,viewPort)
drawLine(win, window.xmin, 0, window.xmax, 0, 'red', window,viewPort)


print( " Enter rectangle coordinates in the following order (xmin, ymin, xmax, ymax) :-")

xmin, ymin, xmax, ymax=map(int, input().split())
vertices=[[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]]
drawPolygon(win, 4, vertices, 'black', window, viewPort)
print( "Enter line ends in the following order (x1, y1, x2, y2) :-")
x1, y1, x2, y2 = map(int, input().split())

dx=x2-x1
dy=y2-y1
p=[0, 0, 0, 0]
p[0]=-dx
p[1]=dx
p[2]=-dy
p[3]=dy
q=[0, 0, 0, 0]
q[0]=x1-xmin
q[1]=xmax-x1
q[2]=y1-ymin
q[3]=ymax-y1

for i in range(4):
	if(p[i]==0):
		print("line is parallel to one of the clipping boundary")
		if(q[i]>=0):
			if(i<2):
				if(y1<ymin):
					y1=ymin
			
				if(y2>ymax):
					y2=ymax

				print('line draw from: ', x1, y1, x2, y2)
			
				drawLine(win, x1, y1, x2, y2, 'red', window, viewPort)
			
			if(i>1):
				if(x1<xmin):
					x1=xmin
				
				if(x2>xmax):
					x2=xmax
				print('line draw from: ', x1, y1, x2, y2)
				drawLine(win, x1, y1, x2, y2, 'yellow', window, viewPort)
		else:
			print("line is rejected")
		exit(0)

t1=0
t2=1

for i in range(4):
	temp=q[i]/p[i]
	
	if(p[i]<0):
		if(t1<=temp):
			t1=temp
	else:
		if(t2>temp):
			t2=temp
if(t1<t2):
	xx1 = x1 + t1 * p[1]
	xx2 = x1 + t2 * p[1]
	yy1 = y1 + t1 * p[3]
	yy2 = y1 + t2 * p[3]
	print('line draw from: ', xx1, yy1, xx2, yy2)
	drawLine(win, xx1, yy1, xx2, yy2, 'black', window, viewPort)

print("Click on window to exit")


win.getMouse()
win.close