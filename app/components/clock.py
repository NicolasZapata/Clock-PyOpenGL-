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
from components import draw
from components import display


def get_time():
	global hr,mint,sec
	currentT=datetime.now()
	hr=currentT.hour
	if hr > 12:
		hr=hr- 12
	mint=currentT.minute
	sec=currentT.second


def second_niddle(sec):
	glColor(0.0,0.0,0.0)
    # this is actually not required in program logic
	lineDDA(0,0,-18.164716180901422, 169.02675257505038)  
	sx=sradius*cos((90-sec*6+6)*3.14/180) 
	sy=sradius*sin((90-sec*6+6)*3.14/180)
	lineDDA(0,0,sx,sy)
	glColor(1.0,1.0,1.0)
	sx=sradius*cos((90-sec*6)*3.14/180) 
	sy=sradius*sin((90-sec*6)*3.14/180)
	lineDDA(0,0,sx,sy)

def minute_niddle(mint):
	glColor(0.0,0.0,0.0)
	mx=mradius*cos((90-mint*6+6)*3.14/180)
	my=mradius*sin((90-mint*6+6)*3.14/180)
	lineDDA(0,0,mx,my)
	glColor(1.0,1.0,0.0)
	mx=mradius*cos((90-mint*6)*3.14/180) 
	my=mradius*sin((90-mint*6)*3.14/180)
	lineDDA(0,0,mx,my)

def hour_niddle(hr):
	glColor(0.0,0.0,0.0)
	hx=hradius*cos((90-hr*30+30)*3.14/180)
	hy=hradius*sin((90-hr*30+30)*3.14/180)
	lineDDA(0,0,hx,hy)
	glColor(1.0,0.0,1.0)
	hx=hradius*cos((90-hr*30)*3.14/180)
	hy=hradius*sin((90-hr*30)*3.14/180)
	draw.lineDDA(0,0,hx,hy)

def clock():
	while True:
		get_time()
		if sec ==0:
			s=60
			mi=mint-1
		else:
			s=sec-1
			mi=mint
		if mint==0:
			h=hr-1
		else:
			h=hr
		glColor3f(0,0,0)
		glut_print(10 ,-250, GLUT_BITMAP_9_BY_15 ,str(s), 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( 10 ,-250, GLUT_BITMAP_9_BY_15 , str(sec) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mi) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -20 ,-250, GLUT_BITMAP_9_BY_15 , str(mint) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(0,0,0)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(h) , 1.0 , 1.0 , 1.0 , 1.0 )
		glColor3f(1,1,1)
		glut_print( -50 ,-250, GLUT_BITMAP_9_BY_15 , str(hr) , 1.0 , 1.0 , 1.0 , 1.0 )
		second_niddle(sec)
		minute_niddle(mint)
		hour_niddle(hr)






