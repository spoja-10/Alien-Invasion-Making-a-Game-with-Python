# Alien Invasion

A classic 2D retro arcade shooter game built with Python and Pygame.

## Description
In Alien Invasion, the player controls a rocket ship that appears at the bottom of the screen. The player can move the ship right and left and shoot bullets to destroy a fleet of aliens moving down the screen. The game tracks the player's score, high score, and level. As the player advances, the game becomes more challenging with faster enemies.

## Features
- **Player Ship**: Move left and right to dodge and position for attacks.
- **Alien Fleet**: A grid of enemies that move and drop down.
- **Shooting Mechanism**: Fire bullets to destroy aliens.
- **Scoring System**: Points are awarded for every alien destroyed.
- **High Score**: The game tracks the highest score achieved in the session.
- **Dynamic Difficulty**: The fleet moves faster as you level up.
- **Game Stats**: Tracks lives (3 ships per game) and current level.
- **Play Button**: Interface to start and restart the game.

## Requirements
- Python 3.x
- Pygame

## Installation
1.  **Clone or Download** the repository.
2.  **Install Pygame**:
    ```bash
    pip install pygame
    ```
    *Note: If you have multiple Python versions or are on Windows, you might need to use:*
    ```bash
    python -m pip install pygame
    ```
    *or*
    ```powershell
    & "Path\To\Python.exe" -m pip install pygame
    ```

## How to Play
1.  Run the game script:
    ```bash
    python alien_invasion.py
    ```
2.  Click the **Play** button to start.

### Controls
| Key | Action |
| :--- | :--- |
| **Right Arrow** | Move Ship Right |
| **Left Arrow** | Move Ship Left |
| **Spacebar** | Fire Bullet |
| **Q** | Quit Game |

## Project Structure
- `alien_invasion.py`: Main game file.
- `settings.py`: Configuration for game settings (speed, dimensions, etc.).
- `ship.py`: Class defining the player's ship.
- `alien.py`: Class defining the alien enemies.
- `bullets.py`: Class defining the projectiles.
- `game_stats.py`: Tracks game statistics (score, level, lives).
- `scoreboard.py`: Handles drawing the score and level to the screen.
- `button.py`: UI element for the Play button.

## Future Improvements
- Sound effects (Laser, Explosion, Game Over).
- Persistent High Score (Save to file).
- Aliens shooting back.