from os import path
import matplotlib as mpl
from matplotlib import pyplot as plt

__all__ = ['set_style', 'use_tex', 'set_fontsize']
_ROOT_DIR = path.abspath(path.dirname(__file__))
_STYLE_DIR =path.join(_ROOT_DIR, 'styles')

def _parse_preamble(path):
    """
    Parse preamble at path.
    """
    with open(path, "r") as f:
        preamble = f.read().split('\n')
    return preamble

def set_style(style="pynt"):
    """
    Set Pynt style for Pyplot.
    """
    try:
        plt.style.use(path.join(_STYLE_DIR, style))
    except FileNotFoundError as e:
        raise ValueError(f"{style} ist not a Pynt style") from e


def use_tex(tex=True, preamble=True):
    """
    Turn on (or off) useage of TeX.

    preamble can be True (Pynt default preamble), a path to a preamble,
    a string (or list) version of the preamble or False (no preamble).
    """
    mpl.rc('text', usetex=tex)
    if preamble is False:
        return
    elif preamble is True:
        preamble = _parse_preamble(path.join(_ROOT_DIR, 'preamble.tex'))
    elif path.isfile(preamble):
        preamble = _parse_preamble(preamble)
    mpl.rcParams['text.latex.preamble'] = preamble


def set_fontsize(fontsize):
    """
    Set Pyplot fontsize.
    """
    mpl.rc('font', size=fontsize)
    mpl.rc('xtick', labelsize=fontsize)
    mpl.rc('ytick', labelsize=fontsize)
