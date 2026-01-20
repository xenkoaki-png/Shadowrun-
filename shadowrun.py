#!/usr/bin/env python3
"""
Shadowrun Startup Screen
Main entry point for the Shadowrun game with world and character creation
"""

import sys
from startup_screen import StartupScreen


def main():
    """Main entry point for the Shadowrun application"""
    startup = StartupScreen()
    startup.run()


if __name__ == "__main__":
    main()
