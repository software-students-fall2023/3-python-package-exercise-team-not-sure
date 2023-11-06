from src.brawndo import rainbow_deterministic
import pytest



texts = [
    "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
    "The quick brown fox jumps over the lazy dog.",
    "The five boxing wizards jump quickly.",
]
shifts = [0, 1, 2]
# TODO: finish last desired
desireds = [
    "!,black\n\",red\n#,green\n$,yellow\n%,blue\n&,magenta\n',cyan\n(,white\n),light_grey\n*,dark_grey\n+,light_red\n,,light_green\n-,light_yellow\n.,light_blue\n/,light_magenta\n0,light_cyan\n1,black\n2,red\n3,green\n4,yellow\n5,blue\n6,magenta\n7,cyan\n8,white\n9,light_grey\n:,dark_grey\n;,light_red\n<,light_green\n=,light_yellow\n>,light_blue\n?,light_magenta\n@,light_cyan\nA,black\nB,red\nC,green\nD,yellow\nE,blue\nF,magenta\nG,cyan\nH,white\nI,light_grey\nJ,dark_grey\nK,light_red\nL,light_green\nM,light_yellow\nN,light_blue\nO,light_magenta\nP,light_cyan\nQ,black\nR,red\nS,green\nT,yellow\nU,blue\nV,magenta\nW,cyan\nX,white\nY,light_grey\nZ,dark_grey\n[,light_red\n\\,light_green\n],light_yellow\n^,light_blue\n_,light_magenta\n`,light_cyan\na,black\nb,red\nc,green\nd,yellow\ne,blue\nf,magenta\ng,cyan\nh,white\ni,light_grey\nj,dark_grey\nk,light_red\nl,light_green\nm,light_yellow\nn,light_blue\no,light_magenta\np,light_cyan\nq,black\nr,red\ns,green\nt,yellow\nu,blue\nv,magenta\nw,cyan\nx,white\ny,light_grey\nz,dark_grey\n{,light_red\n|,light_green\n},light_yellow\n~,light_blue\n",
    "T,yellow\nh,white\ne,blue\n ,none\nq,black\nu,blue\ni,light_grey\nc,green\nk,light_red\n ,none\nb,red\nr,red\no,light_magenta\nw,cyan\nn,light_blue\n ,none\nf,magenta\no,light_magenta\nx,white\n ,none\nj,dark_grey\nu,blue\nm,light_yellow\np,light_cyan\ns,green\n ,none\no,light_magenta\nv,magenta\ne,blue\nr,red\n ,none\nt,yellow\nh,white\ne,blue\n ,none\nl,light_green\na,black\nz,dark_grey\ny,light_grey\n ,none\nd,yellow\no,light_magenta\ng,cyan\n.,light_blue\n"
]

@pytest.mark.parametrize("text", texts)
@pytest.mark.parametrize("shift", shifts)
@pytest.mark.parametrize("desired", desireds)
def test_rainbow_deterministic(capsys, text, shift, desired):
    rainbow_deterministic(text, 0, testing=True)
    # Check that stderr matches desired output
    captured = capsys.readouterr()
    assert captured.err == desired
    