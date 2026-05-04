from dataclasses import dataclass
from typing import Callable, List

# =========================
# Validation Result
# =========================

@dataclass
class ValidationResult:
    is_valid: bool
    message: str = ""


# =========================
# Types
# =========================

Validator = Callable[[str], ValidationResult]


# =========================
# Validation Engine
# =========================

def validate(value: str, validators: List[Validator]) -> ValidationResult:
    for v in validators:
        result = v(value)
        if not result.is_valid:
            return result
    return ValidationResult(True)


# =========================
# Validators
# =========================

def is_not_empty(value: str) -> ValidationResult:
    if not value:
        return ValidationResult(False, "Input cannot be empty")
    return ValidationResult(True)


def is_alpha(value: str) -> ValidationResult:
    if not value.isalpha():
        return ValidationResult(False, "Only letters allowed")
    return ValidationResult(True)


def is_single_char(value: str) -> ValidationResult:
    if len(value) != 1:
        return ValidationResult(False, "Enter exactly one character")
    return ValidationResult(True)
