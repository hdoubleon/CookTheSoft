# 🐢 Turtle Runaway Game

## Overview

A fun interactive game where a red turtle (chaser) tries to catch a blue turtle (runner) within a time limit. The blue turtle moves automatically with random AI, while the red turtle is controlled by the player using keyboard inputs.

## Game Features

### 🎮 Core Gameplay

- **Red Turtle (Chaser)**: Player-controlled using arrow keys
- **Blue Turtle (Runner)**: AI-controlled with random movement
- **Objective**: Catch the runner before time runs out!

### ⏰ Timer System

- **30-second time limit**
- **Real-time countdown** displayed on screen
- **Dynamic speed**: Game gets faster as time progresses
- **Score system**: Points based on survival time (10 points per second)

### 🎯 Collision Detection

- **Precise collision**: Turtles must be within 10 pixels to be "caught"
- **Real-time distance** shown on screen
- **Visual feedback** with game over messages

### 🔄 Game Controls

- **Arrow Keys**: Control the red turtle
  - ⬆️ Up: Move forward
  - ⬇️ Down: Move backward
  - ⬅️ Left: Turn left
  - ➡️ Right: Turn right
- **R Key**: Restart the game after game over

## Technical Implementation

### 📁 File Structure

```
turtle_runaway_skeleton.py
├── RunawayGame class        # Main game logic
├── ManualMover class        # Player-controlled turtle
├── RandomMover class        # AI-controlled turtle
└── Main execution block     # Game initialization
```

### 🏗️ Class Architecture

#### `RunawayGame` Class

- **Purpose**: Manages overall game state and logic
- **Key Methods**:
  - `__init__()`: Initialize game components
  - `start()`: Begin the game
  - `step()`: Main game loop (called every 100ms)
  - `is_catched()`: Check collision between turtles
  - `game_over()`: Handle game termination
  - `restart_game()`: Reset game state

#### `ManualMover` Class

- **Purpose**: Player-controlled turtle
- **Features**:
  - Keyboard event handlers
  - Movement and rotation controls
  - Empty `run_ai()` method (no automatic movement)

#### `RandomMover` Class

- **Purpose**: AI-controlled turtle
- **Features**:
  - Random movement algorithm
  - Three possible actions per step:
    - Move forward
    - Turn left
    - Turn right

### ⚙️ Game Loop Mechanism

```python
# Timer-based game loop
self.canvas.ontimer(self.step, self.ai_timer_msec)

def step(self):
    # 1. Check game over conditions
    # 2. Update timers and scores
    # 3. Move turtles (AI + player input)
    # 4. Check collisions
    # 5. Update display
    # 6. Schedule next step
```

## Game Rules

### 🏆 Victory Conditions

1. **Chaser Wins**: Red turtle catches blue turtle (distance ≤ 10 pixels)
2. **Runner Wins**: Blue turtle survives for 30 seconds

### 📊 Scoring System

- **Base Score**: 10 points per second survived
- **Final Score**: Displayed when game ends
- **High Score**: Try to beat your previous record!

### 🚀 Difficulty Progression

- **Initial Speed**: 100ms per game step
- **Maximum Speed**: 50ms per game step (after ~25 seconds)
- **Speed Formula**: `max(50, 100 - elapsed_time * 2)`

## Installation & Usage

### Prerequisites

```bash
# Required Python packages
import tkinter as tk
import turtle
import random
import time
```

### Running the Game

```bash
# Method 1: Direct execution
python3 turtle_runaway_skeleton.py

# Method 2: In Spyder IDE
!python turtle_runaway_skeleton.py
```

### 🎮 How to Play

1. **Start**: Run the Python script
2. **Control**: Use arrow keys to move the red turtle
3. **Objective**: Catch the blue turtle before time runs out
4. **Restart**: Press 'R' after game over
5. **Exit**: Close the game window

## Code Customization

### 🔧 Adjustable Parameters

#### Game Timing

```python
self.game_time_limit = 30        # Change time limit (seconds)
ai_timer_msec = 100             # Change game speed (milliseconds)
```

#### Movement Settings

```python
step_move = 10                  # Movement distance per step
step_turn = 10                  # Rotation angle per turn
```

#### Collision Detection

```python
catch_radius = 15               # Distance for collision detection
turtle_size = 10               # Turtle size for precise collision
```

### 🎨 Visual Customization

```python
# Turtle colors
self.runner.color("blue")       # Change runner color
self.chaser.color("red")        # Change chaser color

# Canvas settings
canvas = tk.Canvas(root, width=700, height=700, bg="white")
screen.bgcolor("lightgray")
```

## Advanced Features

### 🤖 AI Improvement Ideas

- **Smart AI**: Make the runner avoid the chaser
- **Pathfinding**: Implement A\* algorithm for chaser
- **Difficulty levels**: Different AI behaviors

### 🎮 Game Enhancements

- **Power-ups**: Speed boost, invisibility
- **Obstacles**: Add walls or barriers
- **Multiplayer**: Two-player mode
- **Sound effects**: Add audio feedback

### 📈 Statistics

- **Game history**: Track multiple game sessions
- **Performance metrics**: Average survival time
- **Leaderboards**: High score tracking

## Troubleshooting

### Common Issues

#### Game Window Not Showing

```bash
# Try using system Python instead of virtual environment
python3 turtle_runaway_skeleton.py

# Or run in IDE like Spyder, PyCharm, or VS Code
```

#### Turtles Not Visible

- Check if turtles are positioned within canvas bounds
- Verify turtle colors contrast with background
- Ensure `showturtle()` is called

#### Controls Not Working

- Click on the game window to focus
- Check if `canvas.listen()` is called
- Verify key binding syntax

### Performance Optimization

- Reduce timer frequency for slower computers
- Adjust canvas size for better performance
- Use `speed(0)` for fastest turtle animation

## Development Notes

### 📝 Code Quality

- **Comments**: All functions documented in English
- **Error Handling**: Basic exception management
- **Modularity**: Clean class-based architecture
- **Readability**: Clear variable and function names

### 🧪 Testing Recommendations

- Test on different screen sizes
- Verify keyboard responsiveness
- Check timer accuracy
- Validate collision detection

### 🔮 Future Improvements

- Add configuration file support
- Implement save/load game state
- Create tutorial mode
- Add animation effects

---

## 📞 Support

For questions or improvements, check the code comments or modify the parameters to suit your preferences!

**Happy Gaming!** 🎮🐢
