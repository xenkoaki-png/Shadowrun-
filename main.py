#!/usr/bin/env python3
"""
Shadowrun CDDA - A CDDA Meets Shadowrun game in an Isometric grid
Main entry point for the game
"""

import sys
import pygame
from src.game import Game


def main():
    """Main entry point for the game"""
    pygame.init()
    
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error running game: {e}")
        import traceback
        traceback.print_exc()
        return 1
    finally:
        pygame.quit()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
