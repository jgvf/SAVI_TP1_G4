#!/usr/bin/env python3

import cv2
import matplotlib.pyplot as plt
import os


def main():
    cam=cv2.VideoCapture(0)
    face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    count=0
    nameID=str(input("Enter your name:")).lower()
    path='database/'+nameID
    isExist=os.path.exists(path)
    if isExist:
        print("Name Already Taken")
        nameID=str(input("Enter your name again:"))
    else:
        os.makedirs(path)


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
            
            count+=1
            name='./database/'+nameID+'/'+str(count)+'.jpg'
            print('Creating Images.......'+name)
            cv2.imwrite(name,frame[y:y+h,x:x+w])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 4)
            
        cv2.imshow('face detection', frame)
        #cv2.imread
        if count>100:
            break  

        key = cv2.waitKey(1)
        if key == 27: # esc
            break
            
    cam.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
 main()