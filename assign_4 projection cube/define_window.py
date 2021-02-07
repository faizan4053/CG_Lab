from graphics import *



class Output:
	def __init__(self,Xmin,Xmax,Ymin,Ymax):
		self.Xmin = Xmin
		self.Ymin = Ymin
		self.Xmax = Xmax
		self.Ymax = Ymax
		self.window={}
		for i in range(Xmin,Xmax+1):
			for j in range(Ymin,Ymax+1):
				self.window[(i,j)]='none'
	def changeCoords(self,Xmin,Xmax,Ymin,Ymax):
		self.Xmin = Xmin
		self.Ymin = Ymin
		self.Xmax = Xmax
		self.Ymax = Ymax
	def printInfo(self):
		print("Xmin:",self.Xmin,"Ymin:",self.Ymin,"Xmax:",self.Xmax,"Ymax:",self.Ymax)
		
device= Output(-1000, 200, -1000, 200)
viewport = Output(-1000, 200, -1000, 200)
win=None



def createWindow():
	global win
	global device
	global viewport
	win = GraphWin("Different Projections Of Cube",viewport.Xmax-viewport.Xmin,viewport.Ymax-viewport.Ymin)
	win.setBackground("azure1")
	win.setCoords(viewport.Xmin,viewport.Ymin,viewport.Xmax,viewport.Ymax)
	xlable=Text(Point(viewport.Xmax-5,-5),"x")
	xlable.draw(win)
	ylable=Text(Point(-5,viewport.Ymax-5),"y")
	ylable.draw(win)
	zlable=Text(Point(viewport.Xmin+5,viewport.Ymin+5),"z")
	zlable.draw(win)
	return win
	
#def closeWin():
#	global win
#	win.close()


	
def putPoint(x,y,color):
	global win
	#print(x,y)
	device.window[(x,y)]=color
	#print(x,y,device.window[(x,y)])
	
	#print(device.window[(x,y)])
	pt=Transform(x,y)
	#pt=Point(x,y)
	#win.plotPixel(x,y,color)
	pt.draw(win)
	pt.setFill(color)
	
	
def printCoordinates():
	global device, viewport
	print("Device Coords:")
	device.printInfo()
	print("Viewport Coords:")
	viewport.printInfo()
	
def changeViewportCoordinates():
	global viewport
	print("enter xmin,xmax,ymin,ymax for viewport")
	v_xmin,v_xmax,v_ymin,v_ymax=map(int,input().split())
	viewport.changeCoords(v_xmin,v_xmax,v_ymin,v_ymax)
	print("new viewport coordinates:")
	viewport.printInfo()
	
def changeDeviceCoordinates():
	global device
	print("enter xmin,xmax,ymin,ymax for device")
	w_xmin,w_xmax,w_ymin,w_ymax=map(int,input().split())
	device.changeCoords(w_xmin,w_xmax,w_ymin,w_ymax)
	print("new device coordinates:")
	device.printInfo()
	
def Transform(x,y):
	global device
	global viewport
	x_wmin=device.Xmin
	x_wmax=device.Xmax
	y_wmin=device.Ymin
	y_wmax=device.Ymax
	x_vmin=viewport.Xmin
	x_vmax=viewport.Xmax
	y_vmin=viewport.Ymin
	y_vmax=viewport.Ymax
	
	
	xv=x_vmin+round(((x-x_wmin)*(x_vmax-x_vmin))/(x_wmax-x_wmin))
	
	yv=y_vmin+round(((y-y_wmin)*(y_vmax-y_vmin))/(y_wmax-y_wmin))
	#yv=y_vmax-yv
	
	return Point(xv,yv)
	
def clear():
	global win
	for i in range(-200,201):
		for j in range(-200,201):
			win.plot(i,j,"black")
	win.update()
