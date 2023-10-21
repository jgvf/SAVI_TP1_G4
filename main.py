#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt


def main():
    # --------------------------------------
    # Initialization
    # --------------------------------------
    cam = cv2.VideoCapture(0)

    #Load the Classifier-pre-trained Haar Cascade classifier that is built into OpenCV
    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    
    # --------------------------------------
    # Execution
    # --------------------------------------
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
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # --------------------------------------
        # Visualization
        # --------------------------------------

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
