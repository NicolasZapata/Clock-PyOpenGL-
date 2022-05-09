#MKchaudhary 13th october 2018
# Code edinting for: Nicolas Zapata Alzate
# Unir Colombia


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
from components import display

# Centro y ejes del reloj
xcenter=0	
ycenter=0
radius=200	# Radio del Circulo
hradius=100	# Valor porhora
mradius=140	# Valor por minuto
sradius=170	# Valor por segundo

def ROUND(a):
	return int(a+0.5)

def signal_handler(sig, frame): # Salir del programa con CTRL+C
	print('Precionaste Ctrl+C! para salir del reloj')
	sys.exit(0)

def init():
	glClearColor(0.0,0.0,0.0,0.0)
	glPointSize(4.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-300.0,300.0,-300.0,300.0)


def main():
	signal.signal(signal.SIGINT, signal_handler)
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(600,600)
	glutInitWindowPosition(50,50)
	glutCreateWindow("Reloj UNIR")
	glutDisplayFunc(display.Display(xcenter,ycenter,radius))
	init()
	glutMainLoop()

main()
