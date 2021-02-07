from cohenSutherland import *

if __name__=="__main__":	
	# print("enter xmin, ymin, xmax, ymax for window: ", end="")
	xmin , xmax , ymin , ymax = map(int, input().split())
	window = size(xmin , xmax , ymin , ymax)

	# print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
	# print("enter xmin, ymin, xmax, ymax for viewPort: ", end="")
	xvmin , xvmax , yvmin , yvmax = map(int, input().split())
	viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

	win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

	drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
	drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

	# print("enter xmin, ymin, xmax, ymax: ", end="")
	xmin, ymin, xmax, ymax = map(int, input().split())

	vertices=[[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]]
	drawPolygon(win, 4, vertices, 'black', window, viewPort)

	# Driver Script 
	# First Line segment 
	# P11 = (5, 5), P12 = (7, 7) 
	polyVertices=[]
	# print("enter co-ordinates of vertex of polygon (x1, y1)", end=": ")
	for i in range(4):
		polyVertices.append(list(map(int, input().split())))
	# print("enter line color: ", end="")
	color=input()
	newPoints=[]
	n=4
	for i in range(n):
		cohenSutherlandClip(polyVertices[i][0], polyVertices[i][1], polyVertices[(i+1)%n][0], polyVertices[(i+1)%n][1], color, newPoints)
	print("Click on window to exit")


	win.getMouse()
	win.close 