from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from enum import Enum


class Characters(Enum):
    btn_upper = ascii_uppercase
    btn_lower = ascii_lowercase
    btn_digits = digits
    btn_spicial = "@#$%&*(){}[]|/?"


CHARACTER_NUMBER ={
    "btn_lower": len(Characters.btn_lower.value),
    "btn_upper": len(Characters.btn_upper.value),
    "btn_digits": len(Characters.btn_digits.value),
    "btn_spicial": len(Characters.btn_spicial.value),
}

GENERATE_PASSWORD =(
    "btn_refresh", 'btn_lower', "btn_upper", "btn_digits", "btn_spicial"
)

if __name__ == '__main__':
    for btn in CHARACTER_NUMBER.items():
        print(btn[0])


