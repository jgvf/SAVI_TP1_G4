#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import copy
import sys



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
        gray_image, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30)
        )

        #---------------------------------------
        # Deteção de conhecidos
        #---------------------------------------
        img_person_1=cv2.imread('./database/joao_figueiredo/1.jpg')
        img_person_2=cv2.imread('./database/emanuel/1.jpg')

        result_1 = cv2.matchTemplate(frame,img_person_1, cv2.TM_CCOEFF_NORMED)
        result_2 = cv2.matchTemplate(frame,img_person_2, cv2.TM_CCOEFF_NORMED)
        h,w,_=frame.shape
        _, value_max_1, _,max_loc_1 = cv2.minMaxLoc(result_1)
        cv2.rectangle(frame,(max_loc_1[0],max_loc_1[1]),(max_loc_1[0],max_loc_1[1]),(0,0,255),4)

        _, value_max_2, _,max_loc_2 = cv2.minMaxLoc(result_2)
        cv2.rectangle(frame,(max_loc_2[0],max_loc_2[1]),(max_loc_2[0]+w,max_loc_2[1]+h),(255,0,0),4)


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
