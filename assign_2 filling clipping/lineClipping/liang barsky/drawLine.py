from windowToViewport import *
from graphics import *

def drawLineF(win, x1, y1, x2, y2, color):
	dx = x2 - x1
	dy = y2 - y1

	dx1 = abs(dx)
	dy1 = abs(dy)
	
	px = 2 * dy1 - dx1
	py = 2 * dx1 - dy1

	if (dy1 <= dx1) :
		if (dx >= 0):
			x = x1
			y = y1
			xe =x2
		else:
			x = x2
			y = y2
			xe =x1
		

		while(x<xe):
			win.plotPixel(x, y, color)
			x = x + 1
			if(px < 0):
				px = px + 2 * dy1
			else:
				if ((dx < 0 and dy < 0) or (dx > 0 and dy >0)):
					y = y+1
				else:
					y = y - 1
				px = px + 2 * (dy1 - dx1)
			
	else:
		if ( dy >= 0):
			x = x1
			y = y1
			ye = y2
		else:
			x = x2
			y = y2
			ye = y1
		

		while(y < ye):
			win.plotPixel(x, y, color)
			y = y + 1

			if (py <= 0):
				py = py + 2 * dx1
			else:
				if ((dx < 0 and dy < 0) or (dx > 0 and dy >0)):
					x = x + 1
				else:
					x = x - 1

				py = py + 2 * (dx1 - dy1)

def drawLine(win , xw1, yw1, xw2, yw2, color, window, viewPort):
	xv1,yv1 = windowToViewportPoint(xw1, yw1, window, viewPort)
	xv2,yv2 = windowToViewportPoint(xw2, yw2, window, viewPort)
	drawLineF(win, xv1, yv1, xv2, yv2, color)
