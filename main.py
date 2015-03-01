import pygame
from pygame.locals import *

gameState = 0
pygame.init()

while 1:
#	print "state: ", gameState
	# idle
	if gameState == 0:	
		print pygame.event.get()
		for event in pygame.event.get():
			if (event.type == KEYDOWN and event.key == K_SPACE):
				gameState = 1
					 
	# build ship
	elif gameState == 1:
		for event in pygame.event.get():
			if (event.type == KEYDOWN and event.key == K_1):
				gameState = 2

	# shoot
	elif gameState == 2:
		for event in pygame.event.get():
			if (event.type == KEYDOWN and event.key == K_2):
				gameState = 3
		
	# dead
	elif gameState == 3:
		for event in pygame.event.get():
			if (event.type == KEYDOWN and event.key == K_r):
				gameState = 0
			elif (event.type == KEYDOWN and event.key == K_q):
				gameState = 4
	# quit
	elif gameState == 4:
		print "quitting"
	else:
		print 'meow'
