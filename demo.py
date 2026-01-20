#!/usr/bin/env python3
"""
Demo script to showcase the isometric grid rendering
Runs in headless mode and saves a screenshot
"""

import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
import sys

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.isometric_renderer import IsometricRenderer
from src.world import World
from src.player import Player


def create_demo_screenshot():
    """Create a screenshot of the isometric grid"""
    pygame.init()
    
    # Create display
    screen_width = 1024
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Initialize components
    world = World(width=20, height=20)
    player = Player(x=10, y=10)
    renderer = IsometricRenderer(screen, screen_width, screen_height)
    
    # Render one frame
    screen.fill((20, 20, 30))
    renderer.render_world(world, player.x, player.y)
    renderer.render_entity(player, player.x, player.y)
    
    # Draw title
    font = pygame.font.Font(None, 36)
    title = font.render("Shadowrun CDDA - Isometric Grid Demo", True, (0, 255, 0))
    screen.blit(title, (20, 20))
    
    # Draw info
    info_font = pygame.font.Font(None, 24)
    info_lines = [
        "Isometric grid-based game",
        "Player at center (green circle)",
        "Walls around border",
        "CDDA meets Shadowrun theme"
    ]
    for i, line in enumerate(info_lines):
        text = info_font.render(line, True, (200, 200, 200))
        screen.blit(text, (20, 70 + i * 30))
    
    # Save screenshot
    pygame.image.save(screen, "demo_screenshot.png")
    print("✓ Screenshot saved as demo_screenshot.png")
    
    pygame.quit()


if __name__ == '__main__':
    create_demo_screenshot()
