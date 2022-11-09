
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


os.system('cls')
w,h= 500,500

xPosition = 0
yPosition = 0
xScale = 1
yScale = 1
rotate = 0

black = 0,0,0
lightcream = 247,209,183
cream = 211,133,101
brown = 77,60,56
lightbrown = 101,80,75
maroon = 108,37,65
brick = 194,67,62
lightgrey = 42,51,55
grey = 30,37,42


def kotak(x,y,height,width,color):
    glBegin(GL_POLYGON) 
    glColor3ub(color[0],color[1],color[2])
    glVertex2f(x,y) # pojok kiri atas
    glVertex2f(x, y - height)
    glVertex2f(x + width, y - height)
    glVertex2f(x + width, y)
    glEnd()

def char1():
    glTranslated(xPosition, yPosition, 0)
    glScaled(xScale,yScale,0)
    glRotated(rotate, 0, 0, 3)

    # --- Main Character ---
    kotak(0,40,40,170,lightcream)
    kotak(-40,190,150,210,lightcream)
    kotak(170,100,60,50,lightcream)
    kotak(-250,190,50,50,lightcream)
    kotak(160,-120,50,50,lightcream)
    kotak(-80,440,210,360,lightbrown)
    kotak(-140,280,280,100,cream)
    kotak(-40,280,90,40,cream)
    kotak(-40,40,40,40,cream)
    kotak(0,230,40,220,cream)
    kotak(-200,100,60,60,cream)
    kotak(-250,150,50,110,cream)
    kotak(-250,400,210,110,brown)
    kotak(-200,190,40,60,brown)
    kotak(-200,440,160,120,brown)
    kotak(-80,350,70,80,brown)
    kotak(0,280,50,70,brown)
    kotak(-250,0,130,370,maroon)
    kotak(-150,-120,50,110,maroon)
    kotak(-250,-120,50,50,cream)
    kotak(-40,-120,50,160,brick)
    kotak(-40,-170,50,160,lightgrey)
    kotak(60,-220,50,60,lightgrey)
    kotak(-150,-170,50,110,grey)
    kotak(-150,-220,50,60,grey)
    kotak(-140,0,50,310,black)
    kotak(170,40,50,50,black)
    kotak(220,230,190,60,black)
    kotak(280,400,210,50,black)
    kotak(200,500,100,80,black)
    kotak(-200,500,60,480,black)
    kotak(-250,440,40,50,black)
    kotak(-300,400,300,50,black)
    kotak(-250,100,60,50,black)
    kotak(-200,40,40,60,black)
    kotak(-250,0,70,50,black)
    kotak(-300,-70,140,50,black)
    kotak(-250,-170,40,50,black)
    kotak(-200,-130,180,50,black)
    kotak(-150,-270,40,50,black)
    kotak(-100,-220,50,60,black)
    kotak(-40,-220,10,60,black)
    kotak(20,-220,90,40,black)
    kotak(60,-270,40,60,black)
    kotak(120,-50,70,50,black)
    kotak(120,-110,60,40,black)
    kotak(120,-170,100,50,black)
    kotak(170,-70,50,50,black)
    kotak(170,-170,50,90,black)
    kotak(210,-110,60,50,black)
    kotak(170,190,90,50,black)  # Eye
    kotak(-100,190,90,60,black) # Eye


def mySpecialKeyboard(key, x, y): 
    global xPosition
    global yPosition
    global xScale
    global yScale
    if key == GLUT_KEY_LEFT:
        xPosition -= 100
    elif key == GLUT_KEY_RIGHT:
        xPosition += 100
    elif key == GLUT_KEY_UP:
        yPosition += 100
    elif key == GLUT_KEY_DOWN:
        yPosition -= 100
    elif key == GLUT_KEY_PAGE_UP:
        xScale += .1
        yScale += .1
    elif key == GLUT_KEY_PAGE_DOWN:
        if xScale < 0.2 and yScale < 0.2:
            xScale -= 0
            yScale -= 0
        else:
            xScale -= .1
            yScale -= .1

def rotated(key, x, y):
    global rotate
    if key == b'.':
        rotate -= 10
    elif key == b',':
        rotate += 10

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1000, 1000, -1000, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    char1()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutSpecialFunc(mySpecialKeyboard)
glutKeyboardFunc(rotated)
glutMainLoop()