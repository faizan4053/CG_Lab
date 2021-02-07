from windowToViewport import *
from graphics import *

def drawEllipseF(win,a,b,xc,yc,color):
	x = 0
	y = b

	d1 = (b * b) - (a * a * b) + (0.25 * a * a)
	dx = 2 * b * b * x
	dy = 2 * a * a * y

	while(dx < dy):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)
		
		x = x + 1
		dx = dx + (2 * b * b)

		if(d1 < 0):
			d1 = d1 + dx +(b * b)
		else:
			y = y - 1 
			dy = dy - (2 * a * a)
			d1 = d1 + dx - dy + (b * b)
	d2 = ((b * b) * ((x + 0.5) * (x + 0.5))) + ((a * a) * ((y - 1) * (y - 1))) - (a * a * b * b)

	while(y >= 0):
		win.plotPixel(xc + x,yc + y,color)
		win.plotPixel(xc + x,yc - y,color)
		win.plotPixel(xc - x,yc + y,color)
		win.plotPixel(xc - x,yc - y,color)
		y = y -1
		dy = dy - (2 * a * a)

		if(d2 > 0):
			d2 = d2 + (a * a) - dy
		else:
			x = x + 1 
			dx = dx + (2 * b * b)
			d2 = d2 + dx - dy + (a * a)

def drawEllipse(win , a , b, xw, yw, color, window, viewPort):
	xv, yv = windowToViewportPoint(xw, yw, window, viewPort)
	av, bv = windowToViewportEllipse(a, b, window, viewPort)
	drawEllipseF(win, av, bv, xv, yv, color)