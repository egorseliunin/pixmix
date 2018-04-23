"""
===================================
convertion of a picture to a matrix
===================================

An example of packege usage. It converts a picture "example.png" to
an ASCII matrix file and plots the result.
"""
import pixmix
import matplotlib as plt
import scipy

if __name__=="__main__":
    filename = "example.png"

    # Convert an image to a matrix
    pix = pixmix.pixmix(filename)
    # Saves the matrix into ASCII file
    pixmix.saveTo(pix, filename)

    a = scipy.loadtxt('test.out', delimiter=" ")
    plt.imshow(a)
    plt.show()


