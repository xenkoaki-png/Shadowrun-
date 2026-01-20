"""
Isometric renderer - handles rendering of isometric grid and entities
"""

import pygame


class IsometricRenderer:
    """Renders game world in isometric perspective"""
    
    def __init__(self, screen, screen_width, screen_height):
        """Initialize the isometric renderer"""
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Isometric tile dimensions
        self.tile_width = 64
        self.tile_height = 32
        
        # Colors for different tile types
        self.colors = {
            'floor': (60, 60, 80),
            'floor_alt': (50, 50, 70),
            'wall': (100, 100, 120),
            'player': (0, 255, 100),
            'highlight': (255, 255, 100)
        }
    
    def cart_to_iso(self, x, y):
        """Convert cartesian coordinates to isometric screen coordinates"""
        iso_x = (x - y) * (self.tile_width // 2)
        iso_y = (x + y) * (self.tile_height // 2)
        return iso_x, iso_y
    
    def world_to_screen(self, x, y, camera_x, camera_y):
        """Convert world coordinates to screen coordinates with camera offset"""
        # Convert to isometric
        iso_x, iso_y = self.cart_to_iso(x, y)
        
        # Apply camera offset
        cam_iso_x, cam_iso_y = self.cart_to_iso(camera_x, camera_y)
        
        # Center on screen
        screen_x = iso_x - cam_iso_x + self.screen_width // 2
        screen_y = iso_y - cam_iso_y + self.screen_height // 2
        
        return screen_x, screen_y
    
    def draw_isometric_tile(self, x, y, camera_x, camera_y, color, height=0):
        """Draw a single isometric tile"""
        screen_x, screen_y = self.world_to_screen(x, y, camera_x, camera_y)
        
        # Adjust for height
        screen_y -= height * 10
        
        # Diamond shape for isometric tile
        points = [
            (screen_x, screen_y),                           # Top
            (screen_x + self.tile_width // 2, screen_y + self.tile_height // 2),  # Right
            (screen_x, screen_y + self.tile_height),        # Bottom
            (screen_x - self.tile_width // 2, screen_y + self.tile_height // 2),  # Left
        ]
        
        pygame.draw.polygon(self.screen, color, points)
        pygame.draw.polygon(self.screen, (40, 40, 50), points, 1)  # Border
    
    def render_world(self, world, camera_x, camera_y):
        """Render the entire world"""
        # Render tiles
        for y in range(world.height):
            for x in range(world.width):
                tile = world.get_tile(x, y)
                
                # Checkerboard pattern for floor
                if (x + y) % 2 == 0:
                    color = self.colors['floor']
                else:
                    color = self.colors['floor_alt']
                
                # Different color for walls
                if tile.tile_type == 'wall':
                    color = self.colors['wall']
                
                self.draw_isometric_tile(x, y, camera_x, camera_y, color, tile.height)
    
    def render_entity(self, entity, camera_x, camera_y):
        """Render an entity (player, NPC, item, etc.)"""
        screen_x, screen_y = self.world_to_screen(entity.x, entity.y, camera_x, camera_y)
        
        # Draw entity as a circle for now
        pygame.draw.circle(self.screen, self.colors.get(entity.color, (255, 255, 255)), 
                          (int(screen_x), int(screen_y - 20)), 12)
        
        # Draw outline
        pygame.draw.circle(self.screen, (255, 255, 255), 
                          (int(screen_x), int(screen_y - 20)), 12, 2)
