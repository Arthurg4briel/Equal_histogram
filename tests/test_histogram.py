import numpy as np
import pytest 
from core.histogram import equalize_histogram

def test_equalization_histogram_image_solid():
    img_solid = np.full((50, 50), 100, dtype= np.uint8)
    '''Com a imagem bruta, pegamos a função de equalizar e jogamos na imagem solida'''
    img_equalized = equalize_histogram(img_solid)

    assert np.array_equal(img_solid, img_equalized)

    assert img_equalized.shape == (50, 50)

def test_equalization_simple_image():
    img_test = np.array([
        [0, 50],
        [100, 200],
    ], dtype= np.uint8)

    img_equalized = equalize_histogram(img_test)

    assert np.array_equal(img_test, img_equalized)

    '''
    Para rodar o teste, use (na main.py) python -m pytest
    '''

    

