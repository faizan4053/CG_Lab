def windowToViewportPoint(x_w, y_w,window,viewPort):
	
	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	x_v = (x_w-window.xmin)*dx + viewPort.xmin
	
	y_v =  ( viewPort.ymax - (y_w - window.ymin )*dy )
	
	return (int(x_v),int(y_v))

def windowToViewportRadius(radius,window,viewPort):

	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	if( (viewPort.xmax - viewPort.xmin) < (viewPort.ymax - viewPort.ymin)):
		return int(radius * dx)
	else:
		return int(radius * dy)



def windowToViewportEllipse(rx,ry,window,viewPort):

	dx = (viewPort.xmax - viewPort.xmin )/(window.xmax - window.xmin)
	dy = (viewPort.ymax - viewPort.ymin )/(window.ymax - window.ymin)
	
	rx = dx * rx
	ry = dy * ry
	return (int(rx), int(ry))