from windowToViewport import *
from graphics import *


def drawCircleF(win, xc, yc, rc, color):

	x = 0
	y = rc

	d = 5/4 - rc

	while(x<=y):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)

		win.plotPixel(xc + y,yc + x,color)
		win.plotPixel(xc + y,yc - x,color)
		win.plotPixel(xc - y,yc + x,color)
		win.plotPixel(xc - y,yc - x,color)
		x = x + 1
		if(d<0):
			d = d + 2 * x +3
		else:
			d = d + 2 * (x-y) +5
			y = y-1

def drawCircle(win, xw, yw, rw, color, window, viewPort):
	xv,yv = windowToViewportPoint(xw,yw,window,viewPort)
	rv = windowToViewportRadius(rw,window,viewPort)
	drawCircleF(win , xv, yv, rv, color)