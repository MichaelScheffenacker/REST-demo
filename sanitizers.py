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
    try:
        value = float(value)
    except ValueError:
        raise ValueError("Amount has to be a float, e.g. 100.23 or 0.25567801")
    return value


def number(value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Number has to be a positive integer, e.g. 2")
    if not value > 0:
        raise ValueError("Number has to be a positive integer, e.g. 2")
    return value
