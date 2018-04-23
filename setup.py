import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pixmix",
    version = "0.0.2",
    author = "IPFN Reflectometry group",
    author_email = "eseliunin@ipfn.tecnico.ulisboa.pt",
    description = ("A tool to covert an image to a pixel matrix"),
    license = "GPLv3",
    keywords = "pixel matrix",
    url = "",
    packages=['pixmix'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: alpha ",
        "Topic :: Data analysis",
        "License :: GPLv3 license",
    ],
    install_requires=[
          'numpy','scipy','Pillow',
    ],
    scripts=[]
)
