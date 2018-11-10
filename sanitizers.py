import re


def currency(value):
    if not isinstance(value, str):
        raise ValueError("Currency has to be a string, e.g. 'EUR'")
    if not len(value) == 3:
        raise ValueError("Currency has to consist of 3 letters, e.g. 'EUR'")
    if not re.fullmatch(r"([a-zA-Z]+)", value):
        raise ValueError("Currency has to consist of the letters A-Z, e.g. 'EUR'")
    return value.upper()


def amount(value):
    pass
