#!/usr/bin/env python3

import tensorflow as tf
from tensorflow import keras
from keras import models
from keras.models import load_model

import numpy as np
import cv2

import matplotlib.pyplot as plt
import os

def get_calssName(classNo):
    if classNo == 0:
        return "Joao_Figueiredo"
    elif classNo == 1:
        return "Emanuel"



def main():

    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    cam=cv2.VideoCapture(0)
    font=cv2.FONT_HERSHEY_COMPLEX

    model=load_model('keras_model.h5')

    

    while True:
    
        check,frame = cam.read()
        if check is False:
            break
        frame = cv2.flip(frame,1)
        y_frame,x_frame,_ = frame.shape
       
        # ------------------------------------------------------
        # Detect persons using haar cascade classifier
        # ------------------------------------------------------
        gray_image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        y_gray,x_gray= gray_image.shape
        face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30)
        )

        # --------------------------------------
        # Visualization
        # --------------------------------------

        for (x, y, w, h) in face:
            crop_img=frame[y:y+h,x:x+w]
            img=cv2.resize(crop_img,(224,224))
            cv2.imshow('test', img)
            img=img.reshape(1,224,224,3)
            prediction=model.predict(img)
            classIndex=model.predict_classes(img)
            probabilityValue=np.amax(prediction)
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y-40), (x + w, y ), (0, 255, 0), -2)
            cv2.putText(frame,str(get_calssName(classIndex)),(x,y-10),font,0.75,(255,0,0),4)
             
            cv2.putText(frame,str(round(probabilityValue*100),2)+'%'+(180,75),font,0.7,(0,0,255),2)

        cv2.imshow('face recognhition', frame)
        
        key = cv2.waitKey(1)
        if key == 27: # esc
            break
            
    cam.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
 main()

