
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Nedded for ALS
from scipy import sparse
from scipy.linalg import cholesky
from scipy.sparse.linalg import spsolve
from scipy.ndimage import uniform_filter


def boxcar_smoothing(image, kernel_size=3):
    """
    Applies boxcar (moving average) smoothing to a 2D image.
    
    Parameters:
    image (numpy.ndarray): 2D array representing the image.
    kernel_size (int): Size of the boxcar kernel (square) for smoothing.
    
    Returns:
    numpy.ndarray: Smoothed image.
    """
    smoothed_image = uniform_filter(image, size=kernel_size)
    return smoothed_image

def als(y, lam=1e6, p=0.1, itermax=10):
    r"""
    Implements an Asymmetric Least Squares Smoothing
    baseline correction algorithm (P. Eilers, H. Boelens 2005)
 
    Baseline Correction with Asymmetric Least Squares Smoothing
    based on https://web.archive.org/web/20200914144852/https://github.com/vicngtor/BaySpecPlots
 
    Baseline Correction with Asymmetric Least Squares Smoothing
    Paul H. C. Eilers and Hans F.M. Boelens
    October 21, 2005
 
    Description from the original documentation:
 
    Most baseline problems in instrumental methods are characterized by a smooth
    baseline and a superimposed signal that carries the analytical information: a series
    of peaks that are either all positive or all negative. We combine a smoother
    with asymmetric weighting of deviations from the (smooth) trend get an effective
    baseline estimator. It is easy to use, fast and keeps the analytical peak signal intact.
    No prior information about peak shapes or baseline (polynomial) is needed
    by the method. The performance is illustrated by simulation and applications to
    real data.
 
 
    Inputs:
        y:
            input data (i.e. chromatogram of spectrum)
        lam:
            parameter that can be adjusted by user. The larger lambda is,
            the smoother the resulting background, z
        p:
            wheighting deviations. 0.5 = symmetric, <0.5: negative
            deviations are stronger suppressed
        itermax:
            number of iterations to perform
    Output:
        the fitted background vector
 
    """
    L = len(y)
    D = sparse.eye(L, format='csc')
    D = D[1:] - D[:-1]  # numpy.diff( ,2) does not work with sparse matrix. This is a workaround.
    D = D[1:] - D[:-1]
    D = D.T
    w = np.ones(L)
    for i in range(itermax):
        W = sparse.diags(w, 0, shape=(L, L))
        Z = W + lam * D.dot(D.T)
        z = spsolve(Z, w * y)
        w = p * (y > z) + (1 - p) * (y < z)
    return z
