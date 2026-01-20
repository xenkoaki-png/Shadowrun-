"""
Player class - represents the player character
"""


class Player:
    """Player character"""
    
    def __init__(self, x, y):
        """Initialize the player"""
        self.x = x
        self.y = y
        self.color = 'player'
        
        # Player stats (Shadowrun inspired)
        self.name = "Runner"
        self.health = 100
        self.max_health = 100
        self.essence = 6.0  # Shadowrun essence rating
        self.nuyen = 5000  # Shadowrun currency
        
        # Attributes
        self.body = 3
        self.agility = 3
        self.reaction = 3
        self.strength = 3
        self.willpower = 3
        self.logic = 3
        self.intuition = 3
        self.charisma = 3
        
        # Skills
        self.skills = {
            'firearms': 0,
            'close_combat': 0,
            'athletics': 0,
            'stealth': 0,
            'hacking': 0,
            'electronics': 0,
        }
    
    def move(self, dx, dy, world):
        """Move the player by dx, dy if valid"""
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check if the new position is walkable
        if world.is_walkable(new_x, new_y):
            self.x = new_x
            self.y = new_y
            return True
        return False
    
    def take_damage(self, amount):
        """Take damage"""
        self.health = max(0, self.health - amount)
    
    def heal(self, amount):
        """Heal damage"""
        self.health = min(self.max_health, self.health + amount)
