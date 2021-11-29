import random
from string import ascii_letters
from random import choices


def get_random_strings (string_length: int) -> str:
    random_string: str = "".join(choices(ascii_letters, k=string_length))
    return random_string
