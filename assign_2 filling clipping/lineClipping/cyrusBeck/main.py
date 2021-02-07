from winSize import *
from graphics import *
from drawLine import *
from drawPolygon import *
from windowToViewport import *
from cyrusBeck import *

if __name__=="__main__" :
	# print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
	xmin , xmax , ymin , ymax  =  map(int, input().split())
	window  =  size(xmin , xmax , ymin , ymax)

	# print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
	xvmin , xvmax , yvmin , yvmax  =  map(int, input().split())
	viewPort  =  size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

	win  =  GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

	drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
	drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

	n = int(input())
	# print("Enter Vertices in counter clockwise direction :- ")
	vertices = list(map(int, input().split()))

	xmin  =  min(vertices[0],vertices[2],vertices[4],vertices[6])
	ymin  =  min(vertices[1],vertices[3],vertices[5],vertices[7])
	xmax  =  max(vertices[0],vertices[2],vertices[4],vertices[6])
	ymax  =  max(vertices[1],vertices[3],vertices[5],vertices[7])

	vertices = [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax]]
	drawPolygon(win, n, vertices, "black", window, viewPort)

	print("enter line end points in order as (x1, y1, x2, y2): ")
	x0, y0, x1, y1  =  map(int, input().split())

	drawLine(win, x0, y0, x1, y1, 'black', window, viewPort)

	newPair=cyrusBeck(x0, y0, x1, y1, vertices)
	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)
	# newPair=cyrusBeck(100, 100, 200, 200, vertices)
	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)
	# newPair=cyrusBeck(100, 150, 400, 500, vertices)
	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)
	# newPair=cyrusBeck(100, 300, 500, 700, vertices)
	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)
	


	# if(newPair == None):
	# 	drawLine(win, x0, y0, x1, y1, 'red', window, viewPort)
	# 	print("Click on window to exit")


	# 	win.getMouse()
	# 	win.close 
	# 	exit(0)

	# print(newPair)
	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)
	print("Click on window to exit")


	win.getMouse()
	win.close 