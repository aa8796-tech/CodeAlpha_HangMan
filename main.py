import random
from typing import List, Set
import os
import time

# =========================
# Game Configuration
# =========================

# Maximum number of allowed wrong attempts
TRIES = 6

# Word bank for the Hangman game
WORDS = ["code", "alpha", "programming", "python", "hangman"] 


# =========================
# Core Logic Functions
# =========================

def random_choice(words_seq: List[str]) -> str:
	"""
	Selects and returns a random word from the given sequence.

	Args:
		words_seq (List[str]): List of possible words.

	Returns:
		str: Randomly selected word.
	"""
	return random.choice(words_seq)


def indices_of(character: str, word: str) -> List[int]:
	"""
	Finds all positions of a given character in a word.

	Args:
		character (str): Character to search for.
		word (str): Word to search within.

	Returns:
		List[int]: List of indices where the character appears.
	"""
	return [i for i, c in enumerate(word) if c == character]


# =========================
# Input / Output Utilities
# =========================

def clear_screen():
	"""
	Clears the terminal screen depending on the operating system.
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def display_header():
	"""
	Prints a formatted game header/banner.
	"""
	print("\n" + "=" * 50)
	print(f"{' Hang Man ':=^50}")
	print("=" * 50)


def display_separator(sep_shape: str = "=", length: int = 30, pre: str = "\n", post: str = "\n"):
	"""
	Prints a customizable separator line for better UI readability.

	Args:
		sep_shape (str): Character used for the separator line.
		length (int): Number of repetitions of the separator character.
		pre (str): Text printed before the separator.
		post (str): Text printed after the separator.
	"""
	print(pre, sep_shape * length, sep="", end=post)


def ask_user_guess(guessed_so_far: Set[str]) -> str:
	"""
	Prompts the user to input a valid single-letter guess.

	Ensures:
	- Input is a single alphabet character.
	- The letter has not been guessed before.

	Args:
		guessed_so_far (Set[str]): Set of already guessed letters.

	Returns:
		str: Valid user guess.
	"""
	prompt = "Guess a character: "
	while True:
		try:
			guess = input(prompt).strip().lower()

			# Validate single alphabet character
			if len(guess) != 1 or not guess.isalpha():
				raise ValueError("(!) Invalid: Enter exactly one letter.")

			# Prevent repeated guesses
			if guess in guessed_so_far:
				raise ValueError(f"(!) You already guessed '{guess}'. Try something else.")

			return guess

		except ValueError as e:
			print(e)


# =========================
# Main Game Loop
# =========================

def main():
	"""
	Main function that runs the Hangman game loop.

	Handles:
	- Word selection
	- Player input
	- Game state updates
	- Win/Loss conditions
	"""
	# Initialize game state
	hangman_word = random_choice(WORDS)
	word_len = len(hangman_word)
	
	word_displayed = ['_'] * word_len
	tries_left = TRIES
	chars_to_guess = word_len
	
	# Track guessed letters
	all_guesses = set()
	wrong_guesses = []
	
	# Game loop
	while tries_left > 0 and chars_to_guess > 0:
		clear_screen()
		display_header()
		
		# Display current progress
		print(f"\nWord: {' '.join(word_displayed)} [{chars_to_guess} characters Left]")
		print(f"Missed letters: {', '.join(wrong_guesses)}")
		print(f"Tries left: {tries_left}")
		
		# Get user input
		user_guess = ask_user_guess(all_guesses)
		all_guesses.add(user_guess)
			
		# Process guess
		indices = indices_of(user_guess, hangman_word)
		display_separator()
		
		if indices:
			# Correct guess
			chars_to_guess -= len(indices)
			for i in indices:
				word_displayed[i] = user_guess
			print(f"-> Yes! '{user_guess}' is in the word.")
		else:
			# Incorrect guess
			tries_left -= 1
			wrong_guesses.append(user_guess)
			print(f"-> Sorry, '{user_guess}' is not there.")
			
		display_separator(pre="")
		time.sleep(1)

	# =========================
	# Game Result
	# =========================
	clear_screen()
	display_header()
	display_separator()
	
	if chars_to_guess == 0:
		print(f"CONGRATULATIONS! You Won. The word was: {hangman_word}")
	else:
		print(f"GAME OVER! The word was: {hangman_word}")
		print("Better luck next time!")

	display_separator(pre="")


if __name__ == '__main__':
	main()
