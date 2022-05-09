# Librerias de PyOpenGL, Date y SYS
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from datetime import *
from time import *
import sys
import signal


# Componentes del programa
from components import clock
from components import display

# Funciones donde se alojan las funciones del dibujado del reloj


# Dibujado de las manecillas del reloj
def lineDDA(x0,y0,xEnd,yEnd):	
	delta_x=xEnd-x0
	delta_y=yEnd-y0
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	if steps !=0:
		change_x=dx/float(steps)
		change_y=dy/float(steps)
	else:
		change_x=0
		change_y=0
	setPixel(x,y)
	
	for k in range(int(steps)):
		if delta_x >= 0:  
			x+=change_x
		else:
			x-=change_x
		if delta_y >= 0:
			y+=change_y
		else:
			y-=change_y
		setPixel(x,y)


# Usa el parámetro Form para debujar el círculo
def draw_circle(x,y,radio):	
	glColor(1.0,0.0,0.0)
	theta=0
	while theta <=360:
		angle=(3.14*theta)/180
		xi=x+radio*cos(angle)
		yi=y+radio*sin(angle)
		setPixel(xi,yi)
		theta+=0.5


def Draw():
    glColor3f(0,1,1)
    glut_print( 95+(-5) ,-165+(-5) , GLUT_BITMAP_9_BY_15 , "5" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(165+(-5),-95+(-5), GLUT_BITMAP_9_BY_15 , "4" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(190+(-5),-7 , GLUT_BITMAP_9_BY_15 , "3" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(165+(-7),95+(-7) , GLUT_BITMAP_9_BY_15 , "2" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(95+(-5),165+(-10), GLUT_BITMAP_9_BY_15 , "1" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-3,190+(-10), GLUT_BITMAP_9_BY_15 , "12" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-95+(0),165+(-10), GLUT_BITMAP_9_BY_15 , "11" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-165+(-2),95+(-10), GLUT_BITMAP_9_BY_15 , "10" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-190+(-3),-7 , GLUT_BITMAP_9_BY_15 , "9" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-165+(-5),-95+(-3) , GLUT_BITMAP_9_BY_15 , "8" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-95+(-5),-165+(-5), GLUT_BITMAP_9_BY_15 , "7" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print(-6,-190+(-5), GLUT_BITMAP_9_BY_15 , "6" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( -35 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )
    glut_print( 0 ,-250, GLUT_BITMAP_9_BY_15 , ":" , 1.0 , 1.0 , 1.0 , 1.0 )

# Define los pixeles
def setPixel(x,y):
	glBegin(GL_POINTS)
	glVertex2f(x,y)
	glEnd()
	glFlush()

# Imprime el glutprint
def glut_print( x,  y,  font,  text, r,  g , b , a):
    glRasterPos2f(x,y)
    for ch in text :
        glutBitmapCharacter( font , ctypes.c_int( ord(ch) ) ) 
 






