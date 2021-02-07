from graphics import *
import numpy as np

def onePointPerspective(win,coordinates,viewpoint):
    a = viewpoint[0]
    b = viewpoint[1]
    c = viewpoint[2]
    matrix2=np.array([[c,0,0,0],[0,c,0,0],[-a,-b,0,0],[0,0,-1,c]])
    res = np.dot(coordinates,matrix2)
    return res

def drawAxis(win,X1,X2,Y1,Y2):
    L = Line(Point(X1,0),Point(X2,0))
    L.draw(win)
    L.setOutline('red')
    L = Line(Point(0,Y1),Point(0,Y2))
    L.draw(win)
    L.setOutline('blue')

def visibility(surface, viewpoint):
    normal = np.cross(surface[1]-surface[0], surface[2]-surface[1])
    ray = viewpoint - surface[0]
    res = np.dot(ray, normal)
    if res <= 0:
        return False
    else:
        return True

def main():
    #setting up the window
    WIN_X,WIN_Y = 500,500
    X1,X2,Y1,Y2 = -WIN_X//2,WIN_X//2,-WIN_Y//2,WIN_Y//2
    win=GraphWin("drawLine",WIN_X,WIN_Y )
    win.setCoords(X1,Y1,X2,Y2)
    drawAxis(win,X1,X2,Y1,Y2)
    
    #view point coordinates
    viewpoint = np.array([150, -200, -200])
    
    #obtain perspective coordinates
    coordinates = np.array([[0,0,100,1],[0,0,0,1],[100,0,0,1],[100,0,100,1],[0,100,100,1],[0,100,0,1],[100,100,0,1],[100,100,100,1]])
    res = onePointPerspective(win, coordinates, viewpoint)
    for row in res:
        if row[3] != 0:
            row[0] = row[0]/row[3]
            row[1] = row[1]/row[3]
            row[2] = row[2]/row[3]
            row[3] = row[3]/row[3]
    
    #check visibility of surface 1
    surface1 = np.array([coordinates[0][:-1], coordinates[4][:-1], coordinates[5][:-1], coordinates[1][:-1]])
    if(visibility(surface1, viewpoint)):
        rect = Polygon(Point(res[0][0],res[0][1]),Point(res[4][0],res[4][1]),Point(res[5][0],res[5][1]),Point(res[1][0],res[1][1]))
        rect.setFill('blue')
        rect.draw(win)
    
    #check visiblity of surface 2
    surface2 = np.array([coordinates[7][:-1],coordinates[3][:-1], coordinates[2][:-1], coordinates[6][:-1]])
    if(visibility(surface2, viewpoint)):
        rect = Polygon(Point(res[7][0],res[7][1]),Point(res[3][0],res[3][1]),Point(res[2][0],res[2][1]),Point(res[6][0],res[6][1]))
        rect.setFill('red')
        rect.draw(win)
    
    #check visibility of surface 3
    surface3 = np.array([coordinates[0][:-1],coordinates[1][:-1], coordinates[2][:-1], coordinates[3][:-1]])
    if(visibility(surface3, viewpoint)):
        rect = Polygon(Point(res[0][0],res[0][1]),Point(res[1][0],res[1][1]),Point(res[2][0],res[2][1]),Point(res[3][0],res[3][1]))
        rect.setFill('green')
        rect.draw(win)
    
    #check visibility of surface 4
    surface4 = np.array([coordinates[4][:-1],coordinates[7][:-1], coordinates[6][:-1], coordinates[5][:-1]])
    if(visibility(surface4, viewpoint)):
        rect = Polygon(Point(res[4][0],res[4][1]),Point(res[7][0],res[7][1]),Point(res[6][0],res[6][1]),Point(res[5][0],res[5][1]))
        rect.setFill('yellow')
        rect.draw(win)
    
    #check visibility of surface 5
    surface5 = np.array([coordinates[0][:-1],coordinates[3][:-1], coordinates[7][:-1], coordinates[4][:-1]])
    if(visibility(surface5, viewpoint)):
        rect = Polygon(Point(res[0][0],res[0][1]),Point(res[3][0],res[3][1]),Point(res[7][0],res[7][1]),Point(res[4][0],res[4][1]))
        rect.setFill('violet')
        rect.draw(win)
    
    #check visibility of surface 6
    surface6 = np.array([coordinates[1][:-1], coordinates[5][:-1], coordinates[6][:-1], coordinates[2][:-1]])
    if(visibility(surface6, viewpoint)):
        rect = Polygon(Point(res[1][0],res[1][1]),Point(res[5][0],res[5][1]),Point(res[6][0],res[6][1]),Point(res[2][0],res[2][1]))
        rect.setFill('orange')
        rect.draw(win)
    win.getMouse()
    win.close()
main()

