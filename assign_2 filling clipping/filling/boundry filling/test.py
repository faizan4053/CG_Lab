from winSize import *
from graphics import *
from drawLine import *
from drawCircle import *
from drawEllipse import *
from drawPolygon import *

print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xmin , xmax , ymin , ymax = map(int, input().split())
window = size(xmin , xmax , ymin , ymax)

print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input().split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )


print('''Enter 1 to Draw Line \nEnter 2 to Draw Circle \nEnter 3 to Draw Ellipse \nEnter 4 to draw polygon \nEnter 5 to Quit''')
option = int(input())

while(option != 5):
	if option == 1:
		print("Enter 2 points of line in the following order(x1,y1,x2,y2):-")
		x1,y1,x2,y2 = map(int, input().split())
		color = input("Enter color of the line:-")
		drawLine(win,x1,y1,x2,y2,color,window,viewPort)
	if option == 2:
		print("Enter center and radius of circle in the following order(xc,yc,radius):-")
		xc,yc,radius = map(int, input().split())
		color = input("Enter color of the Circle:-")
		drawCircle(win,xc,yc,radius,color,window,viewPort)
	if option == 3:
		print("Enter radii and center of Ellipse in the following order(rx,ry,xc,yc):-")
		rx,ry,xc,yc = map(int, input().split())
		color = input("Enter color of the Ellipse:-")
		drawEllipse(win,rx,ry,xc,yc,color,window,viewPort)
	if option == 4:
		n=int(input("Enter number of edges: "))
		print("Enter vertices of the edges as (x, y) one by one")
		vertices=[]
		for i in range(n):
			vertices.append(list(map(int, input().split())))
		color = input("Enter color of the Ellipse:-")
		print(n)
		drawPolygon(win, n, vertices, color, window, viewPort)

	print('''Enter 1 to Draw Line \nEnter 2 to Draw Circle \nEnter 3 to Draw Ellipse \nEnter 4 to draw polygon \nEnter 5 to Quit''')
	option = int(input())
win.plotPixel(10, 10, 'red')
print(getPixel(10, 10))
print("Click on window to exit")


win.getMouse()
win.close 