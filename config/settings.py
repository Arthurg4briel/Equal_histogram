import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath("__main__")))

ASSETS_DIR = os.path.join(BASE_DIR, 'Desafio', 'assets')

INPUT_IMAGE_NAME = 'image.png'
OUTPUT_IMAGE_NAME = 'IMAGE_equalized.png'
OUTPUT_CLAHE_IMAGE_NAME = 'IMAGE_CLAHE.png'

INPUT_IMAGE_PATH = os.path.join(ASSETS_DIR, INPUT_IMAGE_NAME)
OUTPUT_IMAGE_PATH = os.path.join(ASSETS_DIR, OUTPUT_IMAGE_NAME)
OUTPUT_CLAHE_IMAGE_PATH = os.path.join(ASSETS_DIR, OUTPUT_CLAHE_IMAGE_NAME)