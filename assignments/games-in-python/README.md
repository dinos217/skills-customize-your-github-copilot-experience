
# 📘 Assignment: Games in Python

## 🎯 Objective

Build the classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Description
Set up the game by creating a word list and initializing game variables to track the player's progress.

#### Requirements
Completed program should:

- Define a list of words that the game can randomly select from
- Randomly select one word at the start of the game
- Initialize tracking variables for guessed letters and remaining attempts (e.g., 6 wrong guesses allowed)


### 🛠️ Implement Guessing Logic

#### Description
Create the guessing mechanism that accepts player input, validates guesses, and updates the game state.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Display the current word progress using underscores for unknown letters (e.g., `_ _ _ _`)
- Track correctly and incorrectly guessed letters
- Decrease remaining attempts on wrong guesses
- Prevent duplicate guesses


### 🛠️ Game Flow and Win/Lose Conditions

#### Description
Implement the main game loop and determine game-ending conditions.

#### Requirements
Completed program should:

- Continue the game until the word is guessed or attempts run out
- Display a win message when the player correctly guesses the word
- Display a lose message when the player runs out of attempts (reveal the word)
- Show the number of remaining attempts after each guess
