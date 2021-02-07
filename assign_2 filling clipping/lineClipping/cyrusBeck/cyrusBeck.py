def dot(a, b):
	return a[0]*b[0]+a[1]*b[1]

def cyrusBeck(x0, y0, x1, y1, vertices):
	N=[]
	# N  =  [(0,-1), (0,1), (1,0), (-1,0)]
	n = len(vertices)
	print(vertices)
	for i in range(n):
		N.append([vertices[(i+1)%n][1]-vertices[(i+2)%n][1], vertices[(i+2)%n][0]-vertices[(i+1)%n][0]])
		# N.append([vertices[i][1]-vertices[(i+1)%n][1], vertices[(i+1)%n][0]-vertices[i][0]])
	print(N)
	p1p0 = [x1-x0, y1-y0]
	p0pE = []
	for i in range(n):
		p0pE.append([x0-vertices[i][0], y0-vertices[i][1]])

	tE = 0
	tL = 1

	for i in range(0, n):
		numerator = dot(N[i], p0pE[i])
		denominator = dot(N[i], p1p0)	
		print(numerator)
		print(denominator)
		if not denominator == 0:
			t = -1*numerator/denominator
			if t<=1 and t>=0:
				if(denominator<0):
					tE = max(tE, t)
				elif(denominator>0):
					tL = min(tL, t)
	print(tE, tL)

	if(tE>tL):
		print("line is rejected completely(trivially)")
		return [[-1, -1], [-1, -1]]

	newPair = []
	newPair.append([])
	newPair.append([])
	print(tE, tL)
	print(p1p0)
	newPair[0].append(x0+p1p0[0]*tE)
	newPair[0].append(y0+p1p0[1]*tE)

	# drawLine(win, x0, y0, newPair[0][0], newPair[0][1], 'red', window, viewPort)

	newPair[1].append(x0+p1p0[0]*tL)
	newPair[1].append(y0+p1p0[1]*tL)
	print(x1, y1)
	print(newPair[1])
	# drawLine(win, newPair[1][0], newPair[1][1], x1, y1, 'red', window, viewPort)

	# drawLine(win, newPair[0][0], newPair[0][1], newPair[1][0], newPair[1][1], 'red', window, viewPort)


	return newPair


