"""
Main Application Entry Point for the Hangman Game.
This module coordinates the flow between the UI, Game Logic, and Configuration.
"""

import sys
import random
from configurations import Config
from game_state import GameState
from word_bank import WORD_BANK
from ui import (
    display_header,
    display_message,
    display_divider,
    display_menu,
    prompt_menu_selection,
    get_valid_input,
    MessageType
)
from utility import clear_screen, pause
from validation import is_not_empty, is_alpha, is_single_char


class HangmanApp:
    """
    The main controller class that manages the application lifecycle and page routing.
    """

    def __init__(self) -> None:
        """Initialize the application with global configurations."""
        self.config = Config()

    def _get_random_word(self) -> str:
        """Selects a random word from the word bank."""
        return random.choice(WORD_BANK)

    def show_instructions(self) -> None:
        """Displays the game rules and instructions to the user."""
        clear_screen()
        display_header("HOW TO PLAY")
        
        instructions = [
            "A secret word has been chosen from the word bank.",
            "Your goal is to guess the word letter by letter.",
            f"You have a total of {self.config.max_attempts} incorrect attempts allowed.",
            "Each correct guess reveals the letter's position.",
            "If you run out of attempts, you lose the game."
        ]
        
        display_menu("Rules and Guidelines:", instructions)
        display_divider()
        pause()

    def play_game(self) -> None:
        """
        Manages the core game loop, including input handling, state updates, 
        and rendering the game board.
        """
        # Initializing a new game state
        target_word = self._get_random_word()
        game = GameState(target_word, self.config.max_attempts)
        
        while not game.is_win and not game.is_loss:
            clear_screen()
            display_header("GAME IN PROGRESS")
            
            # View current status information for play
            print(f"\nWord to guess:  {game.display_word}")
            print(f"Attempts left:  {game.attempts_left} / {game.max_attempts}")
            print(f"Guessed so far: {', '.join(sorted(game.guessed_letters)) if game.guessed_letters else 'None'}")
            display_divider()

            # Define the rules for verification of input
            validators = [is_not_empty, is_alpha, is_single_char]

            guess = get_valid_input("Enter your guess: ", validators).lower()

            # Prevent the same guess from being repeated
            if guess in game.guessed_letters:
                display_message(f"You already guessed '{guess}'. Try another one.", MessageType.WARNING)
                pause()
                continue
            
            if game.process_guess(guess):
                display_message(f"Your guess is correct, well done.", MessageType.SUCCESS)
            else:
                display_message(f"You guessed wrong, you lost an attempt.)
            pause()
        # Endgame: View the end result
        self.show_game_over(game)

    def show_game_over(self, game: GameState) -> None:
        """
        Displays the final result screen (Win or Loss).
        
        Args:
            game (GameState): The final state of the finished game.
        """
        clear_screen()
        display_header("GAME OVER")

        if game.is_win:
            display_message(f"Congratulations! You guessed the word: {game.target_word.upper()}", MessageType.SUCCESS)
        else:
            display_message(f"Game Over! You've run out of attempts.", MessageType.ERROR)
            display_message(f"The word was: {game.target_word.upper()}", MessageType.INFO)

        display_divider()
        pause()

    def run(self) -> None:
        """
        The main execution entry point. Displays the home menu and routes 
        the user based on their selection.
        """
        while True:
            clear_screen()
            display_header("WELCOME TO HANGMAN ALPHA")
            
            menu_options = ["Play New Game", "Instructions", "Exit Application"]
            choice = prompt_menu_selection("Main Menu Options:", menu_options)

            if choice == 1:
                self.play_game()
            elif choice == 2:
                self.show_instructions()
            elif choice == 3:
                display_message("Thank you for playing Hangman Alpha. Goodbye!", MessageType.NOTE)
                sys.exit(0)


# ==========================================
# Application Entry Point
# ==========================================

if __name__ == "__main__":
    try:
        app = HangmanApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nApplication terminated by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] A critical error occurred: {e}")
        sys.exit(1)
