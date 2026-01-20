# Shadowrun CDDA - Isometric Grid Game

A CDDA (Cataclysm: Dark Days Ahead) meets Shadowrun game with an isometric grid perspective.

## Description

This project combines the deep survival mechanics and item management of CDDA with the cyberpunk-fantasy setting of Shadowrun, all rendered in a classic isometric grid view. Navigate a dystopian world where magic and technology collide, scavenge for resources, and survive in the shadows.

## Features

- **Isometric Grid Rendering**: Classic 2.5D isometric perspective
- **Shadowrun-Inspired Character System**: Character attributes including Body, Agility, Reaction, Strength, Willpower, Logic, Intuition, and Charisma
- **Grid-Based Movement**: Navigate through an isometric world with keyboard controls
- **Modular Architecture**: Easy to extend with new features, items, and mechanics

## Installation

### Requirements

- Python 3.7 or higher
- Pygame 2.5.0 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/xenkoaki-png/Shadowrun-.git
cd Shadowrun-
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

To start the game, run:

```bash
python main.py
```

## Controls

- **Arrow Keys / WASD**: Move in cardinal directions
- **Q/E/Z/C**: Diagonal movement
- **ESC**: Quit game

## Project Structure

```
Shadowrun-/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── src/
    ├── __init__.py        # Package initialization
    ├── game.py            # Main game loop and state management
    ├── isometric_renderer.py  # Isometric rendering engine
    ├── world.py           # World and tile management
    ├── player.py          # Player character
    └── input_handler.py   # Input processing
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

- [ ] Item system and inventory management
- [ ] NPC characters and AI
- [ ] Combat system (ranged and melee)
- [ ] Hacking mechanics
- [ ] Magic system
- [ ] Crafting and scavenging
- [ ] Procedural world generation
- [ ] Save/load system
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