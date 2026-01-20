"""
World class - manages the game world and tiles
"""


class Tile:
    """Represents a single tile in the world"""
    
    def __init__(self, x, y, tile_type='floor', height=0):
        """Initialize a tile"""
        self.x = x
        self.y = y
        self.tile_type = tile_type
        self.height = height
        self.walkable = tile_type != 'wall'


class World:
    """Manages the game world"""
    
    def __init__(self, width=20, height=20):
        """Initialize the world"""
        self.width = width
        self.height = height
        self.tiles = []
        
        # Generate initial world
        self.generate_world()
    
    def generate_world(self):
        """Generate the world tiles"""
        self.tiles = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                # Create walls around the border
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    tile = Tile(x, y, tile_type='wall', height=1)
                else:
                    tile = Tile(x, y, tile_type='floor', height=0)
                row.append(tile)
            self.tiles.append(row)
    
    def get_tile(self, x, y):
        """Get tile at position"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        return None
    
    def is_walkable(self, x, y):
        """Check if a tile is walkable"""
        tile = self.get_tile(x, y)
        if tile is None:
            return False
        return tile.walkable
