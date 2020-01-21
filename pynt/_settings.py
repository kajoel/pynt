from os import path
from matplotlib import pyplot as plt

__all__ = ["set_style", "use_tex", "set_fontsize"]
_STYLE_DIR = path.abspath(path.join(path.dirname(__file__), 'styles'))


def set_style(style="pynt"):
    plt.style.use(path.join(_STYLE_DIR, style))


def use_tex():
    pass


def set_fontsize():
    pass
