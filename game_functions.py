import pygame
# Import sys to quit
import sys


pressed_down = {
	"up": False,
	"down": False,
	"right": False,
	"left": False,
}
def check_events(the_player):
	# The escape hatch (from while)
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			# The user clicked the red x. Get out of lopp and kill the game
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == 273:
				the_player.should_move("up", True) 
			elif event.key == 274:
				the_player.should_move('down', True)
			elif event.key == 276:
				the_player.should_move('left', True)
			elif event.key == 275:
				the_player.should_move('right', True)
			# elif event.key == 32:
			# game_paused = not game_paused
		elif event.type == pygame.KEYUP:
			if event.key == 273:
				# the user let go of a key... and that key was the up arrow
				the_player.should_move('up', False)
			if event.key == 274:
				the_player.should_move('down', False)
			if event.key == 276:
				the_player.should_move('left', False)
			if event.key == 275:
				the_player.should_move('right', False)






