# pynt
Settings for Matplotlib

## Installation
`pip install git+https://github.com/kajoel/pynt`

## Tips and tricks
Download Computer Modern for use without LaTeX (e.g. here: https://www.fontsquirrel.com/fonts/computer-modern, you only need to install CMU Serif Roman (`cmunrm`) which should appear as CMU Serif in Windows).
Then, run the following in `python` to make Matplotlib find the new font (you only need to do this once):
```python
from matplotlib import font_manager
font_manager._rebuild()
```
Now, Pynt will use CMU as the default font.