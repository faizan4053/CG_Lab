# https://www.ques10.com/p/22022/explain-scan-line-polygon-filling-algorithm/
# https://www.ques10.com/p/11008/explain-scan-line-fill-algorithm-with-an-example-1/

from winSize import *
from graphics import *
from drawLine import *
from drawPolygon import *
from windowToViewport import *

EdgeTable={}
ActiveEdgeTuple=[]
yvmin=0
yvmax=500

class edgeBucket:
	def __init__(self, ymax=None, xofymin=None, slopeinverse=None):
		self.ymax=ymax #ymax #max y-coordinate of edge 
		self.xofymin=xofymin #xofymin #x-coordinate of lowest edge point updated only in aet
		self.slopeinverse=slopeinverse

def printET(et):
	for i in et:
		print(i.ymax, i.xofymin, i.slopeinverse)
	

def insertionSort(ett):
	temp=edgeBucket() 

	for i in range(1, len(ett)): 
		temp.ymax = ett[i].ymax 
		temp.xofymin = ett[i].xofymin 
		temp.slopeinverse = ett[i].slopeinverse 
		j = i - 1 

		while(j >= 0 and temp.xofymin < ett[j].xofymin): 
			ett[j + 1].ymax = ett[j].ymax 
			ett[j + 1].xofymin = ett[j].xofymin 
			ett[j + 1].slopeinverse = ett[j].slopeinverse 
			j = j - 1 
		ett[j + 1].ymax = temp.ymax 
		ett[j + 1].xofymin = temp.xofymin 
		ett[j + 1].slopeinverse = temp.slopeinverse

def initEdgeTable():
	for i in range(yvmin, yvmax):
		EdgeTable[i]=[]

def updatexbyslopeinv():
	for i in ActiveEdgeTuple:
		i.xofymin+=i.slopeinverse

def removeEdgeByYmax(Tup, yy):
	i=0
	while(i<len(Tup)):
		if (Tup[i].ymax == yy): 
			# print("Removed at "+str(yy))
			del Tup[i]
		else:
			i+=1


def storeEdgeInTuple(et, ymaxTS, xwithyminTS, minv):
	et.append(edgeBucket(ymaxTS, xwithyminTS, minv))
	insertionSort(et)
	# printET(et)

def storeEdgeInTable(x1, y1, x2, y2):
	m=0
	minv=0
	ymaxTS=0
	xwithyminTS=0
	scanline=0 #ts stands for to store 

	if (x2==x1):
		minv=0.000000
	else:
		m = float(y2-y1)/float(x2-x1) 
		
		# horizontal lines are not stored in edge table 
		if (y2==y1):
			return
			
		minv = float(1.0/m)
		# print("Slope string for ",x1,y1," & ",x2,y2," : ",minv) 

	if (y1>y2): 
		scanline=y2 
		ymaxTS=y1 
		xwithyminTS=x2
	else:
		scanline=y1
		ymaxTS=y2
		xwithyminTS=x1
	# # the assignment part is done..now storage.. 
	# print(scanline, ymaxTS, xwithyminTS, minv)
	# print()
	storeEdgeInTuple(EdgeTable[scanline],ymaxTS,xwithyminTS,minv)


def scanLineFill(win, window, viewPort):
	# print(yvmin, yvmax)
	# return
	for i in range(yvmin, yvmax):
		for j in EdgeTable[i]:
			storeEdgeInTuple(ActiveEdgeTuple, j.ymax, j.xofymin, j.slopeinverse)

		printET(ActiveEdgeTuple)
		print(i)
		print()
		print()

		removeEdgeByYmax(ActiveEdgeTuple, i) 
		FillFlag = 0
		coordCount = 0
		x1 = 0
		x2 = 0
		ymax1 = 0
		ymax2 = 0
		j=0
		while (j<len(ActiveEdgeTuple)):
			if (coordCount%2==0): 
				x1 = int(ActiveEdgeTuple[j].xofymin) 
				ymax1 = ActiveEdgeTuple[j].ymax 
				if (x1==x2): 

				# /* three cases can arrive- 
				# 	1. lines are towards top of the intersection 
				# 	2. lines are towards bottom 
				# 	3. one line is towards top and other is towards bottom 
				# */
					if (((x1==ymax1) and (x2!=ymax2)) or ((x1!=ymax1) and (x2==ymax2))):
						x2 = x1 
						ymax2 = ymax1 
					else:
						coordCount+=1 
				else:
					coordCount+=1 
			else:
				x2 = int(ActiveEdgeTuple[j].xofymin)
				ymax2 = ActiveEdgeTuple[j].ymax
				FillFlag = 0 
				print(x1, ymax1, x2, ymax2, FillFlag)

				# checking for intersection... 
				if (x1==x2) :

					# /*three cases can arive- 
					# 	1. lines are towards top of the intersection 
					# 	2. lines are towards bottom 
					# 	3. one line is towards top and other is towards bottom 
					# */
					if (((x1==ymax1) and (x2!=ymax2)) or ((x1!=ymax1) and (x2==ymax2))):					
						x1 = x2 
						ymax1 = ymax2 
					else:
						coordCount+=1 
						FillFlag = 1 
				else:
					coordCount+=1 
					FillFlag = 1
				print(x1, ymax1, x2, ymax2, FillFlag)
				if(FillFlag):
					drawLine(win, x1, i, x2, i, 'yellow', window, viewPort)
					print("\nLine drawn from "+str(x1)+", "+str(i)+" to "+str(x2)+" "+str(i))
			j+=1
		updatexbyslopeinv()




print( " Enter window size im the following order (xmin , xmax , ymin , ymax) :-")
xmin , xmax , ymin , ymax = map(int, input().split())
window = size(xmin , xmax , ymin , ymax)

print( " Enter viewport size in the following order (xmin , xmax , ymin , ymax) :-")
xvmin , xvmax , yvmin , yvmax = map(int, input().split())
viewPort = size(0 , xvmax - xvmin, 0 , yvmax - yvmin)

win = GraphWin(' Line ' , xvmax - xvmin , yvmax - yvmin)

drawLine(win, 0 , window.ymax, 0, window.ymin, 'blue', window,viewPort )
drawLine(win, window.xmin , 0 , window.xmax, 0, 'red', window,viewPort )

n=int(input("enter number of edges in polygon: "))
print("Enter vertices of the edges as (x, y) one by one")
vertices=[]
for i in range(n):
	vertices.append(list(map(int, input().split())))

print(vertices)

initEdgeTable()
i=0
count=0
while(i<len(vertices)): 
		count+=1
		if(count>2): 
			x1 = x2 
			y1 = y2 
			count=2 
		if (count==1): 
			x1, y1=vertices[i][0], vertices[i][1] 
		else: 
			x2, y2=vertices[i][0], vertices[i][1] 
			print(x1, y1, x2, y2)
			storeEdgeInTable(x1, y1, x2, y2) #storage of edges in edge table. 
		i+=1
print(vertices[-1][0], vertices[-1][1], vertices[0][0], vertices[0][1])
storeEdgeInTable(vertices[-1][0], vertices[-1][1], vertices[0][0], vertices[0][1])
scanLineFill(win, window, viewPort)

print("Click on window to exit")


win.getMouse()
win.close 





