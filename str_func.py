# Some action to fix the bug

def to_upper(a: str) -> str:
    """Return uppercase string!!!"""
    return a.upper()


def to_capitalize(a: str) -> str:
    """Return capitalized string"""
    return ' '.join([x.capitalize() for x in a.split(' ')])
