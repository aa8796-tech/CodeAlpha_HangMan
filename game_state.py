class GameState:
    """
    Manages the state and logic of a single Hangman game session.
    """

    def __init__(self, target_word: str, max_attempts: int) -> None:
        """
        Initialize a new game state.

        Args:
            target_word (str): The secret word that the player needs to guess.
            max_attempts (int): The total number of allowed incorrect guesses.
        """
        self.target_word: str = target_word.lower()
        self.max_attempts: int = max_attempts
        self.attempts_left: int = max_attempts
        self.guessed_letters: set[str] = set()

    @property
    def display_word(self) -> str:
        """
        str: The current state of the word with unguessed letters hidden as underscores.
             Example: If target is "python" and guesses are {'p', 't'}, returns "p _ t _ _ _".
        """
        return " ".join(char if char in self.guessed_letters else "_" for char in self.target_word)

    @property
    def is_win(self) -> bool:
        """bool: True if all letters in the target word have been guessed, False otherwise."""
        # If there are no hidden parts ("_") in the display word, the player has won.
        return "_" not in self.display_word

    @property
    def is_loss(self) -> bool:
        """bool: True if the player has no remaining attempts, False otherwise."""
        return self.attempts_left <= 0

    def process_guess(self, guess: str) -> bool:
        """
        Process a player's letter guess.

        Adds the letter to the guessed_letters set. If the letter is not present 
        in the target word, it decrements the attempts_left counter.

        Args:
            guess (str): A single character string guessed by the player.
        """
        guess = guess.lower().strip()
        self.guessed_letters.add(guess)
        
        if guess not in self.target_word:
            self.attempts_left -= 1
            return False
        return True
 
