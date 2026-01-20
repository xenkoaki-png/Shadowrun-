#!/usr/bin/env python3
"""
Demo script to showcase Shadowrun startup screen functionality
Creates a sample world and character automatically
"""

import os
from world_creator import WorldCreator
from character_creator import CharacterCreator

def demo_world_creation():
    """Demonstrate world creation"""
    print("\n" + "=" * 60)
    print("DEMO: Creating a Sample World")
    print("=" * 60)
    
    wc = WorldCreator()
    
    # Create a sample world
    sample_world = {
        "name": "Neo-Seattle 2075",
        "year": 2075,
        "location": "Seattle",
        "difficulty": "Professional",
        "magic_enabled": True,
        "matrix_enabled": True,
        "created_at": "2026-01-20T00:00:00",
        "characters": []
    }
    
    wc.world_data = sample_world
    
    print(f"\n✓ Created world: {sample_world['name']}")
    print(f"  Year: {sample_world['year']}")
    print(f"  Location: {sample_world['location']}")
    print(f"  Difficulty: {sample_world['difficulty']}")
    print(f"  Magic: {'Enabled' if sample_world['magic_enabled'] else 'Disabled'}")
    print(f"  Matrix: {'Enabled' if sample_world['matrix_enabled'] else 'Disabled'}")
    
    return wc, sample_world

def demo_character_creation():
    """Demonstrate character creation"""
    print("\n" + "=" * 60)
    print("DEMO: Creating Sample Characters")
    print("=" * 60)
    
    cc = CharacterCreator()
    
    # Create sample characters
    characters = [
        {
            "name": "Razor",
            "metatype": "Elf",
            "archetype": "Street Samurai",
            "attributes": {
                "Body": 4,
                "Agility": 6,
                "Reaction": 5,
                "Strength": 3,
                "Charisma": 3,
                "Intuition": 4,
                "Logic": 2,
                "Willpower": 3
            },
            "skills": ["Firearms", "Close Combat", "Stealth"],
            "background": "Former corporate security turned shadowrunner",
            "created_at": "2026-01-20T00:00:00",
            "karma": 0,
            "nuyen": 5000,
            "equipment": []
        },
        {
            "name": "Zero Cool",
            "metatype": "Human",
            "archetype": "Decker",
            "attributes": {
                "Body": 2,
                "Agility": 3,
                "Reaction": 4,
                "Strength": 2,
                "Charisma": 3,
                "Intuition": 5,
                "Logic": 6,
                "Willpower": 5
            },
            "skills": ["Hacking", "Electronics", "Software"],
            "background": "Elite matrix specialist with a mysterious past",
            "created_at": "2026-01-20T00:00:00",
            "karma": 0,
            "nuyen": 5000,
            "equipment": []
        },
        {
            "name": "Mystic",
            "metatype": "Elf",
            "archetype": "Mage",
            "attributes": {
                "Body": 2,
                "Agility": 3,
                "Reaction": 4,
                "Strength": 2,
                "Charisma": 4,
                "Intuition": 5,
                "Logic": 5,
                "Willpower": 6
            },
            "skills": ["Sorcery", "Conjuring", "Astral Combat"],
            "background": "Awakened mage seeking ancient magical artifacts",
            "created_at": "2026-01-20T00:00:00",
            "karma": 0,
            "nuyen": 5000,
            "equipment": []
        }
    ]
    
    for char in characters:
        print(f"\n✓ Created character: {char['name']}")
        print(f"  Metatype: {char['metatype']}")
        print(f"  Archetype: {char['archetype']}")
        print(f"  Skills: {', '.join(char['skills'])}")
    
    return characters

def main():
    """Run the demo"""
    print("\n")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                  SHADOWRUN RUNNER SYSTEM                     ║")
    print("║                     FEATURE DEMONSTRATION                    ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    
    # Demo world creation
    wc, world = demo_world_creation()
    
    # Demo character creation
    characters = demo_character_creation()
    
    # Add characters to world
    world['characters'] = characters
    
    # Save the demo world
    print("\n" + "=" * 60)
    print("DEMO: Saving World with Characters")
    print("=" * 60)
    
    filename = wc.save_world(world)
    print(f"\n✓ World saved successfully to {filename}")
    print(f"  Total characters: {len(characters)}")
    
    # Display summary
    print("\n" + "=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print("\nYou can now:")
    print("1. Run 'python3 shadowrun.py' to start the interactive application")
    print("2. Load the 'Neo-Seattle 2075' world from the main menu")
    print("3. View the sample characters")
    print("4. Create your own worlds and characters!")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
