import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

os.system('cls')

play = False
xPosition = 0
yPosition = 0


#=== draw text ================================================================================

def drawText(ch,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))    
 
def drawTextBold(ch,xpos,ypos):
    glPushMatrix()
    color = (0,0,0)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  


#=== Colors =================================================================================

black = 0,0,0
lightcream = 247,209,183
cream = 211,133,101
brown = 77,60,56
lightbrown = 101,80,75
maroon = 108,37,65
brick = 194,67,62
lightgrey = 42,51,55
grey = 30,37,42
pink = 243,121,168
softgrey = 145,135,139
red = 237,35,36

def toplimit():
    glBegin(GL_POLYGON) 
    glColor3ub(101,80,75)
    glVertex2f(0,590) 
    glVertex2f(0,600) 
    glVertex2f(1500,600) 
    glVertex2f(1500,590) 
    glEnd()

def botlimit():
    glBegin(GL_POLYGON) 
    glColor3ub(101,80,75)
    glVertex2f(0,-10) 
    glVertex2f(0,30) 
    glVertex2f(1500,30) 
    glVertex2f(1500,-10) 
    glEnd()

#=== Character =============================================================================

def kotak(x,y,height,width,color):
    glBegin(GL_POLYGON) 
    glColor3ub(color[0],color[1],color[2])
    glVertex2f(x,y) # pojok kiri atas
    glVertex2f(x, y - height)
    glVertex2f(x + width, y- height)
    glVertex2f(x + width, y)
    glEnd()

def char1():    # Main Character
    glPushMatrix()
    glTranslated(xPosition, yPosition, 0)

    kotak(0,4,4,17,lightcream)
    kotak(-4,19,15,21,lightcream)
    kotak(17,10,6,5,lightcream)
    kotak(-25,19,5,5,lightcream)
    kotak(16,-12,5,5,lightcream)
    kotak(-8,44,21,36,lightbrown)
    kotak(-14,28,28,10,cream)
    kotak(-4,28,9,4,cream)
    kotak(-4,4,4,4,cream)
    kotak(0,23,4,22,cream)
    kotak(-20,10,6,6,cream)
    kotak(-25,15,5,11,cream)
    kotak(-25,40,21,11,brown)
    kotak(-20,19,4,6,brown)
    kotak(-20,44,16,12,brown)
    kotak(-8,35,7,8,brown)
    kotak(0,28,5,7,brown)
    kotak(-25,0,13,37,maroon)
    kotak(-15,-12,5,11,maroon)
    kotak(-25,-12,5,5,cream)
    kotak(-4,-12,5,16,brick)
    kotak(-4,-17,5,16,lightgrey)
    kotak(6,-22,5,6,lightgrey)
    kotak(-15,-17,5,11,grey)
    kotak(-15,-22,5,6,grey)

    kotak(-14,0,5,31,black)
    kotak(17,4,5,5,black)
    kotak(22,23,19,5,black)
    kotak(27,40,21,5,black) #xmax
    kotak(20,50,10,8,black) 
    kotak(-20,50,6,48,black) #ymax
    kotak(-25,44,4,5,black)
    kotak(-30,40,30,5,black) #xmin
    kotak(-25,10,6,5,black)
    kotak(-20,4,4,6,black)
    kotak(-25,0,7,5,black)
    kotak(-30,-7,14,5,black)
    kotak(-25,-17,4,5,black)
    kotak(-20,-13,18,5,black)
    kotak(-15,-27,4,5,black)
    kotak(-10,-22,5,7,black)
    kotak(-3,-22,9,6,black)
    kotak(2,-22,9,4,black)
    kotak(6,-27,4,6,black) #ymin
    kotak(12,-5,7,5,black)
    kotak(12,-11,6,4,black)
    kotak(12,-17,10,5,black)
    kotak(17,-7,5,5,black)
    kotak(17,-17,5,9,black)
    kotak(21,-11,6,5,black)
    kotak(14,19,9,6,black)  # Eye
    kotak(-10,19,9,6,black) # Eye
    glPopMatrix()

def mySpecialKeyboard(key, x, y): 
    global xPosition
    global yPosition
    if key == GLUT_KEY_LEFT:
        xPosition -= 20
        if xPosition <= -30:
            xPosition += 20
    elif key == GLUT_KEY_RIGHT:
        xPosition += 20
        if xPosition >= 1380:
            xPosition -=20
    elif key == GLUT_KEY_UP:
        yPosition += 20
        if yPosition >= 450:
            yPosition -=20
    elif key == GLUT_KEY_DOWN:
        yPosition -= 20
        if yPosition <= -50:
            yPosition += 20
    print(xPosition , ' ', yPosition)
    
xpos_ghost1 = 1500 #1500
ypos_ghost1 = 90 #90
yrandom_ghost1 = random.randrange(90,550,5)
speed_ghost1 = 0.2

def kotak2(x,y,height,width,color):
    glBegin(GL_POLYGON) 
    glColor3ub(color[0],color[1],color[2])
    glVertex2f(x , y) # pojok kiri atas
    glVertex2f(x , y - height)
    glVertex2f(x + width , y - height)
    glVertex2f(x + width , y)
    glEnd()

def char2():    # Ghost
    global xPosition,yPosition,xpos_ghost1,ypos_ghost1,speed_ghost1,yrandom_ghost1
    glPushMatrix()
    glTranslated(xpos_ghost1,ypos_ghost1,0)
    xpos_ghost1 -= speed_ghost1
    if xpos_ghost1 <= -50:
        xpos_ghost1 = 1500
        ypos_ghost1 = yrandom_ghost1
    kotak2(-11,38,3,25,black) #ymax
    kotak2(-14,35,3,3,black)
    kotak2(14,35,3,3,black)
    kotak2(-17,32,3,3,black)
    kotak2(17,32,3,3,black)
    kotak2(-20,29,3,3,black)
    kotak2(20,29,6,3,black)
    kotak2(-23,26,5,3,black)
    kotak2(-26,21,20,3,black)
    kotak2(-29,5,4,4,black)
    kotak2(23,23,22,3,black)
    kotak2(-33,1,6,4,black) #xmin
    kotak2(26,1,3,3,black)
    kotak2(29,-2,3,8,black)
    kotak2(37,1,3,3,black)
    kotak2(-29,-5,4,9,black)
    kotak2(-20,-9,6,3,black)
    kotak2(40,-2,13,3,black) #xmax
    kotak2(-17,-15,3,3,black)
    kotak2(-14,-18,3,3,black)
    kotak2(-11,-21,3,3,black)
    kotak2(-8,-24,3,6,black)
    kotak2(37,-14,7,3,black)
    kotak2(34,-21,3,3,black)
    kotak2(27,-24,3,7,black)
    kotak2(-2,-27,3,29,black) #ymin
    kotak2(8,5,3,9,black)   
    kotak2(5,2,6,3,black)   
    kotak2(8,-4,3,11,black)   
    kotak2(-17,17,6,6,pink) #chick
    kotak2(5,17,6,6,pink) #chick
    kotak2(-14,23,9,6,black) #eye
    kotak2(1,23,9,6,black) #eye
    kotak2(-8,10,3,8,black) #mouth
    kotak2(-29,1,3,6,softgrey)   
    kotak2(-23,21,20,3,softgrey)   
    kotak2(-20,26,5,3,softgrey)   
    kotak2(-17,29,3,3,softgrey)   
    kotak2(-14,32,3,3,softgrey)   
    kotak2(-11,35,3,25,softgrey)   
    kotak2(13,32,3,3,softgrey)   
    kotak2(17,29,6,3,softgrey)   
    kotak2(20,23,3,3,softgrey)   
    kotak2(-20,-6,3,3,softgrey)   
    kotak2(-17,-9,6,3,softgrey)   
    kotak2(-14,-15,3,3,softgrey)   
    kotak2(-11,-18,3,3,softgrey)   
    kotak2(-8,-21,3,6,softgrey)   
    kotak2(-2,-24,3,22,softgrey)     
    glPopMatrix()
    
xpos_ghost2 = 1000
ypos_ghost2 = random.randrange(-220,250,5)

def char3():    # Angry Ghost
    global xpos_ghost2,ypos_ghost2
    glPushMatrix()
    glTranslated(xpos_ghost2,ypos_ghost2,0)
    xpos_ghost2 -= 1
    if xpos_ghost2 <= -2000:
        xpos_ghost2 = 1000
        ypos_ghost2 = random.randrange(-220,250,5)
    kotak2(1219,337,3,25,black)
    kotak2(1216,334,3,3,black)
    kotak2(1213,331,3,3,black)
    kotak2(1210,328,3,3,black)
    kotak2(1207,325,5,3,black)
    kotak2(1204,320,16,3,black)
    kotak2(1201,304,4,6,black)
    kotak2(1197,306,4,4,black)
    kotak2(1193,304,8,4,black)
    kotak2(1197,297,4,4,black)
    kotak2(1201,294,4,9,black)
    kotak2(1244,334,3,3,black)
    kotak2(1247,331,3,3,black)
    kotak2(1250,328,6,3,black)
    kotak2(1253,322,22,3,black)
    kotak2(1256,300,3,3,black)
    kotak2(1259,297,3,8,black)
    kotak2(1267,300,3,3,black)
    kotak2(1270,297,13,3,black)
    kotak2(1267,285,7,3,black)
    kotak2(1264,278,3,3,black)
    kotak2(1257,275,3,7,black)
    kotak2(1228,272,3,31,black)
    kotak2(1222,275,3,6,black)
    kotak2(1219,278,3,3,black)
    kotak2(1216,281,3,3,black)
    kotak2(1213,284,3,3,black)
    kotak2(1210,290,6,3,black)
    kotak2(1244,304,4,7,black)
    kotak2(1240,307,4,4,black)
    kotak2(1236,304,8,4,black)
    kotak2(1240,296,4,4,black)
    kotak2(1244,294,4,9,black)
    kotak2(1213,315,6,6,pink) # chik
    kotak2(1234,315,6,6,pink) # chik
    kotak2(1216,322,9,6,black) # eye
    kotak2(1231,322,9,6,black) # eye
    kotak2(1216,306,11,15,red) # - mouth -
    kotak2(1214,304,9,2,black) #
    kotak2(1216,306,2,3,black) #
    kotak2(1219,308,2,3,black) #
    kotak2(1222,306,2,3,black) #
    kotak2(1226,308,2,3,black) # 
    kotak2(1228,306,2,3,black) #
    kotak2(1216,295,2,3,black) #
    kotak2(1219,297,2,3,black) #
    kotak2(1222,295,2,3,black) #
    kotak2(1226,297,2,3,black) #
    kotak2(1228,295,2,3,black) #
    kotak2(1231,304,9,2,black) # - mouth -
    kotak2(1201,300,3,6,softgrey) 
    kotak2(1201,300,3,6,softgrey) 
    kotak2(1207,320,20,3,softgrey) 
    kotak2(1209,325,5,3,softgrey) 
    kotak2(1213,327,3,3,softgrey) 
    kotak2(1216,331,3,3,softgrey) 
    kotak2(1219,334,3,25,softgrey) 
    kotak2(1243,331,3,3,softgrey) 
    kotak2(1247,328,6,3,softgrey) 
    kotak2(1249,322,3,3,softgrey) 
    kotak2(1210,293,3,3,softgrey) 
    kotak2(1213,290,6,3,softgrey) 
    kotak2(1216,284,3,3,softgrey) 
    kotak2(1219,281,3,3,softgrey) 
    kotak2(1222,278,3,6,softgrey) 
    kotak2(1228,275,3,23,softgrey) 
    glPopMatrix()

#=== Engine =====================================================================

def mouse_play_game(button, state, x, y):       # Click start game
    global play
    if button == GLUT_LEFT_BUTTON:
        if 610 <= x <= 800 and 245 <= y <= 345:
            play = True
        print(x,' ',y)

def start_game():
    glPushMatrix()
    glColor3b(36, 150, 127)
    glBegin(GL_QUADS)
    glVertex2f(610,345) 
    glVertex2f(610,245) 
    glVertex2f(800,245) 
    glVertex2f(800,345) 
    glEnd()
    glColor3ub(0,0,0)
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(610,345) 
    glVertex2f(610,245) 
    glVertex2f(800,245) 
    glVertex2f(800,345) 
    glEnd()
    glPopMatrix()
    drawTextBold("P L A Y G A M E", 640, 285)

def play_game():
    toplimit()
    botlimit()
    char2()
    char1() 

#================================================================================

def iterate():
    glViewport(0, 0, 1450, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1450, 0.0, 600, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(255,255,255,1)
    glLoadIdentity()
    iterate()
    if play == False:
        start_game()
    else:
        play_game()

    glutSwapBuffers() #utk membersihkan layar, double buffering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(1450, 600)
    glutInitWindowPosition(40, 100)
    wind = glutCreateWindow("My Game")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(mySpecialKeyboard)
    glutMouseFunc(mouse_play_game)
    glutMainLoop()

main()
