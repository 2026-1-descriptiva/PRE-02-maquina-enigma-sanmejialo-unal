import random

from homework.constants import LETTERS


def make_symmetric_mapping(seed, n=13):
    """Crea un plugboard usando el seed dado."""

    mapping = {letter: letter for letter in LETTERS}

    random.seed(seed)
    new_keys = random.sample(LETTERS[:n], n)
    remaining_letters = [letter for letter in LETTERS if letter not in new_keys]
    new_values = random.sample(remaining_letters, n)

    for k, v in zip(new_keys, new_values):
        mapping[k] = v
        mapping[v] = k

    mapping = "".join(mapping.values())

    return mapping


def make_plugboard(seed, n):
    """Crea un plugboard usando el seed dado."""
    return make_symmetric_mapping(seed, n)  # Reutiliza la función existente


def apply_plugboard(letter, plugboard):
    """Aplica el plugboard a una letra dada."""

    index = LETTERS.index(letter)
    return plugboard[index]
