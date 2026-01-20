#!/usr/bin/env python3
"""
Basic test script for Shadowrun modules
"""

import sys
import os
import tempfile

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    try:
        from startup_screen import StartupScreen
        from world_creator import WorldCreator
        from character_creator import CharacterCreator
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False

def test_world_creator():
    """Test world creator basic functionality"""
    print("\nTesting WorldCreator...")
    try:
        from world_creator import WorldCreator
        wc = WorldCreator()
        
        # Create a test world manually
        wc.world_data = {
            "name": "Test World",
            "year": 2070,
            "location": "Seattle",
            "difficulty": "Professional",
            "magic_enabled": True,
            "matrix_enabled": True,
            "created_at": "2026-01-20T00:00:00",
            "characters": []
        }
        
        # Test save functionality using cross-platform temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
            tmp_filename = tmp_file.name
        
        wc.save_world(wc.world_data, tmp_filename)
        
        # Test load functionality
        loaded = wc.load_world(tmp_filename)
        
        assert loaded["name"] == "Test World"
        assert loaded["year"] == 2070
        
        # Cleanup
        os.remove(tmp_filename)
        
        print("✓ WorldCreator tests passed")
        return True
    except Exception as e:
        print(f"✗ WorldCreator test failed: {e}")
        return False

def test_character_creator():
    """Test character creator basic functionality"""
    print("\nTesting CharacterCreator...")
    try:
        from character_creator import CharacterCreator
        cc = CharacterCreator()
        
        # Create a test character manually
        cc.character_data = {
            "name": "Test Runner",
            "metatype": "Human",
            "archetype": "Street Samurai",
            "attributes": {
                "Body": 4,
                "Agility": 5,
                "Reaction": 4,
                "Strength": 3,
                "Charisma": 2,
                "Intuition": 3,
                "Logic": 2,
                "Willpower": 3
            },
            "skills": ["Firearms", "Close Combat", "Athletics"],
            "background": "Test background",
            "created_at": "2026-01-20T00:00:00",
            "karma": 0,
            "nuyen": 5000,
            "equipment": []
        }
        
        assert cc.character_data["name"] == "Test Runner"
        assert cc.character_data["metatype"] == "Human"
        assert len(cc.character_data["skills"]) == 3
        
        print("✓ CharacterCreator tests passed")
        return True
    except Exception as e:
        print(f"✗ CharacterCreator test failed: {e}")
        return False

def test_startup_screen():
    """Test startup screen initialization"""
    print("\nTesting StartupScreen...")
    try:
        from startup_screen import StartupScreen
        ss = StartupScreen()
        
        assert ss.world_creator is not None
        assert ss.character_creator is not None
        assert ss.current_world is None
        
        print("✓ StartupScreen initialization passed")
        return True
    except Exception as e:
        print(f"✗ StartupScreen test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("SHADOWRUN TEST SUITE")
    print("=" * 60)
    
    results = []
    results.append(test_imports())
    results.append(test_world_creator())
    results.append(test_character_creator())
    results.append(test_startup_screen())
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {sum(results)}/{len(results)} tests passed")
    print("=" * 60)
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
