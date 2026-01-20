#!/usr/bin/env python3
"""
Integrated Game - Load CLI characters into isometric game
Combines the CLI character/world system with the isometric game engine
"""

import sys
import os
import json
from world_creator import WorldCreator
from src.game import Game
from src.player import Player


def list_saved_characters():
    """List all available characters from saved worlds"""
    wc = WorldCreator()
    saved_worlds = wc.list_saved_worlds()
    
    if not saved_worlds:
        return []
    
    all_characters = []
    for world_file in saved_worlds:
        try:
            world = wc.load_world(f"saves/{world_file}")
            for char in world.get('characters', []):
                char['world_file'] = world_file
                char['world_name'] = world['name']
                all_characters.append(char)
        except (FileNotFoundError, ValueError, IOError, KeyError) as e:
            # Skip worlds that can't be loaded
            print(f"Warning: Could not load {world_file}: {e}")
            continue
    
    return all_characters


def load_character_into_player(char_data, player):
    """Load CLI character data into isometric game player"""
    player.name = char_data.get('name', 'Runner')
    player.nuyen = char_data.get('nuyen', 5000)
    
    # Map attributes (CLI uses capitalized names, game uses lowercase)
    attrs = char_data.get('attributes', {})
    player.body = attrs.get('Body', 3)
    player.agility = attrs.get('Agility', 3)
    player.reaction = attrs.get('Reaction', 3)
    player.strength = attrs.get('Strength', 3)
    player.willpower = attrs.get('Willpower', 3)
    player.logic = attrs.get('Logic', 3)
    player.intuition = attrs.get('Intuition', 3)
    player.charisma = attrs.get('Charisma', 3)
    
    # Calculate health based on Body attribute
    player.max_health = 100 + (player.body * 10)
    player.health = player.max_health
    
    # Map skills
    skills = char_data.get('skills', [])
    skill_mapping = {
        'Firearms': 'firearms',
        'Close Combat': 'close_combat',
        'Athletics': 'athletics',
        'Stealth': 'stealth',
        'Hacking': 'hacking',
        'Electronics': 'electronics'
    }
    
    for skill_name in skills:
        game_skill = skill_mapping.get(skill_name)
        if game_skill:
            player.skills[game_skill] = 3  # Set to competent level


def main():
    """Main function - select character and start game"""
    print("\n" + "=" * 60)
    print("SHADOWRUN INTEGRATED GAME")
    print("=" * 60)
    print("\nLoad a character from your saved worlds to play in the")
    print("isometric game, or play with a default character.\n")
    
    characters = list_saved_characters()
    
    if not characters:
        print("No saved characters found. Starting with default character.")
        print("\nTip: Create characters using 'python3 shadowrun.py'")
        input("\nPress Enter to continue...")
    else:
        print("Available Characters:")
        print("-" * 60)
        for i, char in enumerate(characters, 1):
            print(f"{i}. {char['name']} ({char['metatype']} {char['archetype']})")
            print(f"   World: {char['world_name']}")
        print(f"{len(characters) + 1}. Play with default character")
        print("-" * 60)
        
        try:
            choice = int(input("\nSelect character (1-{}): ".format(len(characters) + 1)).strip())
            if 1 <= choice <= len(characters):
                selected_char = characters[choice - 1]
                print(f"\nLoading {selected_char['name']}...")
                
                # Create and configure player
                import pygame
                pygame.init()
                game = Game()
                load_character_into_player(selected_char, game.player)
                
                print(f"✓ Character loaded successfully!")
                print(f"  Name: {game.player.name}")
                print(f"  Health: {game.player.health}/{game.player.max_health}")
                print(f"  Nuyen: {game.player.nuyen}")
                print(f"  Stats: Body {game.player.body}, Agility {game.player.agility}")
                
                input("\nPress Enter to start game...")
                game.run()
                return
        except (ValueError, IndexError):
            print("\nInvalid choice. Starting with default character.")
            input("Press Enter to continue...")
    
    # Start with default character
    import pygame
    pygame.init()
    game = Game()
    print(f"\nStarting game with default character: {game.player.name}")
    input("Press Enter to start...")
    game.run()


if __name__ == "__main__":
    main()
