# Shadowrun CDDA - Isometric Grid Game

A CDDA (Cataclysm: Dark Days Ahead) meets Shadowrun game combining CLI character/world creation with an isometric grid game perspective.

## Description

This project combines the deep character and world creation systems with survival mechanics of CDDA and the cyberpunk-fantasy setting of Shadowrun, rendered in a classic isometric grid view. Navigate a dystopian world where magic and technology collide, create detailed characters and worlds, then explore them in isometric glory.

## Features

### Character & World Creation System (CLI)
- **World Creation**: Create custom Shadowrun game worlds with configurable settings:
  - Timeline selection (2050s, 2070s, 2080s, or custom)
  - Location settings (Seattle, Neo-Tokyo, Berlin, Hong Kong, or custom)
  - Difficulty levels (Street Level, Professional, Elite)
  - Toggle magic and matrix capabilities
  
- **Character Creation**: Design your shadowrunner with:
  - Multiple metatypes (Human, Elf, Dwarf, Ork, Troll)
  - Seven archetypes (Street Samurai, Decker, Mage, Shaman, Rigger, Face, Adept)
  - Attribute point allocation system (30 points across 8 attributes)
  - Skill selection (choose 3 primary skills)
  - Background customization

- **Save/Load System**: Persist worlds and characters to JSON files

### Isometric Game Engine
- **Isometric Grid Rendering**: Classic 2.5D isometric perspective
- **Shadowrun-Inspired Character System**: Character attributes including Body, Agility, Reaction, Strength, Willpower, Logic, Intuition, and Charisma
- **Grid-Based Movement**: Navigate through an isometric world with keyboard controls
- **Modular Architecture**: Easy to extend with new features, items, and mechanics

## Installation

### Requirements

- Python 3.7 or higher
- Pygame 2.5.0 or higher (for isometric game only, optional for CLI)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/xenkoaki-png/Shadowrun-.git
cd Shadowrun-
```

2. Install dependencies (optional for CLI, required for isometric game):
```bash
pip install -r requirements.txt
```

## Running the Game

### CLI Character & World Creation

To start the CLI interface for creating and managing worlds and characters:

```bash
python3 shadowrun.py
```

### Isometric Game

To start the isometric grid game:

```bash
python main.py
```

## CLI Usage

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

## Isometric Game Controls

- **Arrow Keys / WASD**: Move in cardinal directions (up, down, left, right)
- **Q**: Move diagonally up-left
- **E**: Move diagonally up-right
- **Z**: Move diagonally down-left
- **C**: Move diagonally down-right
- **ESC**: Quit game

## Project Structure

```
Shadowrun-/
├── main.py                 # Isometric game entry point
├── shadowrun.py           # CLI entry point
├── startup_screen.py      # CLI main menu and UI
├── world_creator.py       # World creation logic
├── character_creator.py   # Character creation logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── src/                  # Isometric game modules
│   ├── __init__.py        # Package initialization
│   ├── game.py            # Main game loop and state management
│   ├── isometric_renderer.py  # Isometric rendering engine
│   ├── world.py           # World and tile management
│   ├── player.py          # Player character
│   └── input_handler.py   # Input processing
└── saves/                # Saved world files (created on first save)
```

## Game Mechanics

### Character System (Shadowrun-Inspired)

Each character has attributes that affect gameplay:
- **Body**: Physical health and resistance
- **Agility**: Movement and physical finesse
- **Reaction**: Speed and reflexes
- **Strength**: Physical power
- **Willpower**: Mental fortitude
- **Logic**: Reasoning and technical skills
- **Intuition**: Perception and instinct
- **Charisma**: Social influence

### World

The game world is represented as an isometric grid where each tile can be:
- **Floor**: Walkable terrain
- **Wall**: Impassable obstacles
- Different tile types can be added for varied gameplay

## Development

### Adding New Features

The modular architecture makes it easy to extend:

1. **New Tile Types**: Add to `world.py`
2. **New Entities**: Create classes similar to `player.py`
3. **New Mechanics**: Extend the `game.py` update loop
4. **Graphics**: Modify `isometric_renderer.py`

### Future Plans

- [x] CLI Character and world creation
- [x] Save/load system
- [x] Isometric grid rendering
- [ ] Integration between CLI and isometric game (load created characters into game)
- [ ] Item system and inventory management
- [ ] NPC characters and AI
- [ ] Combat system (ranged and melee)
- [ ] Hacking mechanics
- [ ] Magic system
- [ ] Crafting and scavenging
- [ ] Procedural world generation
- [ ] More complex terrain types
- [ ] Sprite graphics and animations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational and personal use.

## Credits

Inspired by:
- Cataclysm: Dark Days Ahead (CDDA)
- Shadowrun tabletop RPG
- Classic isometric games
