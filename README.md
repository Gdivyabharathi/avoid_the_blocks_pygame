# my-second-project
# Simple Pygame Cube Game

This is a simple game built using Pygame where you control a cube that moves within a 400x400 window. Avoid colliding with the moving obstacle!

## Features

- Control the cube using the arrow keys.
- The game detects collisions with the moving wall.
- A "Game Over" message is displayed when a collision is detected.

## How to Run

1. **Install Dependencies:**

   Make sure you have Python and Pygame installed. You can install Pygame using the following command:


2. **Run the Game:**

Execute the script using Python:


## Controls

- **Left Arrow Key:** Move cube left
- **Right Arrow Key:** Move cube right
- **Up Arrow Key:** Move cube up
- **Down Arrow Key:** Move cube down
- **Enter Key:** Restart the game after Game Over

## Code Overview

The game consists of a main loop that handles events, updates the game state, and renders the graphics.

### Key Components

- **Cube:** The player-controlled cube that moves based on arrow key inputs.
- **Obstacle:** A moving wall that travels from right to left. The player must avoid colliding with it.
- **Game Over:** A state that occurs when the cube collides with the wall. The screen displays a "Game Over" message.

## Future Enhancements

- Add sound effects and background music.
- Implement a scoring system.
- Add more complex obstacles.

## Contributing

Feel free to fork this repository, submit issues, or make pull requests with enhancements!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
