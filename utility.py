import os
from typing import Callable, Optional, Type

# =========================
# Config
# =========================
BORDER_CHAR = "="
BORDER_LENGTH = 50


# =========================
# Core Utilities
# =========================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("Press Enter to continue...")

def read_input(prompt: str) -> str:
    return input(prompt).strip()

def convert(value: str, return_type: Optional[Type]):
    if return_type is None:
        return value
    return return_type(value)
