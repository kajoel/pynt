# pynt
Settings for Matplotlib

## Installation
`pip install git+https://github.com/kajoel/pynt`

## Tips and tricks
Download Latin Modern Roman (e.g. here: https://www.fontsquirrel.com/fonts/latin-modern-roman, you only need to install Latin Modern Roman, `lmroman10-regular.otf`).
Then, run the following in `python` to make Matplotlib find the new font (you only need to do this once):
```python
from matplotlib import font_manager
font_manager._rebuild()
```
Now, Pynt will use Latin Modern Roman as the default font when LaTeX is not used.