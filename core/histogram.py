import cv2
import numpy as np 

def equalize_histogram(image):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()
    cdf = hist.cumsum()

    cdf_masked = np.ma.masked_equal(cdf, 0)

    numerator = (cdf_masked - cdf_masked.min()) * 255
    denominator = (cdf_masked.max() - cdf_masked.min())

    if denominator == 0:
        denominator = 1  # CORREÇÃO: Um '=' (atribuição)
    
    cdf_normalized = np.ma.filled(numerator / denominator, 0).astype('uint8')

    image_equalized = cdf_normalized[image]

    return image_equalized

def apply_CLAHE(image_gray, clip_limit = 2.0, tile_size = (8, 8)):
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)
    image_CLAHE = clahe.apply(image_gray)
    return image_CLAHE