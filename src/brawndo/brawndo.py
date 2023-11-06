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
    for char in text:
        if char in values:
            color_value = (values[char] + shift) % 16
            color_name = colors[color_value]

            if color_name == 'black':
                colored_char = termcolor.colored(char, on_color='on_white')
            else:
                colored_char = termcolor.colored(char, color_name)

            if testing:
                printerr(f"{char},{color_name}")
            else:
                print(colored_char, end='')
        else:
            if testing:
                printerr(f"{char},none")
            else:
                print(char, end='')

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