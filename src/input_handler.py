"""
Input handler - processes user input
"""

import pygame
import sys


class InputHandler:
    """Handles user input"""
    
    def __init__(self):
        """Initialize the input handler"""
        pass
    
    def handle_keydown(self, key, player, world):
        """Handle keydown events"""
        # Movement with arrow keys
        if key == pygame.K_UP or key == pygame.K_w:
            player.move(0, -1, world)
        elif key == pygame.K_DOWN or key == pygame.K_s:
            player.move(0, 1, world)
        elif key == pygame.K_LEFT or key == pygame.K_a:
            player.move(-1, 0, world)
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            player.move(1, 0, world)
        
        # Diagonal movement
        elif key == pygame.K_q:
            player.move(-1, -1, world)
        elif key == pygame.K_e:
            player.move(1, -1, world)
        elif key == pygame.K_z:
            player.move(-1, 1, world)
        elif key == pygame.K_c:
            player.move(1, 1, world)
        
        # Quit
        elif key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
