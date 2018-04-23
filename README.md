pixmix
----
A project to covert an image to a pixel matrix. The matrix then is saved in ASCII format. 

Getting started
----
The project uses Python Imaging Library (PIL). If you don't have it, do the following to install:
```
$ pip install Pillow
```
**Install development setup**

```
$ git clone https://github.com/egorseliunin/pixmix.git
$ cd pixfix
$ python setup.py install --user
```
If it doesn't work, add the path to the directory pixmix to $PYTHONPATH

Example of usage
----
**Command line**

copy `pixmix/pixmix.py` and your image (e.g. with the name 'image.png') to the same foulder and run the following command in the command line
```
$ python pixmix.py -n image.png
```
The output ASCII file is `*.out`.
To see alternative options for `pixmix.py` use the following command:
```
$ python pixmix.py -h
```
**Python script**

To use `pixmix.py` see example `examples/pic_to_matrix_demo.py`
