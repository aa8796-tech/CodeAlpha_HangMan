class CLIUtility:
  @staticmethod
  def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

  @staticmethod
  def menu(items: List):
    CLIUtility.display_divider()
    for index, item in enumerate(items, start=1):
      print(f"{index}. {item}")
class CLIUI:
  @staticmethod
  def render_home_page(title):
    
    
