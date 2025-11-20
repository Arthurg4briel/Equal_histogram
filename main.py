import cv2
from config import settings
from core.histogram import equalize_histogram, apply_CLAHE
from utils.io import LOAD_IMAGE_GRAY, SAVE_IMAGE
from config.settings import (
    INPUT_IMAGE_PATH,
    OUTPUT_IMAGE_PATH,
    OUTPUT_CLAHE_IMAGE_PATH
)

def run():

    print("Iniciando a equalização")

    IMG_ORIGINAL = LOAD_IMAGE_GRAY(INPUT_IMAGE_PATH)

    if IMG_ORIGINAL is None:
        print("Encerrando...")
        return

    print ("Aplicando a equalização")
    image_equalized = equalize_histogram(IMG_ORIGINAL)

    SAVE_IMAGE(OUTPUT_IMAGE_PATH, image_equalized)

    print("Aplicando CLAHE")
    image_CLAHE = apply_CLAHE(IMG_ORIGINAL)

    SAVE_IMAGE(OUTPUT_CLAHE_IMAGE_PATH, image_CLAHE)

    '''Mostrando os resultados da equalização'''
    print("Resultados:")
    try:
        cv2.imshow("- Imagem original", IMG_ORIGINAL)
        cv2.imshow("- Imagem equalizada", image_equalized)
        cv2.imshow("- Imagem equalizada por CLAHE", image_CLAHE)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except cv2.error:
        print("Não foi possivel executar")

    print("Procedimento concludo")

if __name__ == "__main__":
    run()
