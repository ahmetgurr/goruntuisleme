import numpy as np
import cv2 as cv


def Image_Inversion (Image):

    Yukseklik = Image.shape[0]
    Genislik = Image.shape[1]
    Kanallar = Image.shape[2]

    Boyut = (Yukseklik, Genislik, Kanallar)

    yeni_foto = np.zeros(Boyut, np.uint8)

    for x in range(0, Yukseklik):
        for y in range(0, Genislik):
            for c in range(0, Kanallar):
                yeni_foto[x, y, c] = 255 - Image[x, y, c]
    return yeni_foto


def main():

    orijinal_foto = cv.imread("elephant.jpg")

    cevirilmis_foto = Image_Inversion(orijinal_foto)


    cv.imwrite("cevirilmis_foto.png", cevirilmis_foto)
    cv.imshow("cevirilmis_foto.png", cevirilmis_foto)
    cv.waitKey(0)

if __name__ == '__main__':
    main()

