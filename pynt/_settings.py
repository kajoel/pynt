from os import path
import matplotlib as mpl
from matplotlib import pyplot as plt

__all__ = ["set_style", "use_tex", "set_fontsize"]
_STYLE_DIR = path.abspath(path.join(path.dirname(__file__), 'styles'))


def set_style(style="pynt"):
    """
    Set Pynt style for Pyplot.
    """
    try:
        plt.style.use(path.join(_STYLE_DIR, style))
    except FileNotFoundError as e:
        raise ValueError(f"{style} ist not a Pynt style") from e


def use_tex(tex=True, font=None):
    """
    Turn on (or off) useage of TeX and set font. If font or tex is False,
    the font will not be changed.
    """
    # if font is None:
    #     if tex:
    #         font = {'family': 'serif', 'serif': ['DejaVu Sans']}
    #     else:
    #         font = {}
    # if font ist not False:
    #     mpl.rc('font', **font)
    mpl.rc('text', usetex=tex)


def set_fontsize(fontsize):
    """
    Set Pyplot fontsize.
    """
    mpl.rc('font', size=fontsize)
    mpl.rc('xtick', labelsize=fontsize)
    mpl.rc('ytick', labelsize=fontsize)
