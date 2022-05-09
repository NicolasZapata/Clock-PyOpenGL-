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
from components import draw



# Configuracion de la pantalla del programa
def Display(x, y, r): # Eje X y Y y el radio
	glClear(GL_COLOR_BUFFER_BIT)
	draw.draw_circle(x,y,r)
	draw.Draw()
	glut_print(-50 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().day), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-30 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(-20,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().month), 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(0 ,-280, GLUT_BITMAP_9_BY_15 ,"-", 1.0 , 1.0 , 1.0 , 1.0 )
	glut_print(10 ,-280, GLUT_BITMAP_9_BY_15 ,str(datetime.now().year), 1.0 , 1.0 , 1.0 , 1.0 )
	draw.clock()


