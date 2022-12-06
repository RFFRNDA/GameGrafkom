import OpenGL.GLUT as glut
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

os.system('cls')

play = False
crash= False
xPosition = 50      #50
yPosition = 100     #100
score_player = 0
fix_score_player = 0
level = 1

# Ghost
xpos_ghost1 = 1500 #1500
ypos_ghost1 = random.randrange(90,550,5)
speed_ghost1 = 0.4

# Angry Ghost
xpos_ghost2 = 3000 #3000
ypos_ghost2 = random.randrange(90,550,5)
speed_ghost2 = 0.7

# Fire Ghost
xpos_ghost3 = 25000
ypos_ghost3 = random.randrange(85,560,2)
speed_ghost3 = 2.5


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
 
def drawTextNum(skor,xpos,ypos,r,b,g):
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_8_BY_13
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in str(skor):
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))

#=== Colors & Decoration =================================================================================

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
orange= 242,99,34
yellow = 250,163,27

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

def char2():    # Ghost
    global xPosition,yPosition,xpos_ghost1,ypos_ghost1,speed_ghost1,yrandom_ghost1
    glPushMatrix()
    glTranslated(xpos_ghost1,ypos_ghost1,0)
    xpos_ghost1 -= speed_ghost1
    if xpos_ghost1 <= -50:
        xpos_ghost1 = 1500
        ypos_ghost1 = yrandom_ghost1
    kotak(-11,38,3,25,black) #ymax
    kotak(-14,35,3,3,black)
    kotak(14,35,3,3,black)
    kotak(-17,32,3,3,black)
    kotak(17,32,3,3,black)
    kotak(-20,29,3,3,black)
    kotak(20,29,6,3,black)
    kotak(-23,26,5,3,black)
    kotak(-26,21,20,3,black)
    kotak(-29,5,4,4,black)
    kotak(23,23,22,3,black)
    kotak(-33,1,6,4,black) #xmin
    kotak(26,1,3,3,black)
    kotak(29,-2,3,8,black)
    kotak(37,1,3,3,black)
    kotak(-29,-5,4,9,black)
    kotak(-20,-9,6,3,black)
    kotak(40,-2,13,3,black) #xmax
    kotak(-17,-15,3,3,black)
    kotak(-14,-18,3,3,black)
    kotak(-11,-21,3,3,black)
    kotak(-8,-24,3,6,black)
    kotak(37,-14,7,3,black)
    kotak(34,-21,3,3,black)
    kotak(27,-24,3,7,black)
    kotak(-2,-27,3,29,black) #ymin
    kotak(8,5,3,9,black)   
    kotak(5,2,6,3,black)   
    kotak(8,-4,3,11,black)   
    kotak(-17,17,6,6,pink) #chick
    kotak(5,17,6,6,pink) #chick
    kotak(-14,23,9,6,black) #eye
    kotak(1,23,9,6,black) #eye
    kotak(-8,10,3,8,black) #mouth
    kotak(-29,1,3,6,softgrey)   
    kotak(-23,21,20,3,softgrey)   
    kotak(-20,26,5,3,softgrey)   
    kotak(-17,29,3,3,softgrey)   
    kotak(-14,32,3,3,softgrey)   
    kotak(-11,35,3,25,softgrey)   
    kotak(13,32,3,3,softgrey)   
    kotak(17,29,6,3,softgrey)   
    kotak(20,23,3,3,softgrey)   
    kotak(-20,-6,3,3,softgrey)   
    kotak(-17,-9,6,3,softgrey)   
    kotak(-14,-15,3,3,softgrey)   
    kotak(-11,-18,3,3,softgrey)   
    kotak(-8,-21,3,6,softgrey)   
    kotak(-2,-24,3,22,softgrey)     
    glPopMatrix()
    
def char3():    # Angry Ghost
    global xpos_ghost2,ypos_ghost2,speed_ghost2,yrandom_ghost2
    glPushMatrix()
    glTranslated(xpos_ghost2,ypos_ghost2,0)
    xpos_ghost2 -= speed_ghost2
    if xpos_ghost2 <= -100:
        xpos_ghost2 = 3000
        ypos_ghost2 = yrandom_ghost2
    kotak(-11,38,3,25,black) #ymax
    kotak(-14,35,3,3,black)
    kotak(14,35,3,3,black)
    kotak(-17,32,3,3,black)
    kotak(17,32,3,3,black)
    kotak(-20,29,3,3,black)
    kotak(20,29,6,3,black)
    kotak(-23,26,5,3,black)
    kotak(-26,21,20,3,black)
    kotak(-29,5,4,4,black)
    kotak(23,23,22,3,black)
    kotak(-33,-3,4,4,black)
    kotak(-35,7,3,6,black)
    kotak(-33,4,3,4,softgrey)
    kotak(-37,6,9,4,black) #xmin
    kotak(26,1,3,3,black)
    kotak(29,-2,3,8,black)
    kotak(37,1,3,3,black)
    kotak(-29,-5,4,9,black) 
    kotak(-20,-9,6,3,black)
    kotak(40,-2,13,3,black) #xmax
    kotak(-17,-15,3,3,black)
    kotak(-14,-18,3,3,black)
    kotak(-11,-21,3,3,black)
    kotak(-8,-24,3,6,black)
    kotak(37,-14,7,3,black)
    kotak(34,-21,3,3,black)
    kotak(27,-24,3,7,black)
    kotak(-2,-27,3,29,black) #ymin
    kotak(14,6,4,6,black)   
    kotak(6,5,8,4,black)   
    kotak(8,8,4,6,black)   
    kotak(14,-5,4,9,black)   
    kotak(10,-3,4,4,black)   
    kotak(-17,17,6,6,pink) #chick
    kotak(5,17,6,6,pink) #chick
    kotak(-14,23,9,6,black) #eye
    kotak(1,23,9,6,black) #eye
    kotak(-14,7,11,15,red) #mouth
    kotak(-2,7,2,3,black) #mouth
    kotak(-5,9,2,3,black) #mouth
    kotak(-8,7,2,3,black) #mouth
    kotak(-11,9,2,3,black) #mouth
    kotak(-14,7,2,3,black) #mouth
    kotak(-2,-4,2,3,black) #mouth
    kotak(-5,-2,2,3,black) #mouth
    kotak(-8,-4,2,3,black) #mouth
    kotak(-11,-2,2,3,black) #mouth
    kotak(-14,-4,2,3,black) #mouth
    kotak(-16,5,9,2,black) #mouth
    kotak(1,5,9,2,black) #mouth
    kotak(-29,1,3,6,softgrey)   
    kotak(-23,21,20,3,softgrey)   
    kotak(-20,26,5,3,softgrey)   
    kotak(-17,29,3,3,softgrey)   
    kotak(-14,32,3,3,softgrey)   
    kotak(-11,35,3,25,softgrey)   
    kotak(13,32,3,3,softgrey)   
    kotak(17,29,6,3,softgrey)   
    kotak(20,23,3,3,softgrey)   
    kotak(-20,-6,3,3,softgrey)   
    kotak(-17,-9,6,3,softgrey)   
    kotak(-14,-15,3,3,softgrey)   
    kotak(-11,-18,3,3,softgrey)   
    kotak(-8,-21,3,6,softgrey)   
    kotak(-2,-24,3,22,softgrey)   
    glPopMatrix()
    
def char4():    # Fire Ghost
    global xpos_ghost3,ypos_ghost3,yrandom_ghost3,speed_ghost3
    glPushMatrix()
    glTranslated(xpos_ghost3,ypos_ghost3,0)
    xpos_ghost3 -= speed_ghost3
    if xpos_ghost3 <= -100:
        xpos_ghost3= 25000
        ypos_ghost3 = yrandom_ghost3
    kotak(-9,-8,7,2,red)
    kotak(-15,6,21,6,red)
    kotak(-13,11,5,6,red)
    kotak(10,-8,3,5,red)
    kotak(8,-10,5,7,red)
    kotak(-11,-15,2,25,red)
    kotak(13,11,4,2,red)
    kotak(15,11,25,7,red)
    kotak(-6,31,10,14,red)
    kotak(-13,21,10,30,red)
    kotak(19,9,8,2,orange)
    kotak(21,3,11,2,orange)
    kotak(19,-6,6,2,orange)
    kotak(17,-10,6,2,orange)
    kotak(14,-14,2,3,orange)
    kotak(6,25,2,4,orange)
    kotak(8,23,2,4,orange)
    kotak(10,21,2,7,orange)
    kotak(15,19,4,2,orange)
    kotak(17,17,10,2,orange)
    kotak(4,31,8,2,orange)
    kotak(2,35,5,2,orange)
    kotak(-4,30,4,5,orange)
    kotak(-11,19,6,2,orange)
    kotak(-9,24,7,3,orange)
    kotak(-6,26,4,2,orange)
    kotak(-14,15,8,3,orange)
    kotak(-16,8,5,2,orange)
    kotak(-17,6,18,2,orange)
    kotak(-15,-10,2,2,orange)
    kotak(-15,-12,4,4,orange)
    kotak(-13,-16,2,29,orange)
    kotak(-7,3,6,5,black) 
    kotak(-11,6,12,2,black)
    kotak(-9, 8, 2 ,2,black)
    kotak(-9 ,-6, 2, 2,black)
    kotak(-7, 11, 3, 2,black)
    kotak(-5 ,11,2, 18,black)
    kotak(-3, -4, 1 ,1,black)
    kotak(-7,-8,6,2,black)
    kotak(-3,-8,6,2,black)
    kotak(1,-8,6,2,black)
    kotak(5,-8,6,2,black)
    kotak(-7,3,6,5,black)
    kotak(2,3,6,5,black)
    kotak(0,-4,1,1,black)
    kotak(11,11,5,2,black)
    kotak(13,7,15,2,black)
    kotak(8,-6,2,5,black)
    kotak(8,-8,2,2,black)
    kotak(-17, 10, 4, 2,black)
    kotak(-17, -12, 4, 2,black)
    kotak(-15, -14, 4, 2,black)
    kotak(-15, -18, 2, 33,black)
    kotak(21 ,11, 8 ,2,black)
    kotak(23 ,5, 15 ,2,black)
    kotak(21 ,-8, 6 ,2,black)
    kotak(16 ,-16, 2, 5,black)
    kotak(19, -12 ,4 ,2,black)
    kotak(-19,7,21,2,black) 
    kotak(-15,17,9,2,black)
    kotak(-13,19,4,2,black)
    kotak(-13,21,2,5,black)
    kotak(-10,26,5,2,black)
    kotak(-8,28,4,2,black)
    kotak(-6,31,5,2,black)
    kotak(-4,32,3,2,black)
    kotak(-2,32,2,4,black)
    kotak(0,35,3,2,black)
    kotak(0,37,2,6,black)
    kotak(4,35,4,2,black)
    kotak(6,33,6,2,black)
    kotak(6,27,2,6,black)
    kotak(10,25,2,4,black)
    kotak(12,23,2,7,black)
    kotak(17,21,4,2,black)
    kotak(19,19,10,2,black)
    glPopMatrix()

#=== Control ====================================================================
def mySpecialKeyboard(key, x, y): 
    global crash,play,yPosition,xPosition,xpos_ghost1,ypos_ghost1,yrandom_ghost1,xpos_ghost2,ypos_ghost2,yrandom_ghost2,score_player,fix_score_player,xpos_ghost3,ypos_ghost3,speed_ghost3,yrandom_ghost3
    if key == GLUT_KEY_LEFT:
        if crash == False:
            if collision():
                crash = True
            else:
                xPosition -= 20
                if xPosition <= 10:
                    xPosition += 20
                    crash = False              
        else:
            xPosition += 0
    elif key == GLUT_KEY_RIGHT:
        if crash == False:
            if collision():
                crash = True
            else:
                xPosition += 20
                if xPosition >= 1420:
                    xPosition -= 20
                    crash = False
        else:
            xPosition += 0
    elif key == GLUT_KEY_UP:
        if crash == False:
            if collision():
                crash = True
            else:
                yPosition += 20
                if yPosition >= 560:
                    yPosition -=20
                    crash = False                 
        else:
            yPosition += 0
    elif key == GLUT_KEY_DOWN:
        if crash == False:
            if collision():
                crash = True
            else:
                yPosition -= 20
                if yPosition <= 40:
                    yPosition += 20
                    crash = False                   
        else:
            yPosition -= 0
    
def myKeyboard(key,x,y):
    global crash,play,score_player,fix_score_player,level,xPosition,yPosition,xpos_ghost1,ypos_ghost1,speed_ghost1,yrandom_ghost1,xpos_ghost2,ypos_ghost2,speed_ghost2,yrandom_ghost2,xpos_ghost3,ypos_ghost3,speed_ghost3,yrandom_ghost3
    if crash == True:
        if ord(key) == ord(b'\r'):
            # Reset All Variable
            crash= False
            play = False
            xPosition = 50      #50
            yPosition = 100     #100
            score_player = 0
            fix_score_player = 0
            level = 1
            # Ghost
            xpos_ghost1 = 1500 #1500
            ypos_ghost1 = random.randrange(90,550,5)
            speed_ghost1 = 0.4
            # Angry Ghost
            xpos_ghost2 = 3000 #3000
            ypos_ghost2 = random.randrange(90,550,5)
            speed_ghost2 = 0.7
            # Fire Ghost
            xpos_ghost3 = 15000
            ypos_ghost3 = random.randrange(85,560,2)
            speed_ghost3 = 2.5

def mouse_play_game(button, state, x, y):       # Click start game
    global play,crash
    if button == GLUT_LEFT_BUTTON:
        if 610 <= x <= 800 and 245 <= y <= 345:
            crash = False
            play = True
        print(x,' ',y)
        
#=== Engine =====================================================================
def gameover():
    global fix_score_player
    glColor3ub(237,35,36)
    glBegin(GL_QUADS)
    glVertex2f(570,450) 
    glVertex2f(570,320) 
    glVertex2f(800,320) 
    glVertex2f(800,450) 
    glEnd()
    drawTextBold("G A M E O V E R",600,400)
    drawText("Enter To Play Again",600,370,38, 33, 98)
    drawText('YOUR FINAL SCORE: ',600,350,0,0,0) 
    drawTextNum(fix_score_player,750,350,0,0,0)
    
def scoring():
    global level,crash,play,yPosition,xPosition,xpos_ghost1,ypos_ghost1,yrandom_ghost1,xpos_ghost2,ypos_ghost2,yrandom_ghost2,score_player,fix_score_player,speed_ghost1,speed_ghost2,speed_ghost3,yrandom_ghost3
    collision()
    if crash == False:
        score_player += 1
        if score_player % 10000 == 0:
            level += 1
            speed_ghost1 += 0.1
            speed_ghost2 += 0.1
            print("speed1",speed_ghost1)
            print("speed2",speed_ghost2)
    else:
        score_player += 0
        
def collision():
    global crash,play,yPosition,xPosition,xpos_ghost1,ypos_ghost1,yrandom_ghost1,xpos_ghost2,ypos_ghost2,yrandom_ghost2,score_player,fix_score_player
    if xpos_ghost1-55 <= xPosition <= xpos_ghost1+63 and ypos_ghost1-79 <= yPosition <= ypos_ghost1+78:
        fix_score_player = score_player
        crash = True
        gameover()   
        score_player += 0
    if xpos_ghost2-55 <= xPosition <= xpos_ghost2+63 and ypos_ghost2-79 <= yPosition <= ypos_ghost2+78:
        fix_score_player = score_player
        gameover()
        crash = True
        score_player += 0
    if xpos_ghost3-40 <= xPosition <= xpos_ghost3+50 and ypos_ghost3-60 <= yPosition <= ypos_ghost3+60:
        fix_score_player = score_player
        gameover()
        crash = True
        score_player += 0

#============ Main Program ==========================================================================

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
    drawText("Use arrow keys to move your character",560,230,0,0,0)
    
def play_game():
    global crash,play,yPosition,xPosition,xpos_ghost1,ypos_ghost1,yrandom_ghost1,xpos_ghost2,ypos_ghost2,yrandom_ghost2,score_player,fix_score_player,xpos_ghost3,ypos_ghost3,speed_ghost3,yrandom_ghost3
    toplimit()
    botlimit()
    if crash == False:
        drawText('LEVEL : ',1000,10,0,0,0) 
        drawTextNum(level,1070,10,0,0,0) 
        drawText('SCORE : ',1200,10,0,0,0) 
        drawTextNum(score_player,1300,10,0,0,0) 
        char2()
        char3()
        char4()
        char1() 
        scoring()
    else:
        gameover()

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
    glutKeyboardFunc(myKeyboard)
    glutSpecialFunc(mySpecialKeyboard)
    glutMouseFunc(mouse_play_game)
    glutMainLoop()

main()
