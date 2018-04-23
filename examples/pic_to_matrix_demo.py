"""
===================================
convertion of a picture to a matrix
===================================

An example of packege usage. It converts a picture "example.png" to
an ASCII matrix file and plots the result.
"""
import pixmix.pixmix as pixmix
import matplotlib.pyplot as plt
import scipy

if __name__=="__main__":
    filename = "example.png"

    # Convert an image to a matrix
    pix = pixmix.pixmix(filename)
    # Saves the matrix into ASCII file
    pixmix.saveTo(pix, filename)

    # Read the matrix from a file
    a = scipy.loadtxt(filename+".out", delimiter=" ")
    # Plot the matrix
    plt.imshow(a, cmap='gray_r')
    plt.xlabel("X index")
    plt.ylabel("Y index")
    plt.show()


