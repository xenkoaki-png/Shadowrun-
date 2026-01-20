"""
Main game class - handles the game loop and core game state
"""

import pygame
from src.isometric_renderer import IsometricRenderer
from src.world import World
from src.player import Player
from src.input_handler import InputHandler


class Game:
    """Main game class that manages game state and the main loop"""
    
    def __init__(self):
        """Initialize the game"""
        self.screen_width = 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Shadowrun CDDA - Isometric Grid")
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        
        # Initialize game components
        self.world = World(width=20, height=20)
        self.player = Player(x=10, y=10)
        self.renderer = IsometricRenderer(self.screen, self.screen_width, self.screen_height)
        self.input_handler = InputHandler()
        
        # Camera offset for scrolling
        self.camera_x = 0
        self.camera_y = 0
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.input_handler.handle_keydown(event.key, self.player, self.world)
    
    def update(self):
        """Update game state"""
        # Center camera on player
        self.camera_x = self.player.x
        self.camera_y = self.player.y
    
    def render(self):
        """Render the game"""
        self.screen.fill((20, 20, 30))  # Dark background
        
        # Render world and entities
        self.renderer.render_world(self.world, self.camera_x, self.camera_y)
        self.renderer.render_entity(self.player, self.camera_x, self.camera_y)
        
        # Render UI
        self.render_ui()
        
        pygame.display.flip()
    
    def render_ui(self):
        """Render UI elements"""
        font = pygame.font.Font(None, 24)
        
        # Title
        title_text = font.render("Shadowrun CDDA - Isometric Grid", True, (0, 255, 0))
        self.screen.blit(title_text, (10, 10))
        
        # Position
        pos_text = font.render(f"Position: ({self.player.x}, {self.player.y})", True, (200, 200, 200))
        self.screen.blit(pos_text, (10, 40))
        
        # Controls
        controls_font = pygame.font.Font(None, 20)
        controls = [
            "Controls:",
            "Arrow Keys / WASD - Cardinal movement",
            "Q/E/Z/C - Diagonal movement",
            "ESC - Quit"
        ]
        for i, line in enumerate(controls):
            text = controls_font.render(line, True, (150, 150, 150))
            self.screen.blit(text, (10, self.screen_height - 90 + i * 20))
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
