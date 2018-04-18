"""
Converts an image to a pixel 2D matrix.
"""

import os
import sys
import scipy
import argparse
import numpy as np
import PIL.Image

def pisxmix(filename, directory=None, xpix=None, ypix=None):
    """
    Converts an image to a pixel 2D matrix.

    Note: It assigns the white color (255,255,255) to 0 and all the others to 1

    Parameters
    ----------
    filename: str
        Filename of the image to convert
    directory: str
        Path of the directory the image is saved in. Defaults to the
        directory of the invoked script.
    xpix, ypix: int
        Number of points(pixels) along x and y axes. If (xpix, ypix) unequal to
        the pixel matrix shape, pads the output matrix with zeros to (xpix, ypix).
        Defoults (xpix, ypix) equal to the pixel matrix shape.
    Returns
    -------
    pix: numpy 2D array
        A pixel 2D array
    """
    if directory is None:
        directory = os.getcwd()
        if os.path.basename(directory) == "Notepad++":
            directory = os.path.dirname(sys.argv[0])

    full_path = os.path.abspath(
        os.path.join(directory, "{}".format(filename)))

    pic = PIL.Image.open(full_path)
    pix = np.sum(np.array(pic), axis=2)
    # Assign the white color (255,255,255) to 0 and all the others to 1
    pix[pix != 255*3] = 1
    pix[pix == 255*3] = 0

    # Pad to (xpix, ypix):
    xpix = xpix or pix.shape[1]
    ypix = ypix or pix.shape[0]
    pix = np.pad(pix, ((0, ypix - pix.shape[0]), (0, xpix - pix.shape[1])), 'constant', constant_values=(0))

    return pix

def saveTo(array, filename, directory=None, extention=".out", verbose=True):
    """
    Save an array to the current working directory or directory of the
    invoked script.

    Parameters
    ----------
    array: numpy array
        An array to be saved
    filename: str
        Filename of the saved array
    directory: str
        Path of the directory the array is saved in. Defaults to the
        directory of the invoked script.
    verbose: bool
        If True, print the full path of the saved file.

    Returns
    -------
    None

    """
    # Set directory of the invoked script as default
    if directory is None:
        directory = os.getcwd()
        if os.path.basename(directory) == "Notepad++":
            directory = os.path.dirname(sys.argv[0])

    # Create the directory if it does not exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    full_path = os.path.abspath(
        os.path.join(directory, "{}.out".format(filename,extention)))

    scipy.savetxt(full_path, array, delimiter=" ", fmt="%i")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert an image to a pixel matrix',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--filename',
                        help='A name of an image to convert',
                        required=True, default=None)
    parser.add_argument('-p', '--path',
                        help='A path to the image file',
                        required=False, default=None)
    parser.add_argument('-sp', '--savepath',
                        help='A path where the pixel matrix to save',
                        required=False, default=None)
    parser.add_argument('-xdim', '--xdimention',
                        help='A dimention of the pixel matrix along x axes.',
                        required=False, default=None)
    parser.add_argument('-ydim', '--ydimention',
                        help='A dimention of the pixel matrix along y axes.',
                        required=False, default=None)

    args = parser.parse_args()
    filename = args.filename
    path = args.path
    savepath = args.savepath
    xdim = args.xdimention
    if xdim:
        xdim = int(xdim)
    ydim = args.ydimention
    if ydim:
        ydim = int(ydim)

    pix = pisxmix(filename, directory=path, xpix=xdim, ypix=ydim)
    saveTo(pix, filename, directory=savepath)



