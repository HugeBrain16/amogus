"""sus"""

import string
import random

__version__ = "0.2.0"

SYMBOLS = list(string.printable.strip()[62:])
VOWELS = list("euioaEUIOA")
SUS_WORD = [f"s{char}s" for char in VOWELS[:5]]
SUS_WORD.append("amogus")
SUS_FACE = ["😳", "😎", "😭", "😠", "😤", "😂", "😥", "😱", "🤯"]


def amogusify(text: str, emoji: bool = False) -> str:
    """amogusify your text"""
    result = []

    if not text:
        return ""

    for word in text.split(" "):
        rng_emoji = random.randint(1, 5)
        rng_emoji_count = random.randint(1, 3)

        if word.startswith(":") and word.endswith(":"):  # skip emoji (?)
            result.append(word)
            continue

        has_symbol = False
        sym_count = 0
        sym = ""

        if word.lower() not in SUS_WORD and not word[-1].isdigit():
            for char in word[::-1]:
                if char in SYMBOLS:
                    has_symbol = True
                    sym_count -= 1
                    sym += char
                else:
                    break

            if has_symbol is True:
                word = word[:sym_count]

            if len(word) > 2:
                if word[-2:].lower() != "us":
                    if word[-1] in VOWELS:
                        word = word[:-1]
                        word += "us"
                    else:
                        if word != " ":
                            word += "us"
            elif len(word) > 1:
                if word != " " and word.lower() != "us":
                    word += "us"
            else:
                if word[-1] in VOWELS:
                    if word[-1].isupper():
                        word = word.replace(word[-1], f"S{word[-1].lower()}s")
                    else:
                        word = word.replace(word[-1], f"s{word[-1]}s")

            if has_symbol is True:
                word += sym

        if rng_emoji == 3 and emoji is True:
            word += " " + (random.choice(SUS_FACE) * rng_emoji_count)

        result.append(word)

    return " ".join(result)
