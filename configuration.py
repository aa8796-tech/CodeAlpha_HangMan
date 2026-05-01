from dataclasses import dataclass

WORD_BANK = {}


@dataclass(frozen = True)
class Config:
  max_attempts: str = 6

  
