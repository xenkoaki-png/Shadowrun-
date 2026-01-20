"""
Startup Screen Module for Shadowrun
Main menu and navigation for the game
"""

import os
import sys
from world_creator import WorldCreator
from character_creator import CharacterCreator


class StartupScreen:
    """Main startup screen for Shadowrun game"""
    
    def __init__(self):
        self.world_creator = WorldCreator()
        self.character_creator = CharacterCreator()
        self.current_world = None
        
    def clear_screen(self):
        """Clear the console screen"""
        # Using print with newlines is safer than os.system
        print('\n' * 100)
        
    def display_banner(self):
        """Display the game banner"""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗      ║
║   ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║      ║
║   ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║      ║
║   ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║      ║
║   ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝      ║
║   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝       ║
║                                                              ║
║              R  U  N  N  E  R     S  Y  S  T  E  M          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def display_main_menu(self):
        """Display main menu options"""
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print("1. Create New World")
        print("2. Load Existing World")
        print("3. Create New Character")
        print("4. View Current World")
        print("5. View Characters in World")
        print("6. Exit")
        print("=" * 60)
        
    def create_new_world(self):
        """Handle world creation"""
        self.current_world = self.world_creator.create_world()
        
        # Ask if user wants to save
        save_choice = input("\nSave this world? (y/n): ").strip().lower()
        if save_choice == 'y':
            self.world_creator.save_world(self.current_world)
        
        input("\nPress Enter to continue...")
        
    def load_existing_world(self):
        """Handle loading existing world"""
        saved_worlds = self.world_creator.list_saved_worlds()
        
        if not saved_worlds:
            print("\nNo saved worlds found.")
            input("Press Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print("SAVED WORLDS")
        print("=" * 60)
        for i, world_file in enumerate(saved_worlds, 1):
            print(f"{i}. {world_file}")
        print("=" * 60)
        
        try:
            choice = int(input("\nSelect world to load (0 to cancel): ").strip())
            if choice == 0:
                return
            if 1 <= choice <= len(saved_worlds):
                world_file = saved_worlds[choice - 1]
                self.current_world = self.world_creator.load_world(f"saves/{world_file}")
                print(f"\nWorld '{self.current_world['name']}' loaded successfully!")
            else:
                print("\nInvalid choice.")
        except (ValueError, FileNotFoundError) as e:
            print(f"\nError loading world: {e}")
        
        input("\nPress Enter to continue...")
        
    def create_new_character(self):
        """Handle character creation"""
        if self.current_world is None:
            print("\nPlease create or load a world first!")
            input("Press Enter to continue...")
            return
        
        character = self.character_creator.create_character()
        
        # Add character to current world
        self.current_world['characters'].append(character)
        
        # Ask if user wants to save the world with new character
        save_choice = input("\nSave character to world? (y/n): ").strip().lower()
        if save_choice == 'y':
            self.world_creator.save_world(self.current_world)
        
        input("\nPress Enter to continue...")
        
    def view_current_world(self):
        """Display current world information"""
        if self.current_world is None:
            print("\nNo world currently loaded.")
            input("Press Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print(f"WORLD: {self.current_world['name']}")
        print("=" * 60)
        print(f"Year: {self.current_world['year']}")
        print(f"Location: {self.current_world['location']}")
        print(f"Difficulty: {self.current_world['difficulty']}")
        print(f"Magic: {'Enabled' if self.current_world['magic_enabled'] else 'Disabled'}")
        print(f"Matrix: {'Enabled' if self.current_world['matrix_enabled'] else 'Disabled'}")
        print(f"Characters: {len(self.current_world['characters'])}")
        print("=" * 60)
        
        input("\nPress Enter to continue...")
        
    def view_characters(self):
        """Display all characters in current world"""
        if self.current_world is None:
            print("\nNo world currently loaded.")
            input("Press Enter to continue...")
            return
        
        characters = self.current_world.get('characters', [])
        
        if not characters:
            print("\nNo characters in this world yet.")
            input("Press Enter to continue...")
            return
        
        print("\n" + "=" * 60)
        print(f"CHARACTERS IN {self.current_world['name']}")
        print("=" * 60)
        
        for i, char in enumerate(characters, 1):
            print(f"\n{i}. {char['name']}")
            print(f"   Metatype: {char['metatype']}")
            print(f"   Archetype: {char['archetype']}")
        
        print("\n" + "=" * 60)
        
        # Option to view detailed character info
        choice = input("\nEnter character number to view details (0 to go back): ").strip()
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(characters):
                self.character_creator.display_character(characters[choice - 1])
        except ValueError:
            pass
        
        input("\nPress Enter to continue...")
        
    def run(self):
        """Main application loop"""
        while True:
            self.clear_screen()
            self.display_banner()
            self.display_main_menu()
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.create_new_world()
            elif choice == '2':
                self.load_existing_world()
            elif choice == '3':
                self.create_new_character()
            elif choice == '4':
                self.view_current_world()
            elif choice == '5':
                self.view_characters()
            elif choice == '6':
                print("\nThanks for playing Shadowrun!")
                print("Stay in the shadows, chummer...")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")
