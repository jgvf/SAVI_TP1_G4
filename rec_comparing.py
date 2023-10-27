#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import copy
import sys



def main():
  
    #template_1=cv2.imread('./database/joao_figueiredo/1.jpg')
    #template_2=cv2.imread('./database/emanuel/1.jpg')
    #template_3=cv2.imread('./database/joao_figueiredo/1.jpg')
    #template_1=cv2.resize(template_1,(200,200))
    #template_2=cv2.resize(template_2,(200,200))

    #cv2.imshow('template_1',template_1)
    #cv2.imshow('template_2',template_2)


    #face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Carregue o reconhecedor LBPH para reconhecimento facial
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Carregue o modelo treinado
    recognizer.read('./database/joao_figueiredo/1.jpg')

    # Capture a imagem da face que você deseja comparar
    imagem = cv2.imread('/database/emanuel/1.jpg')

    # Converta a imagem em escal de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces=imagem_cinza
    # Detecte a face na imagem de teste
    #faces = face_cascade.detectMultiScale(imagem_cinza)

    for (x, y, w, h) in faces:
        # Extraia a região da face
        face_roi = imagem_cinza[y:y+h, x:x+w]

        # Realize o reconhecimento facial
        id, confidence = recognizer.predict(face_roi)

        # Se a confiança for baixa, pode não ser uma correspondência
        if confidence < 100:
            print(f'ID da pessoa reconhecida: {id}')
        else:
            print('Pessoa não reconhecida')

    cv2.waitKey(0)
    cv2.destroyAllWindows()



















    while(True):
        key = cv2.waitKey(1)
        if key == 27: # esc
            break
                

    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()
