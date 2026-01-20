"""
Test the core game components
"""

import os
import sys
os.environ['SDL_VIDEODRIVER'] = 'dummy'  # For headless testing

import pygame
pygame.init()

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.world import World, Tile
from src.player import Player
from src.isometric_renderer import IsometricRenderer


def test_tile_creation():
    """Test tile creation"""
    tile = Tile(5, 5, 'floor', 0)
    assert tile.x == 5
    assert tile.y == 5
    assert tile.tile_type == 'floor'
    assert tile.height == 0
    assert tile.walkable is True
    
    wall = Tile(0, 0, 'wall', 1)
    assert wall.walkable is False
    print("✓ Tile creation test passed")


def test_world_generation():
    """Test world generation"""
    world = World(width=10, height=10)
    assert world.width == 10
    assert world.height == 10
    assert len(world.tiles) == 10
    assert len(world.tiles[0]) == 10
    
    # Check corners are walls
    assert world.get_tile(0, 0).tile_type == 'wall'
    assert world.get_tile(9, 9).tile_type == 'wall'
    
    # Check center is floor
    assert world.get_tile(5, 5).tile_type == 'floor'
    print("✓ World generation test passed")


def test_player_movement():
    """Test player movement"""
    world = World(width=10, height=10)
    player = Player(5, 5)
    
    assert player.x == 5
    assert player.y == 5
    
    # Move right
    result = player.move(1, 0, world)
    assert result is True
    assert player.x == 6
    assert player.y == 5
    
    # Try to move into wall (should fail)
    player.x = 1
    player.y = 1
    result = player.move(-1, 0, world)
    assert result is False
    assert player.x == 1  # Should not have moved
    print("✓ Player movement test passed")


def test_isometric_conversion():
    """Test isometric coordinate conversion"""
    screen = pygame.display.set_mode((800, 600))
    renderer = IsometricRenderer(screen, 800, 600)
    
    # Test cartesian to isometric conversion
    iso_x, iso_y = renderer.cart_to_iso(0, 0)
    assert iso_x == 0
    assert iso_y == 0
    
    # Test with non-zero coordinates
    iso_x, iso_y = renderer.cart_to_iso(1, 0)
    assert iso_x == 32  # tile_width // 2
    assert iso_y == 16  # tile_height // 2
    
    print("✓ Isometric conversion test passed")


def test_player_stats():
    """Test player stats"""
    player = Player(0, 0)
    
    assert player.health == 100
    assert player.max_health == 100
    assert player.essence == 6.0
    assert player.nuyen == 5000
    
    # Test damage
    player.take_damage(30)
    assert player.health == 70
    
    # Test healing
    player.heal(20)
    assert player.health == 90
    
    # Test healing cap
    player.heal(50)
    assert player.health == 100  # Should cap at max_health
    
    print("✓ Player stats test passed")


if __name__ == '__main__':
    print("Running tests...")
    test_tile_creation()
    test_world_generation()
    test_player_movement()
    test_isometric_conversion()
    test_player_stats()
    print("\n✅ All tests passed!")
