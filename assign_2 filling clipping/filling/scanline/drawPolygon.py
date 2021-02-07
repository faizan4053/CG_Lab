from windowToViewport import *
from graphics import *
from drawLine import *


def drawPolygon(win, n, vertices, color, window, viewPort, colors):
	for i in range(n-1):
		xw1=vertices[i][0]
		yw1=vertices[i][1]
		xw2=vertices[i+1][0]
		yw2=vertices[i+1][1]
		drawLine(win, xw1, yw1, xw2, yw2, color, window, viewPort, colors, '1')
	xw1=vertices[n-1][0]
	yw1=vertices[n-1][1]
	xw2=vertices[0][0]
	yw2=vertices[0][1]
	drawLine(win, xw1, yw1, xw2, yw2, color, window, viewPort, colors, '1')