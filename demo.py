from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str


@dataclass
class ValidationResult:
    is_valid: bool


def validate_user(user: User) -> ValidationResult:
    # simple validation: name non-empty and email contains '@'
    if not user:
        return ValidationResult(is_valid=False)
    is_valid = bool(user.name and user.email and "@" in user.email)
    return ValidationResult(is_valid=is_valid)


def validate_email(user: User) -> ValidationResult:
    if not user or not user.email:
        return ValidationResult(is_valid=False)
    return ValidationResult(is_valid=("@" in user.email))
