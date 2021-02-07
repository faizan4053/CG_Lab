from winSize import *
from graphics import *
from drawLine import *
from drawCircle import *
from drawEllipse import *
from drawPolygon import *
from windowToViewport import *
from fillColor import *


print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xmin , xmax , ymin , ymax = map(int, input().split())
window = size(xmin , xmax , ymin , ymax)

print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input().split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)
colors=[]
for i in range(xvmax-xvmin+10):
	colors.append([])
	for j in range(yvmax-yvmin+10):
		colors[i].append('0')

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort, colors, '1' )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort, colors, '1' )
n=int(input("enter number of edges in polygon: "))
print("Enter vertices of the edges as (x, y) one by one")
vertices=[]
for i in range(n):
	vertices.append(list(map(int, input().split())))
color = input("enter boundry color: ")

drawPolygon(win, n, vertices, color, window, viewPort, colors)
fillColor=input("enter color to be filled(not same as boundry color): ")
if(fillColor.lower()==color.lower()):
	print("sorry! same color as boundry color entered.")
	exit(0)
xv1,yv1 = windowToViewportPoint(int((vertices[2][0]+vertices[0][0])/2), int((vertices[2][1]+vertices[0][1])/2), window,  viewPort)
fillColor4(win, xv1, yv1, fillColor, colors, window, viewPort, color)


print("Click on window to exit")


win.getMouse()
win.close 


