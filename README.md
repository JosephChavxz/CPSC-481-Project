# BlackJack with AI

## Contributors
- Matthew Jun
  - School Email: Matt.j@csu.fullerton.edu
  - Github: mwjun
- Leoanrdo Medrano
  - School Email: lm1014367@csu.fullerton.edu
  - Github: @FenTheDeer
- Joseph Chavez
  - School Email:jchavez0026@csu.fullerton.edu
  - Github: @JosephChavxz

## Project Overview

This project is a Python implementation of the card game Blackjack. It includes classes for the game itself, players, the dealer, and individual cards. The game can be played with multiple players, and includes an AI player that learns from a dataset containing real players game history. The AI players decisions are based on real players past experiences, specifically by looking at the outcomes of their past games.

## File Structure

Here's an overview of the main files and folders in this project:

- `blackjack.py`: This is the main script that runs the game. It imports and uses functions from the other scripts.

- `blackjackgame/card.py`: This script defines the Card class, which represents a card in the game, and the Deck class, which represents a deck of cards.

- `blackjackgame/game.py`: This script defines the Game class, which represents a game of Blackjack. It includes methods for dealing cards, playing a round, and checking the winner.

- `blackjackgame/player.py`: This script defines the Player class, which represents a player in the game. It includes methods for making moves, calculating the hand value, and checking if the player is busted. This also contains the classes for both the Dealer and AiPlayer classes, inherits from the Player class and overrides the method for making moves.

- `history/`: This folder contains JSON files with the history of moves for both real and AI player.

## How to Run the Project

Provide instructions on how to run your project. For example:

1. Clone the repository: `git clone https://github.com/JosephChavxz/CPSC-481-Project`
2. Navigate to the project directory: `cd CPSC-481-Project`
3. Run the main script: `python blackjack.py`
