
from windowToViewport import *
def fillColor4(win, x, y, fillColor, colors, window, viewPort, boundaryColor):
	#tempx1, tempy1 = windowToViewportPoint(tempx , tempy, window,  viewPort)
	if(x<len(colors) and y<len(colors[0]) and x>=0 and y>=0):
		stack=[[x, y]]
	else:
		return
	while(len(stack)>0):
		tempx, tempy=stack[-1][0], stack[-1][1]
		stack.pop()
		if(colors[tempx][tempy] != '1' and colors[tempx][tempy] != '2' and x<len(colors) and y<len(colors[0]) and x>=0 and y>=0):
			win.plotPixel(tempx, tempy, fillColor)
			colors[tempx][tempy]='2'
			if(colors[tempx+1][tempy] != '1' and colors[tempx+1][tempy] != '2' and tempx+1<len(colors) and tempy<len(colors[0]) and tempx+1>=0 and tempy>=0):# and [tempx+1, tempy] not in stack):
				stack.append([tempx+1, tempy])
			if(colors[tempx][tempy+1] != '1' and colors[tempx][tempy+1] != '2' and tempx<len(colors) and tempy+1<len(colors[0]) and tempx>=0 and tempy+1>=0):# and [tempx, tempy+1] not in stack):
				stack.append([tempx, tempy+1])
			if(colors[tempx-1][tempy] != '1' and colors[tempx-1][tempy] != '2' and tempx-1<len(colors) and tempy<len(colors[0]) and tempx-1>=0 and tempy>=0):# and [tempx-1, tempy] not in stack):
				stack.append([tempx-1, tempy])
			if(colors[tempx][tempy-1] != '1' and colors[tempx][tempy-1] != '2' and tempx<len(colors) and tempy-1<len(colors[0]) and tempx>=0 and tempy-1>=0):# and [tempx, tempy-1] not in stack):
				stack.append([tempx, tempy-1])
			# if(colors[tempx+1][tempy+1] != boundaryColor[0] and colors[tempx+1][tempy+1] != fillColor[0]):# and [tempx+1, tempy] not in stack):
			# 	stack.append([tempx+1, tempy+1])
			# if(colors[tempx-1][tempy+1] != boundaryColor[0] and colors[tempx-1][tempy+1] != fillColor[0]):# and [tempx, tempy+1] not in stack):
			# 	stack.append([tempx-1, tempy+1])
			# if(colors[tempx-1][tempy-1] != boundaryColor[0] and colors[tempx-1][tempy-1] != fillColor[0]):# and [tempx-1, tempy] not in stack):
			# 	stack.append([tempx-1, tempy-1])
			# if(colors[tempx+1][tempy-1] != boundaryColor[0] and colors[tempx+1][tempy-1] != fillColor[0]):# and [tempx, tempy-1] not in stack):
			# 	stack.append([tempx+1, tempy-1])
