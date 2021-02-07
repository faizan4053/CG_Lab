from drawLine import *
from drawPolygon import *
from windowToViewport import *
from winSize import *
from graphics import *

# Defining region codes 
INSIDE = 0 #0000 
LEFT = 1 #0001 
RIGHT = 2 #0010 
BOTTOM = 4 #0100 
TOP = 8	 #1000 

# Defining xmax,ymax and xmin,ymin for rectangle 
# Since diagonal points are enough to define a rectangle 
xmax = 10.0
ymax = 8.0
xmin = 4.0
ymin = 4.0


# Function to compute region code for a point(x,y) 
def computeCode(x, y): 
	print(xmin, ymin, xmax, ymax)

	print(x, y)
	code = INSIDE 
	if x < xmin:	 # to the left of rectangle 
		code |= LEFT 
	elif x > xmax: # to the right of rectangle 
		code |= RIGHT 
	if y < ymin:	 # below the rectangle 
		code |= BOTTOM 
	elif y > ymax: # above the rectangle 
		code |= TOP 

	return code 


# Implementing Cohen-Sutherland algorithm 
# Clipping a line from P1 = (x1, y1) to P2 = (x2, y2) 
def cohenSutherlandClip(x1, y1, x2, y2, color): 

	# Compute region codes for P1, P2 
	print(x1, y1, x2, y2)
	code1 = computeCode(x1, y1) 
	code2 = computeCode(x2, y2) 
	print(code1)
	print(code2)
	accept = False

	while True: 

		# If both endpoints lie within rectangle 
		if code1 == 0 and code2 == 0: 
			accept = True
			break

		# If both endpoints are outside rectangle 
		elif (code1 & code2) != 0: 
			break

		# Some segment lies within the rectangle 
		else: 

			# Line Needs clipping 
			# At least one of the points is outside, 
			# select it 
			x = 1.0
			y = 1.0
			if code1 != 0: 
				codeout = code1 
			else: 
				codeout = code2 

			# Find intersection point 
			# using formulas y = y1 + slope * (x - x1), 
			# x = x1 + (1 / slope) * (y - y1) 
			if codeout & TOP: 
				
				# point is above the clip rectangle 
				x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1) 
				y = ymax 

			elif codeout & BOTTOM: 
				
				# point is below the clip rectangle 
				x = x1 + (x2 - x1) *(ymin - y1) / (y2 - y1) 
				y = ymin 

			elif codeout & RIGHT: 
				
				# point is to the right of the clip rectangle 
				y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1) 
				x = xmax 

			elif codeout & LEFT: 
				
				# point is to the left of the clip rectangle 
				y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1) 
				x = xmin 

			# Now intersection point x,y is found 
			# We replace point outside clipping rectangle 
			# by intersection point 
			if codeout == code1: 
				x1 = x 
				y1 = y 
				code1 = computeCode(x1,y1) 

			else: 
				x2 = x 
				y2 = y 
				code2 = computeCode(x2, y2) 

	if accept: 
		print ("Line accepted from %.2f,%.2f to %.2f,%.2f" % (x1,y1,x2,y2)) 
		drawLine(win, x1, y1, x2, y2, color, window, viewPort)

		# Here the user can add code to display the rectangle 
		# along with the accepted (portion of) lines 

	else: 
		print("Line rejected") 



xmin , xmax , ymin , ymax = map(int, input("enter xmin, ymin, xmax, ymax for window: ").split())
window = size(xmin , xmax , ymin , ymax)

# print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input("enter xmin, ymin, xmax, ymax for viewPort: ").split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

xmin, ymin, xmax, ymax = map(int, input("enter xmin, ymin, xmax, ymax: ").split())

vertices=[[xmin, ymin], [xmin, ymax], [xmax, ymax], [xmax, ymin]]
drawPolygon(win, 4, vertices, 'black', window, viewPort)

# Driver Script 
# First Line segment 
# P11 = (5, 5), P12 = (7, 7) 
x1, y1, x2, y2=map(int, input("enter co-ordinates of line ends as (x1, y1, x2, y2): ").split())
color=input("enter line color: ")
cohenSutherlandClip(x1, y1, x2, y2, color)
print("Click on window to exit")


win.getMouse()
win.close 