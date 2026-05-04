import os
from typing import List, Callable

# ==========================================
# UI Configuration Constants
# ==========================================
BORDER_CHAR = "="
BORDER_LENGTH = 50

class CLIUtility:
    """
    A utility class providing basic, independent tools for CLI operations.
    These methods handle simple screen and input tasks without being tied
    to any specific UI layout or application logic.
    """

    @staticmethod
    def pause() -> None:
        """Pause the program execution until the user presses Enter."""
        input("Press Enter to continue...")

    @staticmethod
    def clear_screen() -> None:
        """Clear the terminal screen based on the operating system."""
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def display_divider(border_char: str = BORDER_CHAR, border_length: int = BORDER_LENGTH) -> None:
        """
        Display a divider line without excessive vertical spacing.
        """
        print(border_char * border_length)
        
    @staticmethod
    def display_menu(title: str, items: List[str], items_padding: int = 2) -> None:
        """
        Displays a title followed by a numbered list of items.
        
        Args:
            title (str): The title of the menu.
            items (List[str]): A list of options to display.
            items_padding (int): Spaces to pad the item numbers for alignment.
        """
        print(title)
        for i, item in enumerate(items, start=1):
            # Fixed: Using single curly braces for correct f-string formatting
            print(f"{i:>{items_padding}}. {item}")

    @staticmethod
    def handle_input(prompt: str, validator: Callable[[str], bool], error_message: str) -> str:
        """
        Continuously prompt the user for input until it passes the validation function.
        
        Args:
            prompt (str): The text to display when asking for input.
            validator (Callable[[str], bool]): A function that returns True if input is valid.
            error_message (str): The text to display if the input is invalid.
            
        Returns:
            str: The validated user input.
        """
        while True:
            user_input = input(prompt).strip()
            if validator(user_input):
                return user_input
            print(error_message)


class CLIUI:
    """
    A class responsible for structuring the visual layout and flow of the application.
    It utilizes CLIUtility to build complex, standardized UI components.
    """

    @staticmethod
    def display_header(title: str) -> None:
        """
        Display a standardized header with borders and a centered title.
        
        Args:
            title (str): The text to display inside the header.
        """
        CLIUtility.display_divider()
        print(f"{title:
                 ^{BORDER_LENGTH}}")
        CLIUtility.display_divider()

    @staticmethod
    def prompt_menu_selection(menu_title: str, menu_items: List[str], error_message: str = "Invalid choice. Please try again.") -> int:
        """
        Display a full menu layout and safely get the user's valid integer choice.
        This method acts as a UI component and leaves the action routing to the main engine.
        
        Args:
            menu_title (str): The title to display above the menu.
            menu_items (Iterable[str]): The list of options available to the user.
            error_message (str): Message to display upon an invalid selection.
            
        Returns:
            int: The validated choice as an integer (1-based index).
        Raises:
            ValueError: if `menu_items` is empty.
            TypeError: if `menu_items` is not iterable
        """
        if not isinstance(menu_items, Iterable):
            raise TypeError("The menu should be iterable")
        if menu_items:
          # 1. Draw the UI components
          CLIUtility.display_menu(menu_title, menu_items)
          CLIUtility.display_divider()
        
          # 2. Define the validation logic (must be digits and within the list range)
          validator = lambda x: x.isdigit() and 1 <= int(x) <= len(menu_items)
        
          # 3. Get validated input using the utility tool
          choice = CLIUtility.handle_input(
            prompt="Enter your choice: ", 
            validator=validator, 
            error_message=error_message
          )
        
          # 4. Return the integer choice (SRP: Only get the choice, do not execute the action here)
          return int(choice)
        raise ValueError("The list must contain at least one item")
