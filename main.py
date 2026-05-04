from configurations import Config
from ui import CLIUI, CLIUtility

config = Config()
utility = CLIUtility()
ui = CLIUI()

def home_page():
  utility.clear_screen()
  ui.display_header("Hang Man")
  utility.display_message("Welcome to the Hang Man Game.")
  utility.display_message("Follow the instructions for a pleasant user experience.", "note")
  uitility.display_divider()
  utility.display_menu("Instructions", instructions) # I'll write the instructions later. Don't run the program now

