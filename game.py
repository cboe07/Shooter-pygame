# The reason you have access to this module is because you ran 
# $ pip install pyagme
# Pygame is NOT part of core (like math or random)
import pygame
# Get sys module to exit the program
# import sys
# Import the player class from Player
from player import Player

from game_functions import check_events
# Get the Enemy class to make new enemies
from enemy import Enemy
# Get groupcollide and Group from the sprite module
from pygame.sprite import Group, groupcollide


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

	the_player = Player(screen,'./images/Hero.png',100,100)
	the_player_group = Group()
	the_player_group.add(the_player)
	bad_guy = Enemy(screen)
	enemies = Group()
	enemies.add(bad_guy)

	

	# Main Game Loop. Run forever...(or until break)
	while 1:
		screen.fill(background_color)                 #fill is a method in pygame

		check_events(the_player)

		# Draw the player
		for player in the_player_group:
			the_player.draw_me()

		# Update and Draw the bad bad_guy
		bad_guy.update_me(the_player)
		bad_guy.draw_me()

		# Check for collisions
		hero_died = groupcollide(the_player_group, enemies, True, False)
		print hero_died

		# Clear the screen for the next time through the loop
		pygame.display.flip()

# Start the game!
run_game()








