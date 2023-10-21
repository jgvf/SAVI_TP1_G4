#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt


def main():
    cam = cv2.VideoCapture(0)

    while True:
        #Read video
        check,frame = cam.read()
        frame = cv2.flip(frame,1)
        y_frame,x_frame,_ = frame.shape
        #print('x frame',x_frame,'y frame',y_frame)
        #cv2.imshow('video_original', frame)
        
        #Convert the image to grayscale
        gray_image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        y_gray,x_gray= gray_image.shape
        #print('x_gray',x_gray,'y_gray',y_gray)
        cv2.imshow('video_gray', gray_image)

        #Load the Classifier-pre-trained Haar Cascade classifier that is built into OpenCV
        face_classifier = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        
        #Perform the Face Detection
        face = face_classifier.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        #Drawing a Bounding Box
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)

        cv2.imshow('face detection', frame)
        cv2.imread
        key = cv2.waitKey(1)
        if key == 27: # esc
            break
            
    cam.release()
    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()
