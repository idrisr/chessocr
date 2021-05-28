from setuptools import setup
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chessocr",
    version="0.0.2",
    author="not Idris Raja",
    author_email="idris.raja@gmail.com",
    install_requires=['opencv-python', 'numpy'],
    url="https://github.com/idrisr/chessocr",
    project_urls={
        "Bug Tracker": "https://github.com/idrisr/chessocr/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
