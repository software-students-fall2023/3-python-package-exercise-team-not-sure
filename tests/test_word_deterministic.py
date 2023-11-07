from brawndo.brawndo import word_deterministic

from io import StringIO
import sys
from contextlib import redirect_stderr
import pytest

texts = [
    "The be to of and",
    "a in that have I",
    "it for not on with.",
]
shifts = [0, 1, 2]
desireds = [
    "The,14\nbe,5\nto,1\nof,3\nand,0\n",
    "a,1\nin,7\nthat,1\nhave,4\nI,9\n",
    "it,15\nfor,10\nnot,4\non,15\nwith.,15\n"
]

# Zip all together
params = zip(texts, shifts, desireds)

@pytest.mark.parametrize("text,shift,desired", params)
def test_rainbow_deterministic(text, shift, desired):
    test_vector = word_deterministic(text, shift, testing=True)
    assert test_vector == desired