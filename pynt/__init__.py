from os import path
from matplotlib import pyplot as plt

pynt_style_path = path.join(path.dirname(__file__), 'styles', 'pynt_style')
print(f"(DEBUG) pynt_style_path = {pynt_style_path}")

plt.style.use(pynt_style_path)
