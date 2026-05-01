from dataclasses import dataclass

WORD_BANK = ["code", "alpha", "internship", "python", "hangman", "programming"]


@dataclass(frozen = True)
class Config:
  max_attempts: str = 6

  
