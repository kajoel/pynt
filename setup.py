import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pynt",
    version="0.0.1",
    author="Joel Karlsson, Carl Eklind",
    author_email="joelkarlsson97@gmail.com, carleklind@outlook.com",
    description="Settings for Matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kajoel/pynt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
    ],
    data_files=[('styles', ['styles/pynt_style'])],
)
