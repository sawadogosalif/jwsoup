import re


def clean_text(text: str) -> str:
    """Clean unwanted characters and format the verse text."""
    text = re.sub(r"\+\s*\.", ".", text)
    text = re.sub(r"\*\s*\+\s*;", ";", text)
    text = re.sub(r"\*\s*\+", "", text)
    text = text.replace(" + ", " ")
    text = text.replace(" * ", " ")
    return text
