# Shadowrun Runner System

A command-line interface application for managing Shadowrun game worlds and characters.

## Features

- **World Creation**: Create custom Shadowrun game worlds with configurable settings:
  - Timeline selection (2050s, 2070s, 2080s, or custom)
  - Location settings (Seattle, Neo-Tokyo, Berlin, Hong Kong, or custom)
  - Difficulty levels (Street Level, Professional, Elite)
  - Toggle magic and matrix capabilities
  
- **Character Creation**: Design your shadowrunner with:
  - Multiple metatypes (Human, Elf, Dwarf, Ork, Troll)
  - Seven archetypes (Street Samurai, Decker, Mage, Shaman, Rigger, Face, Adept)
  - Attribute point allocation system
  - Skill selection
  - Background customization

- **Save/Load System**: Persist worlds and characters to JSON files

## Installation

### Requirements
- Python 3.6 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/xenkoaki-png/Shadowrun-.git
cd Shadowrun-

# Run the application (no additional dependencies needed)
python3 shadowrun.py
```

## Usage

1. **Start the Application**:
   ```bash
   python3 shadowrun.py
   ```

2. **Create a World**:
   - Select option 1 from the main menu
   - Follow the prompts to configure your world
   - Choose to save the world when prompted

3. **Create Characters**:
   - Load or create a world first
   - Select option 3 from the main menu
   - Follow the character creation prompts
   - Save characters to the world

4. **View and Manage**:
   - Option 4: View current world details
   - Option 5: View all characters in the world

## File Structure

```
Shadowrun-/
├── shadowrun.py           # Main entry point
├── startup_screen.py      # Main menu and UI
├── world_creator.py       # World creation logic
├── character_creator.py   # Character creation logic
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
└── saves/                # Saved world files (created on first save)
```

## Save Files

World data is saved as JSON files in the `saves/` directory. Each world file contains:
- World configuration
- All characters associated with that world

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for use in your Shadowrun campaigns.