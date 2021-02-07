from math import *
import numpy as np
from define_window import *
from graphics import *

color=['blue','orange','maroon','green','grey','purple','violet','brown','dark sea green','gold','tomato','magenta']

def print_line(x1,y1,x2,y2,color): 			#function to print line
	x=x1
	y=y1
	dx=x2-x1
	dy=y2-y1
	swap=0
	if dx>0:
		sign1=1
	elif dx==0:
		sign1=0
	else:
		sign1=-1
	
	if dy>0:
		sign2=1
	elif dy==0:
		sign2=0
	else:
		sign2=-1
		
	dx=abs(dx)
	dy=abs(dy)
	
	if dy>dx:
		tmp=dy
		dy=dx
		dx=dy
		swap=1
	
	d=2*dy-dx
	a=2*dy
	b=2*dy-2*dx
	
	putPoint(x,y,color)
	
	for i in range(1,dx+1):
		if d<0:
			if swap==1:
				y=y+sign2
			else:
				x=x+sign1
			d=d+a
		else:
			y=y+sign2
			x=x+sign1
			d=d+b
		putPoint(x,y,color)
		
	if dx==0:
		for i in range(y1,y2+1):
			putPoint(x,i,color)
			
			

def axisDraw():
	Xmin=-500
	Xmax=1000
	Ymin=-500
	Ymax=1000
	xaxis=print_line(0,0,Xmax,0,"black")
	yaxis=print_line(0,0,0,Ymax,"black")
	zaxis=print_line(0,0,Xmin,Ymin,"black")
	
def draw_line_in_3d(x1,y1,z1,x2,y2,z2,color,t):
	if t==1:					#for cabinet projection forsightening factor(0.3)(a=63.4)
		v=0.3
	else:
		v=1/(2**0.5)			#for cavallier projection forsightening factor(0.7)(a=45)
	
	ax=x1-(z1*v)
	ay=y1-(z1*v)
	bx=x2-(z2*v)
	by=y2-(z2*v)
	ax=(int)(ax)
	ay=(int)(ay)
	bx=(int)(bx)
	by=(int)(by)
	print_line(ax,ay,bx,by,color)

def draw(cube,typ):
	if typ==1:
		for i in range(len(color)):
			color[i]="black"
	ptr=0
	for i in range(3):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+1][0]
		y2=cube[i+1][1]
		z2=cube[i+1][2]
		h2=cube[i+1][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],0)
		ptr=ptr+1
	for i in range(4,7):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+1][0]
		y2=cube[i+1][1]
		z2=cube[i+1][2]
		h2=cube[i+1][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],0)
		ptr=ptr+1
	x1=cube[0][0]
	y1=cube[0][1]
	z1=cube[0][2]
	h1=cube[0][3]
	x2=cube[3][0]
	y2=cube[3][1]
	z2=cube[3][2]
	h2=cube[3][3]
	draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],0)
	ptr=ptr+1
	x1=cube[4][0]
	y1=cube[4][1]
	z1=cube[4][2]
	h1=cube[4][3]
	x2=cube[7][0]
	y2=cube[7][1]
	z2=cube[7][2]
	h2=cube[7][3]
	draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],0)
	ptr=ptr+1
	for i in range(4):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+4][0]
		y2=cube[i+4][1]
		z2=cube[i+4][2]
		h2=cube[i+4][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],0)
		ptr=ptr+1

def drawCabinet(cube,typ):
	if typ==1:
		for i in range(len(color)):
			color[i]="black"
	ptr=0
	for i in range(3):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+1][0]
		y2=cube[i+1][1]
		z2=cube[i+1][2]
		h2=cube[i+1][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],1)
		ptr=ptr+1
	for i in range(4,7):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+1][0]
		y2=cube[i+1][1]
		z2=cube[i+1][2]
		h2=cube[i+1][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],1)
		ptr=ptr+1
	x1=cube[0][0]
	y1=cube[0][1]
	z1=cube[0][2]
	h1=cube[0][3]
	x2=cube[3][0]
	y2=cube[3][1]
	z2=cube[3][2]
	h2=cube[3][3]
	draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],1)
	ptr=ptr+1
	x1=cube[4][0]
	y1=cube[4][1]
	z1=cube[4][2]
	h1=cube[4][3]
	x2=cube[7][0]
	y2=cube[7][1]
	z2=cube[7][2]
	h2=cube[7][3]
	draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],1)
	ptr=ptr+1
	for i in range(4):
		x1=cube[i][0]
		y1=cube[i][1]
		z1=cube[i][2]
		h1=cube[i][3]
		x2=cube[i+4][0]
		y2=cube[i+4][1]
		z2=cube[i+4][2]
		h2=cube[i+4][3]
		draw_line_in_3d(x1,y1,z1,x2,y2,z2,color[ptr],1)
		ptr=ptr+1
		
def orthogonal(typ,cube):
	for i in range(8):
		cube[i][typ]=0
	return cube
	
def arbitraryplane_orthogonal(cube,typ):
	normal=(1,1,0)				#general axonometric
	if(typ==1):
		normal=(2,2,2)			#isometric
	elif typ==2:
		normal=(-2,3,-2)		#diametric with equal  x and z
	elif typ==3:
		normal=(-1,2,3)			#triametric
	n1,n2,n3=normal[0],normal[1],normal[2]
	rfpoint=(100,100,100)
	x0,y0,z0=rfpoint[0],rfpoint[1],rfpoint[2]
	direction=(-n1,-n2,-n3)
	a,b,c=direction[0],direction[1],direction[2]
	k=np.zeros((4,4),dtype=int)
	d1=a*n1+b*n2+c*n3
	d0=n1*x0+n2*y0+n3*z0
	k[0][0]=b*n2+c*n3
	k[0][1]=-b*n1
	k[0][2]=-c*n1
	k[0][3]=d1
	k[1][0]=-a*n2
	k[1][1]=a*n1+c*n3
	k[1][2]=-c*n2
	k[1][3]=d1
	k[2][0]=-a*n3
	k[2][1]=-b*n3
	k[2][2]=a*n1+b*n2
	k[2][3]=d1
	k[3][0]=a*d0
	k[3][1]=b*d0
	k[3][2]=c*d0
	k[3][3]=1
	res=np.matmul(cube,k)

	res=res/d1

	return res
	
def perspective(cube,typ):
	cop=(120,0,0)
	a,b,c=cop[0],cop[1],cop[2]
	rfpoint=(-10,0,0)
	x0,y0,z0=rfpoint[0],rfpoint[1],rfpoint[2]
	normal=(1,0,0)
	n1,n2,n3=normal[0],normal[1],normal[2]
	k=np.zeros((4,4),dtype=int)
	d0=x0*n1+y0*n2+z0*n3
	d1=a*n1+b*n2+c*n3
	d=-(d0-d1)
	k[0][0]=n1*a+d
	k[0][1]=b*n1
	k[0][2]=c*n1
	k[0][3]=n1
	k[1][0]=a*n2
	k[1][1]=b*n2+d
	k[1][2]=c*n2
	k[1][3]=n2
	k[2][0]=a*n3
	k[2][1]=b*n3
	k[2][2]=c*n3+d
	k[2][3]=n3
	k[3][0]=-a*d0
	k[3][1]=-b*d0
	k[3][2]=-c*d0
	k[3][3]=-d1
	res=np.matmul(cube,k)

	for i in range(8):
		for j in range(4):
			cf=cube[i][0]*n1+cube[i][1]*n2+cube[i][2]*n3-d
			res[i,j]=res[i,j]//cf
	return res

	
if __name__=="__main__":
	print("To run for different scenerios and to make another choice from console click on viewport to get rid of present case\n")
	print("press b for cabinet projection")
	print("press v for cavallier projection")
	print("press z for orthogonal projection in xy plane")
	print("press y for orthogonal projection in xz plane")
	print("press x for orthogonal projection in yz plane")
	print("press o for orthogonal projection(axonometric)")
	print("press i for isometric projection")
	print("press d for isometric projection")
	print("press t for isometric projection")
	print("press p for general perspective projection")
	key=input()
	while True:
		if key=='z':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			#draw(cube,0)
			res=orthogonal(2,cube)
			draw(res,1)
			win.getMouse()
			win.close()
		elif key=='x':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			#draw(cube,0)
			res=orthogonal(0,cube)
			draw(res,1)
			win.getMouse()
			win.close()
		elif key=='y':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			#draw(cube,0)
			res=orthogonal(1,cube)
			draw(res,1)
			win.getMouse()
			win.close()
		elif key=='o':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			res=arbitraryplane_orthogonal(cube,0)
			draw(res,0)
			win.getMouse()
			win.close()
		elif key=='i':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			res=arbitraryplane_orthogonal(cube,1)
			draw(res,0)
			win.getMouse()
			win.close()
		elif key=='d':
			win=createWindow()
			axisDraw()
			res=arbitraryplane_orthogonal(cube,2)
			draw(res,0)
			win.getMouse()
			win.close()
		elif key=='t':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			res=arbitraryplane_orthogonal(cube,3)
			draw(res,0)
			win.getMouse()
			win.close()
		elif key=='p':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			res=perspective(cube,0)
			draw(res,0)
			win.getMouse()
			win.close()
		elif key=='b':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			drawCabinet(cube,0)
			win.getMouse()
			win.close()
		elif key=='v':
			win=createWindow()
			axisDraw()
			cube=np.array([0,0,0,0,0,150,150,0,150,150,0,0,0,150,0,0,150,150,150,150,150,150,150,0])
			cube=cube.reshape(8,3)
			hc=np.ones((8,1),dtype=int)
			cube=np.append(cube,hc,axis=1)
			draw(cube,0)
			win.getMouse()
			win.close()
		elif key=='e':
			break
		else:
			print("Wrong key!")
		key=input()

	
