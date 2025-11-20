import cv2
from config. settings import (
    INPUT_IMAGE_PATH,
    OUTPUT_IMAGE_PATH,
    OUTPUT_CLAHE_IMAGE_PATH
)

def LOAD_IMAGE_GRAY(path):
    '''É carregado uma imagem em escala de cinza'''
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Não foi possivel carregar a imagem em: {path}")
    return img

def SAVE_IMAGE(path, img):
    try:
        cv2.imwrite(path, img)
        print(f"Imagem salva com sucesso em: {path}")
        return True
    except Exception as error:
        print(f"Erro ao salvar a imagem: {error}")
        return False