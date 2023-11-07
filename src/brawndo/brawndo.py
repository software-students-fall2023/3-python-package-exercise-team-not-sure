import termcolor
import colorama
colorama.init()
colorama.deinit()

from typing import Optional

import sys
printerr = lambda x: print(x, file=sys.stderr)

from random import randint, seed
randval = lambda _ : randint(0,15)

from brawndo.constants import *

def colorsafe(func):
    def wrapper(*args, **kwargs):
        colorama.reinit()
        try:
            retval = func(*args, **kwargs)
        except Exception as e:
            printerr(e)
            colorama.deinit()
            exit(1)
        colorama.deinit()
        return retval
    return wrapper

# "Function 1"
@colorsafe
def rainbow_deterministic(text: str, shift: int, testing=False) -> Optional[str]:
    test_vector = []
    for char in text:
        if char in values:
            color_value = (values[char] + shift) % 16
            color_name = colors[color_value]
            if color_name == 'black':
                colored_char = termcolor.cprint(char, "black", 'on_white', end='')
            else:
                colored_char = termcolor.cprint(char, color_name, end='')
            if testing:
                test_vector.append(f"{char},{color_name}")
        else:
            if testing:
                test_vector.append(f"{char},none")
    if testing:
        retval = "\n".join(test_vector)
        if retval[-1] != "\n":
            retval += "\n"
        return retval
    else:
        return None

# "Function 2"
@colorsafe
def word_deterministic(text: str, shift: int, testing=False) -> None:
    pass

# "Function 3"
@colorsafe
def rainbow_random(text: str, rndseed=None, testing=False) -> None:
    pass

# "Function 4"
@colorsafe
def word_random(text: str, operate_on_sentences: bool, rndseed=None, testing=False) -> None:
    pass