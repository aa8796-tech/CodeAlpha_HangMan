from dataclasses import dataclass
from typing import Optional


@dataclass(frozen = True)
class Config:
  max_attempts: int = 6
