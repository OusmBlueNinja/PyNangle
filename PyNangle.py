import sys,time, math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class color():
	black = (0,0,0)
	white = (255,255,255)
	red =(255,0,0)
	green = (0,255,0)
	blue = (0,0,255)

clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 25)
Res = [700,500]
win = pygame.display.set_mode(Res)
pygame.display.set_caption("Py-Nangle v 1.2")
DEBUG = True

#set pos to the position of something and set sizex and y to the size of the item, insert any pos	to itemPos and it will check if that pos is inside the other, if so it will return True else False
def colide(pos, sizex, sizey, itemPos):
	if itemPos[0] >= pos[0] and itemPos[0] <= (pos[0] + sizex):
		if itemPos[1] >= pos[1] and itemPos[1] <= (pos[1] + sizey):
			return True
		else:
			return False
	else:
		return False


def drawLine(pos1, pos2):
	 pygame.draw.line(win, color.red, pos1, pos2, 2)

def drawTriangle(pos1, pos2):
	 pygame.draw.line(win, color.blue, (pos2[0], pos1[1]), pos1, 2)
	 pygame.draw.line(win, color.green, (pos2[0], pos1[1]), pos2, 2)

def drawText(pos1, pos2):
	#(pos2[0], pos1[1]), pos2
	win.blit(font.render("len R: {}".format(round(math.dist(pos1, pos2)), 1), True, color.red), (10, 5))
	win.blit(font.render("len G: {}".format(math.dist((pos2[0], pos1[1]), pos2)), True, color.green), (10, 25))
	win.blit(font.render("len B: {}".format(math.dist((pos2[0], pos1[1]), pos1)), True, color.blue), (10, 45))
	 


hasClicked = False
oldMousePos = []
run = True
while run:
	win.fill(color.black)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				run = False

	mousePos = pygame.mouse.get_pos()



	if pygame.mouse.get_pressed()[0]:
		oldMousePos = mousePos
		hasClicked = True
	elif pygame.mouse.get_pressed()[2]:
		hasClicked = False

	if hasClicked:
		drawLine(oldMousePos, mousePos)
		drawTriangle(oldMousePos, mousePos)
		drawText(oldMousePos, mousePos)
		win.blit(font.render("Right Click Anyware To Close", True, color.white), ((Res[0]/2)-120, 5))
	else:
		win.blit(font.render("Click Anyware To Start", True, color.white), ((Res[0]/2)-100, 5))
		 
	print(mousePos, oldMousePos)
	FPS = round(clock.get_fps(), 1)
	if DEBUG:

	  win.blit(font.render("FPS: {}".format(FPS), True, color.white), (Res[0] - 100, 5))
	clock.tick()
	pygame.display.update()



