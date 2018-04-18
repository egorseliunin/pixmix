from setuptools import setup


setup(
    name = "pixmix",
    version = "0.0.1",
    author = "IPFN Reflectometry group",
    author_email = "eseliunin@ipfn.tecnico.ulisboa.pt",
    description = ("A tool to covert an image to a pixel matrix"),
    license = "GPLv3",
    keywords = "pixel matrix",
    url = "",
    packages=['pixmix'],
    #ong_description=read('README.md'),
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
