import termcolor
import colorama
colorama.init()
colorama.deinit()

import sys
printerr = lambda x: sys.stderr.write(x+"\n")

from random import randint, seed
randval = lambda _ : randint(0,15)

from constants import *

def colorsafe(func):
    def wrapper(*args, **kwargs):
        colorama.reinit()
        try:
            func(*args, **kwargs)
        except Exception as e:
            printerr(e)
            colorama.deinit()
            exit(1)
        colorama.deinit()
    return wrapper

# "Function 1"
@colorsafe
def rainbow_deterministic(text: str, shift: int, testing=False) -> None:
    pass

# "Function 2"
@colorsafe
def word_deterministic(text: str, shift: int, testing=False) -> None:
    pass

# "Function 3"
@colorsafe
def rainbow_random(text: str, rndseed=None, testing=False) -> None:
    if rndseed is not None and isinstance(rndseed, int):
        seed(rndseed)
    for char in text:
        random_value = randval()
        ref_color = colors[random_value]
        if char == "black":
            colored_char = termcolor.colored(char, "black", "on_white")
        else:
            colored_char = termcolor.colored(char, ref_color)
        if testing:
            printerr(f"{char},{ref_color}")
        else:
            termcolor.cprint(char, ref_color)

# "Function 4"
@colorsafe
def word_random(text: str, operate_on_sentences: bool, rndseed=None, testing=False) -> None:
    pass