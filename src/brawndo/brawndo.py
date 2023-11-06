import termcolor
import colorama
colorama.init()

import sys
printerr = lambda x: sys.stderr.write(x+"\n")

from random import randint, seed
randval = lambda _ : randint(0,15)

from constants import *

# "Function 1"
def rainbow_deterministic(text: str, shift: int, testing=False) -> None:
    pass

# "Function 2"
def word_deterministic(text: str, shift: int, testing=False) -> None:
    pass

# "Function 3"
def rainbow_random(text: str, rndseed=None, testing=False) -> None:
    pass

# "Function 4"
def word_random(text: str, operate_on_sentences: bool, rndseed=None, testing=False) -> None:
    pass