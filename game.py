# The reason you have access to this module is because you ran 
# $ pip install pyagme
# Pygame is NOT part of core (like math or random)
import pygame
# Get sys module to exit the program
# import sys
# Import the player class from Player
from player import Player

from game_functions import check_events

# The core game functionality/loop
def run_game():
	# Init all the pygame stuff
	pygame.init()
	# Set up tuple for screensize, (horiz,vert)
	screen_size = (1000,800)
	# Set up a tuple for the bg color
	background_color = (82,111,53)

	# Create a pygame screen to use
	screen = pygame.display.set_mode(screen_size)
	# Set a caption on the terminal window
	pygame.display.set_caption("A heroic 3rd person shooter")

	the_player = Player(screen)

	# Main Game Loop. Run forever...(or until break)
	while 1:
		screen.fill(background_color)                 #fill is a method in pygame

		check_events()

		# Draw the player
		the_player.draw_me()

		# Clear the screen for the next time through the loop
		pygame.display.flip()

# Start the game!
run_game()








