from brawndo.brawndo import rainbow_random
import pytest

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "'as..[poavesf[  8a7*.f\"]",
    "!@#$%^&*()-=_+",
]
rndseeds = [
    4292285838037326215,
    6551146165133617474,
    -5650950641291792112
]

desireds = [
    "T,0\nh,12\ne,14\n ,7\nq,6\nu,10\ni,13\nc,8\nk,15\n ,0\nb,8\nr,14\no,3\nw,6\nn,11\n ,8\nf,14\no,3\nx,13\n ,2\nj,6\nu,7\nm,2\np,8\ns,15\n ,2\no,4\nv,7\ne,15\nr,13\n ,14\nt,3\nh,5\ne,9\n ,15\nl,8\na,14\nz,4\ny,0\n ,2\nd,1\no,8\ng,0\n.,13\n",
    "',0\na,0\ns,15\n.,12\n.,13\n[,9\np,0\no,12\na,2\nv,12\ne,5\ns,0\nf,2\n[,13\n ,12\n ,4\n8,9\na,10\n7,6\n*,6\n.,5\nf,11\n\",11\n],3\n",
    "!,10\n@,13\n#,13\n$,3\n%,0\n^,13\n&,11\n*,3\n(,2\n),8\n-,3\n=,8\n_,14\n+,8\n",
]

# Zip all together
params = zip(texts, rngseeds, desireds)


@pytest.mark.parametrize("text,rngseed,desired", params)
def test_rainbow_random(text, rndseed, desired):
    test_vector = rainbow_random(text, rndseed, testing=True)
    assert test_vector == desired
