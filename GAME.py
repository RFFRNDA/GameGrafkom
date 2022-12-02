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
    glVertex2f(x+50,y+100) # pojok kiri atas
    glVertex2f((x+50), (y+100) - height)
    glVertex2f((x+50) + width, (y+100) - height)
    glVertex2f((x+50) + width, (y+100))
    glEnd()

def char1():    # Main Character
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
    kotak(27,40,21,5,black)
    kotak(20,50,10,8,black)
    kotak(-20,50,6,48,black)
    kotak(-25,44,4,5,black)
    kotak(-30,40,30,5,black)
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
    kotak(6,-27,4,6,black)
    kotak(12,-5,7,5,black)
    kotak(12,-11,6,4,black)
    kotak(12,-17,10,5,black)
    kotak(17,-7,5,5,black)
    kotak(17,-17,5,9,black)
    kotak(21,-11,6,5,black)
    kotak(14,19,9,6,black)  # Eye
    kotak(-10,19,9,6,black) # Eye

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
    
xpos_ghost1 = 1000
ypos_ghost1 = random.randrange(-220,250,5)

def kotak2(x,y,height,width,color):
    glBegin(GL_POLYGON) 

    glColor3ub(color[0],color[1],color[2])
    glVertex2f(x , y) # pojok kiri atas
    glVertex2f(x , y - height)
    glVertex2f(x + width , y - height)
    glVertex2f(x + width , y)
    glEnd()

def char2():    # Ghost
    global xpos_ghost1,ypos_ghost1
    glPushMatrix()
    glTranslated(xpos_ghost1,ypos_ghost1,0)
    xpos_ghost1 -= 0.5
    if xpos_ghost1 <= -1000:
        xpos_ghost1 = 1000
        ypos_ghost1 = random.randrange(-220,250,5)
    kotak2(1019,337,3,25,black)
    kotak2(1016,334,3,3,black)
    kotak2(1013,331,3,3,black)
    kotak2(1010,328,3,3,black)
    kotak2(1007,325,5,3,black)
    kotak2(1004,320,16,3,black)
    kotak2(1001,304,4,6,black)
    kotak2(997,300,6,4,black)
    kotak2(1001,294,4,9,black)
    kotak2(1044,334,3,3,black)
    kotak2(1047,331,3,3,black)
    kotak2(1050,328,6,3,black)
    kotak2(1053,322,22,3,black)
    kotak2(1056,300,3,3,black)
    kotak2(1059,297,3,8,black)
    kotak2(1067,300,3,3,black)
    kotak2(1070,297,13,3,black)
    kotak2(1067,285,7,3,black)
    kotak2(1064,278,3,3,black)
    kotak2(1057,275,3,7,black)
    kotak2(1028,272,3,31,black)
    kotak2(1022,275,3,6,black)
    kotak2(1019,278,3,3,black)
    kotak2(1016,281,3,3,black)
    kotak2(1013,284,3,3,black)
    kotak2(1010,290,6,3,black)
    kotak2(1038,304,3,9,black)
    kotak2(1035,301,6,3,black)
    kotak2(1038,296,3,11,black)
    kotak2(1013,315,6,6,pink) # chik
    kotak2(1034,315,6,6,pink) # chik
    kotak2(1016,322,9,6,black) # eye
    kotak2(1031,322,9,6,black) # eye
    kotak2(1022,309,3,7,black) # mouth
    kotak2(1001,300,3,6,softgrey) 
    kotak2(1001,300,3,6,softgrey) 
    kotak2(1007,320,20,3,softgrey) 
    kotak2(1009,325,5,3,softgrey) 
    kotak2(1013,327,3,3,softgrey) 
    kotak2(1016,331,3,3,softgrey) 
    kotak2(1019,334,3,25,softgrey) 
    kotak2(1043,331,3,3,softgrey) 
    kotak2(1047,328,6,3,softgrey) 
    kotak2(1049,322,3,3,softgrey) 
    kotak2(1010,293,3,3,softgrey) 
    kotak2(1013,290,6,3,softgrey) 
    kotak2(1016,284,3,3,softgrey) 
    kotak2(1019,281,3,3,softgrey) 
    kotak2(1022,278,3,6,softgrey) 
    kotak2(1028,275,3,23,softgrey) 
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
