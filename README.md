# Minesweeper-Game-and-Solving-AI
Minesweeper Game with Oppie and Urchie

This Minesweeper game requires the following packages to be installed. Ensure that you have these packages before running the game. Additionally, make sure to organize the game files in a folder named "minesweeper."

Required Packages
* Python: This game is written in Python and requires a Python interpreter. You can download Python from python.org.
* Pygame: The game uses Pygame for graphics and interaction. Install Pygame using the following command:  pip install pygame
* Font Package: The game utilizes a font file for text rendering. Ensure you have the font file in the specified path:
    * Font file: assets/fonts/OpenSans-Regular.ttf
* Images: Place the image files in the following paths:
    * Oppie's icon: 1.png
    * Urchie's icon: 2.png
    * Mine image: assets/images/mine.png
    * Red mine image: assets/images/mine-red.png
    * Flag image: assets/images/flag.png
    * 
How to Run
Navigate to the "minesweeper" folder using the command line and run the following command to start the game: python runner.py - for running Oppie
python runner_algo2.py - for running Urichie



This is a Minesweeper game with two different AI agents, Oppie and Urchie. You can play the game manually or watch the AIs in action. The game provides options to toggle autoplay, make AI moves, reset the game, and show safe and mine cells based on AI inference.

How to Play

Manual Gameplay:
Click a cell to reveal it.
Right-click a cell to mark it as a mine.
Mark all mines successfully to win!
Autoplay:
Toggle autoplay to let the AI play the game automatically.
AI Move:
Click "AI Move" to make the AI agents (Oppie or Urchie) take a move.
Reset:
Click "Reset" to start a new game.
Show Inference:
Toggle "Show Inference" to display cells marked as safe or mines based on AI inference.

Controls:

Left-Click: Reveal a cell or make a user move.
Right-Click: Mark a cell as a mine.

Game Statistics
Wins: Total number of games won.
Losses: Total number of games lost.
Elapsed Time: Time elapsed since the start of the current game.

Instructions
		Play Game:
Click "Play Game" to start playing manually.
		Autoplay:
Toggle "Oppie" or "Urchie" to let the respective AI play the game automatically.
		AI Move:
Click "AI Move" to make an AI move manually.
		Reset:
Click "Reset" to start a new game.
		Show Inference:
Toggle "Show Inference" to display AI inference on the game board.
		Win/Loss:
Check if you win or lose based on the displayed text.

Game Status
Lost: Indicates that you lost the game. The mine that caused the loss is highlighted.
Won: Indicates that you won the game by correctly marking all mines.

Game Limit
The game will automatically exit after reaching 1000 completed games.
Check the total wins, losses, and games played upon exit.

Enjoy the Game!
Feel free to explore different strategies, watch the AIs play, and enjoy the classic Minesweeper experience with Oppie and Urchie!


------------------------------------------------------------------------------------------------
Minesweeper Game

This is a Minesweeper game implemented in Python using the Tkinter library. The game provides a graphical user interface for the classic Minesweeper puzzle, where players uncover tiles on a grid to avoid hidden bombs.

Features
* Classic Minesweeper Gameplay: Uncover tiles and avoid hidden bombs.
* Customizable Grid Size: Choose the number of rows and columns for the game grid.
* Flagging System: Flag tiles suspected of containing bombs.
* Recursive Tile Uncovering: Click on an empty tile to uncover neighboring tiles recursively.
* Spiral Sweep Algorithm: An intelligent algorithm to automatically uncover safe tiles when possible.

Getting Started
To run the Minesweeper game, follow these steps:

cd minesweeper

python new.py

Game Rules
The objective of Minesweeper is to uncover all tiles on the grid without detonating any bombs. Each tile may contain a number indicating the number of neighboring tiles that contain bombs. Use this information to strategically uncover tiles and flag potential bomb locations.

Controls
* Left Click: Uncover a tile.
* Right Click: Flag or unflag a tile suspected of containing a bomb.

Enjoy!
Thank you for checking out the Minesweeper game! We hope you enjoy playing and challenging yourself with this classic puzzle. If you have any feedback, suggestions, or issues to report, feel free to do that. Happy Minesweeping!




