"""
World Creation Module for Shadowrun
Handles creation and management of game worlds
"""

import json
import os
from datetime import datetime


class WorldCreator:
    """Handles creation of Shadowrun game worlds"""
    
    def __init__(self):
        self.world_data = {}
        
    def create_world(self):
        """Interactive world creation process"""
        print("\n" + "=" * 60)
        print("WORLD CREATION")
        print("=" * 60)
        
        # World name
        world_name = input("\nEnter world name: ").strip()
        if not world_name:
            world_name = f"Shadowrun World {datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Year setting
        print("\nShadowrun Timeline:")
        print("1. 2050s (Early Shadowrun era)")
        print("2. 2070s (Modern Shadowrun)")
        print("3. 2080s (Latest timeline)")
        print("4. Custom")
        
        year_choice = input("\nSelect timeline (1-4): ").strip()
        year_map = {
            "1": 2050,
            "2": 2070,
            "3": 2080
        }
        
        if year_choice == "4":
            year = input("Enter custom year: ").strip()
            try:
                year = int(year)
            except ValueError:
                year = 2070
        else:
            year = year_map.get(year_choice, 2070)
        
        # Location
        print("\nPrimary Location:")
        print("1. Seattle")
        print("2. Neo-Tokyo")
        print("3. Berlin")
        print("4. Hong Kong")
        print("5. Custom")
        
        location_choice = input("\nSelect location (1-5): ").strip()
        location_map = {
            "1": "Seattle",
            "2": "Neo-Tokyo",
            "3": "Berlin",
            "4": "Hong Kong"
        }
        
        if location_choice == "5":
            location = input("Enter custom location: ").strip()
        else:
            location = location_map.get(location_choice, "Seattle")
        
        # Difficulty
        print("\nWorld Difficulty:")
        print("1. Street Level (Easier)")
        print("2. Professional (Standard)")
        print("3. Elite (Challenging)")
        
        difficulty_choice = input("\nSelect difficulty (1-3): ").strip()
        difficulty_map = {
            "1": "Street Level",
            "2": "Professional",
            "3": "Elite"
        }
        difficulty = difficulty_map.get(difficulty_choice, "Professional")
        
        # Additional settings
        magic_enabled = input("\nEnable magic? (y/n): ").strip().lower() == 'y'
        matrix_enabled = input("Enable matrix/cyberspace? (y/n): ").strip().lower() == 'y'
        
        # Create world data structure
        self.world_data = {
            "name": world_name,
            "year": year,
            "location": location,
            "difficulty": difficulty,
            "magic_enabled": magic_enabled,
            "matrix_enabled": matrix_enabled,
            "created_at": datetime.now().isoformat(),
            "characters": []
        }
        
        print("\n" + "-" * 60)
        print(f"World '{world_name}' created successfully!")
        print(f"Year: {year}")
        print(f"Location: {location}")
        print(f"Difficulty: {difficulty}")
        print(f"Magic: {'Enabled' if magic_enabled else 'Disabled'}")
        print(f"Matrix: {'Enabled' if matrix_enabled else 'Disabled'}")
        print("-" * 60)
        
        return self.world_data
    
    def save_world(self, world_data, filename=None):
        """Save world data to JSON file"""
        if not os.path.exists('saves'):
            os.makedirs('saves')
        
        if filename is None:
            filename = f"saves/{world_data['name'].replace(' ', '_')}.json"
        
        with open(filename, 'w') as f:
            json.dump(world_data, f, indent=2)
        
        print(f"\nWorld saved to {filename}")
        return filename
    
    def load_world(self, filename):
        """Load world data from JSON file"""
        with open(filename, 'r') as f:
            self.world_data = json.load(f)
        return self.world_data
    
    def list_saved_worlds(self):
        """List all saved worlds"""
        if not os.path.exists('saves'):
            return []
        
        world_files = [f for f in os.listdir('saves') if f.endswith('.json')]
        return world_files
