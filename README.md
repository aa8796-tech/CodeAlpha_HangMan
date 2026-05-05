# CodeAlpha Hangman
A Command Line Interface (CLI) Hangman game written in Python. This project is structured into multiple modules to separate game logic, user interface, and input validation, demonstrating maintainable software design principles.
## Overview
This project implements the classic Hangman game. It tracks user attempts, validates inputs, and manages the game state through separate Python files rather than a monolithic script. The architecture is designed to make adding new features and modifying existing ones straightforward.
## Features
 * **Modular Structure:** The codebase is divided into distinct modules for UI presentation, core logic, input validation, and configuration.
 * **Input Validation Engine:** Implements a reusable validation system to ensure user input is a single alphabetical character and handles duplicate guesses seamlessly.
 * **CLI Interface:** Provides a formatted text-based menu, clear status indicators (e.g., success, error, warning), and visual boundaries for a structured user experience.
 * **State Management:** The GameState class independently tracks the target word, remaining attempts, and guessed letters without relying on the UI layer.
## Installation & Execution
### Prerequisites
 * Python 3.8 or higher.
### Steps
 1. Clone the repository:
   ```bash
   git clone https://github.com/aa8796-tech/CodeAlpha_HangMan.git
   
   ```
 2. Navigate to the project directory:
   ```bash
   cd CodeAlpha_HangMan
   
   ```
 3. Run the game:
   ```bash
   python main.py
   
   ```
## How to Play
 1. Run the script and select **Play New Game** from the main menu.
 2. The game will select a random word from the internal word bank. You have **6 attempts** (configurable) to guess it.
 3. Type one letter at a time and press Enter.
 4. You win if you guess the word before running out of attempts. If you reach 0 attempts, you lose, and the word is revealed.
## Project Structure
The project files are organized to enforce the Single Responsibility Principle:
 * **main.py**: The application entry point. It controls the main menu routing, initializes the game components, and manages the overall game loop.
 * **game_state.py**: Contains the GameState class. It manages the pure logic of the game: tracking the target word, counting remaining attempts, processing guesses, and checking for win/loss conditions.
 * **ui.py**: Handles all visual presentation. It contains functions for printing formatted menus, structured headers, and standardized system messages based on MessageType.
 * **validation.py**: A validation engine that uses higher-order functions to check input rules (e.g., is_not_empty, is_alpha, is_single_char).
 * **utility.py**: Contains general console helper functions, such as clearing the terminal screen, pausing execution, and formatting console borders.
 * **configurations.py**: Contains a frozen dataclass for global game settings, primarily the default max_attempts.
 * **word_bank.py**: Contains the repository list of secret words used in the game.
## Customization and Expansion
Because the code logic is decoupled from the UI, modifying the game is efficient. Here are actionable ways to extend the project:
### 1. Change Difficulty Constraints
 * Open configurations.py and modify the max_attempts value in the Config dataclass to give the player more or fewer chances. This change will automatically reflect across the game logic.
### 2. Update the Word List or Add Categories
 * Open word_bank.py and add or remove strings from the WORD_BANK list.
 * **To add categories:** Change WORD_BANK into a dictionary (e.g., {"Animals": [...], "Tech": [...]}). In main.py, prompt the user to select a category key before the GameState is initialized.
### 3. Modify the UI Layout
 * Open utility.py and change the variables BORDER_CHAR (e.g., from = to *) or BORDER_LENGTH to alter the width and style of headers and menus across the entire game instantly.
### 4. Implement a Hint Feature
 * In game_state.py, add a new method provide_hint() that selects an unguessed letter from target_word and adds it to guessed_letters, while decrementing attempts_left.
 * In main.py, add logic inside the play_game loop to catch a specific input (like ?) to trigger the hint method.
### 5. Add ASCII Art
 * Create a list of multi-line strings representing the hangman stages. In ui.py, create a function draw_hangman(attempts_left: int) that prints the corresponding string. Call this function in the main game loop in main.py before displaying the display_word.
## License
This project is licensed under the MIT License.
## Author
**AbdElMoneim Ali Ali**
 * **GitHub:** aa8796-tech
