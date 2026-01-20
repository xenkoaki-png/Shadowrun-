"""
Character Creation Module for Shadowrun
Handles creation and management of player characters
"""

from datetime import datetime


class CharacterCreator:
    """Handles creation of Shadowrun characters"""
    
    def __init__(self):
        self.character_data = {}
        
    def create_character(self):
        """Interactive character creation process"""
        print("\n" + "=" * 60)
        print("CHARACTER CREATION")
        print("=" * 60)
        
        # Character name
        char_name = input("\nEnter character name: ").strip()
        if not char_name:
            char_name = f"Shadowrunner_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Metatype selection
        print("\nSelect Metatype:")
        print("1. Human")
        print("2. Elf")
        print("3. Dwarf")
        print("4. Ork")
        print("5. Troll")
        
        metatype_choice = input("\nSelect metatype (1-5): ").strip()
        metatype_map = {
            "1": "Human",
            "2": "Elf",
            "3": "Dwarf",
            "4": "Ork",
            "5": "Troll"
        }
        metatype = metatype_map.get(metatype_choice, "Human")
        
        # Archetype selection
        print("\nSelect Archetype:")
        print("1. Street Samurai (Combat specialist)")
        print("2. Decker (Matrix specialist)")
        print("3. Mage (Magic user)")
        print("4. Shaman (Nature magic)")
        print("5. Rigger (Drone/vehicle specialist)")
        print("6. Face (Social specialist)")
        print("7. Adept (Physical magic)")
        
        archetype_choice = input("\nSelect archetype (1-7): ").strip()
        archetype_map = {
            "1": "Street Samurai",
            "2": "Decker",
            "3": "Mage",
            "4": "Shaman",
            "5": "Rigger",
            "6": "Face",
            "7": "Adept"
        }
        archetype = archetype_map.get(archetype_choice, "Street Samurai")
        
        # Attributes (simplified point allocation)
        print("\nAttribute Distribution (30 points total)")
        print("Attributes: Body, Agility, Reaction, Strength, Charisma, Intuition, Logic, Willpower")
        print("Minimum: 1, Maximum: 6 per attribute")
        
        attributes = {}
        attr_names = ["Body", "Agility", "Reaction", "Strength", "Charisma", "Intuition", "Logic", "Willpower"]
        points_remaining = 30
        
        for attr in attr_names:
            while True:
                try:
                    value = input(f"\n{attr} (1-6, {points_remaining} points remaining): ").strip()
                    value = int(value)
                    if 1 <= value <= 6 and value <= points_remaining:
                        attributes[attr] = value
                        points_remaining -= value
                        break
                    else:
                        print(f"Invalid value. Must be 1-6 and you have {points_remaining} points left.")
                except ValueError:
                    print("Please enter a number.")
        
        # Background
        print("\nCharacter Background:")
        background = input("Enter a brief background (optional): ").strip()
        
        # Skills (simplified)
        print("\nPrimary Skills (select 3):")
        skill_list = [
            "Firearms", "Close Combat", "Athletics",
            "Hacking", "Electronics", "Software",
            "Sorcery", "Conjuring", "Astral Combat",
            "Stealth", "Perception", "Negotiation",
            "Driving", "Pilot", "Gunnery"
        ]
        
        for i, skill in enumerate(skill_list, 1):
            print(f"{i}. {skill}")
        
        skills = []
        for i in range(3):
            while True:
                try:
                    choice = input(f"\nSelect skill #{i+1} (1-{len(skill_list)}): ").strip()
                    choice = int(choice) - 1
                    if 0 <= choice < len(skill_list):
                        skill = skill_list[choice]
                        if skill not in skills:
                            skills.append(skill)
                            break
                        else:
                            print("Skill already selected. Choose another.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a number.")
        
        # Create character data structure
        self.character_data = {
            "name": char_name,
            "metatype": metatype,
            "archetype": archetype,
            "attributes": attributes,
            "skills": skills,
            "background": background,
            "created_at": datetime.now().isoformat(),
            "karma": 0,
            "nuyen": 5000,  # Starting money
            "equipment": []
        }
        
        print("\n" + "-" * 60)
        print(f"Character '{char_name}' created successfully!")
        print(f"Metatype: {metatype}")
        print(f"Archetype: {archetype}")
        print(f"Attributes: {attributes}")
        print(f"Skills: {', '.join(skills)}")
        print(f"Starting Nuyen: {self.character_data['nuyen']}")
        print("-" * 60)
        
        return self.character_data
    
    def display_character(self, character_data):
        """Display character information"""
        print("\n" + "=" * 60)
        print(f"CHARACTER: {character_data['name']}")
        print("=" * 60)
        print(f"Metatype: {character_data['metatype']}")
        print(f"Archetype: {character_data['archetype']}")
        print(f"\nAttributes:")
        for attr, value in character_data['attributes'].items():
            print(f"  {attr}: {value}")
        print(f"\nSkills: {', '.join(character_data['skills'])}")
        print(f"\nKarma: {character_data['karma']}")
        print(f"Nuyen: {character_data['nuyen']}¥")
        if character_data['background']:
            print(f"\nBackground: {character_data['background']}")
        print("=" * 60)
